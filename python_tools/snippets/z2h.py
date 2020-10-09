"""
This code is generally borrown from under-maintained pkg `japandas`
and used to turn 「全角」strings to 「半角」strings.
"""

__version__ = 0.1

from unicodedata import normalize

# soundmarks require special handlings
_ZALPHA = ('ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ'
           'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ')
_ZSYMBOL = '！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～　'
_ZDIGIT = '０１２３４５６７８９'

# mapping from full-width to half-width
_ALPHA_MAPPER = {c: normalize('NFKC', c) for c in _ZALPHA}
_DIGIT_MAPPER = {c: normalize('NFKC', c) for c in _ZDIGIT}
_SYMBOL_MAPPER = {c: normalize('NFKC', c) for c in _ZSYMBOL}

# adding symbols that un-normalizable
# https://www.utf8-chartable.de/unicode-utf8-table.pl?start=12224&names=-&utf8=string-literal
_ZSYMBOL_MAPPER = {"〜": "~", }
_SYMBOL_MAPPER.update(_ZSYMBOL_MAPPER)


def _ord_dict(dict):
    return {ord(k): v for k, v in dict.items()}


# for unicode.translate
_Z2H_ALPHA = _ord_dict(_ALPHA_MAPPER)
_Z2H_DIGIT = _ord_dict(_DIGIT_MAPPER)
_Z2H_SYMBOL = _ord_dict(_SYMBOL_MAPPER)

mapper = dict()
mapper.update(_Z2H_ALPHA)
mapper.update(_Z2H_DIGIT)
mapper.update(_Z2H_SYMBOL)


def str_z2h(string: str, ):
    try:
        res = string.translate(mapper)
        return res
    except AttributeError:
        return string
