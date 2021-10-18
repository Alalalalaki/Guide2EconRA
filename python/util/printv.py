from datetime import datetime


def printt(x):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


def printf(x, f=4):
    # print([f'{i:.{f}f}' for i in x])
    print([round(i, f) for i in x])
