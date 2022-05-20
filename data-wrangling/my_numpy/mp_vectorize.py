import numpy as np


def find_count_and_maxlen():
    print(
        'foo %s' % np.vectorize(len)(df1.values.astype(str)).max(axis=0),
        'bar %s' % np.vectorize(len)(df2.values.astype(str)).max(axis=0)
    )


find_count_and_maxlen()