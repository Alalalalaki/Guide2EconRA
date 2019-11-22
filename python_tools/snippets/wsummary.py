"""
This code provide weighted statistic summary for data
Source: stolen from Spencer Lyon's "Replicating ADH 2013"
"""

import numpy as np
import pandas as pd

# Helper routines for weighted descriptive stats
def xbar(x, w):
    return np.dot(x, w) / np.sum(w)


def w_stdev(x, w):
    n = x.shape[0]
    W = np.sum(w)
    xb = xbar(x, w)
    return np.sqrt((n/(W * (n - 1))) * np.sum(w * (x - xb)**2))


def w_mean_std(x, w):
    return xbar(x, w), w_stdev(x, w)


def wquantile(vals_in, weights_in, probs_in):
    """
    Taken from StatsBase.jl
    """
    weights = np.asarray(weights_in)
    probs = np.asarray(probs_in)

    if isinstance(vals_in, pd.DataFrame):
        datas = [wquantile(vals_in[c], weights, probs) for c in vals_in.columns]
        return pd.concat(datas, axis=1)

    vals = np.asarray(vals_in)

    # full sort
    inds = np.argsort(vals)
    v = vals.copy()[inds]
    w = weights.copy()[inds]
    wsum = w.sum()

    # prepare percentiles
    p_inds = np.argsort(probs)
    p = np.clip(probs.copy()[p_inds], 1e-10, 1-1e-10)

    # prepare out vector
    N = v.size
    out = np.empty(p.size)
    out[:] = v[-1]

    # start looping on quantiles
    cumulative_weight, Sk, Skold = 0.0, 0.0, 0.0
    vk, vkold = 0.0, 0.0
    k = 0
    for i in range(p.size):
        h = p[i] * (N - 1) * wsum
        if h == 0:
            # happens when N or p or wsum equal zero
            out[p_inds[i]] = v[0]
        else:
            while Sk <= h:
                # happens in particular when k == 0
                vk = v[k]
                wk = w[k]
                cumulative_weight += wk
                if k >= N:
                    # out was initialized with maximum v
                    return out
                k += 1
                Skold, vkold = Sk, vk
                vk = v[k]
                wk = w[k]
                Sk = (k - 1) * wk + (N - 1) * cumulative_weight
            # in particular, Sk is different from Skold
            g = (h - Skold) / (Sk - Skold)
            out[p_inds[i]] = vkold + g * (vk - vkold)

    if isinstance(vals_in, pd.Series):
        res = pd.DataFrame(index=probs, data={vals_in.name: out})

    res.index.name = "quantile"
    return res


def wsummary(df, weights, qs=None):
    "looks like Stata's summarize variable [aw=weights], detail"
    if isinstance(df, pd.Series):
        return wsummary(df.to_frame(), weights, qs)

    if not isinstance(df, pd.DataFrame):
        msg = "wsummary only works with pandas Series or DataFrame"
        raise ValueError(msg)

    if qs is None:
        qs = [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]

    if len(qs) > 0:
        quants = wquantile(df, weights, qs)
        quants.index.name = None
        new_index = ["{0:d}%".format(int(i*100)) for i in quants.index]
        quants.index = ["{0:d}%".format(int(i*100)) for i in quants.index]
        quantsT = quants.T
    else:
        quantsT = pd.DataFrame(index=df.columns)

    # add other descriptive stats
    quantsT["count"] = df.count()
    quantsT["mean"] = df.aggregate(lambda x: xbar(x, weights))
    quantsT["std"] = df.aggregate(lambda x: w_stdev(x, weights))
    quantsT["min"] = df.min()
    quantsT["max"] = df.max()
    out = quantsT.T

    if len(qs) > 0:
        row_order = ["count", "mean", "std", "min"] + new_index + ["max"]
        return out.loc[row_order]
    else:
        return out
