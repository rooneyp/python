import pandas as pd
import numpy as np
# import os
# from os import path
import pathlib
from pathlib import Path

# see https://www.kdnuggets.com/2021/03/pandas-big-data-better-options.html
n_rows = 1_000_000
n_cols = 1000
for i in range(1, 3): # gen 2 18GB files
    filename = 'analysis_%d.csv' % i
    output_dir = Path('/Users/paul/Dev/Data')
    file_path = pathlib.PurePath(output_dir, filename)

    output_dir.mkdir(exist_ok=True)
    # os.makedirs(output_dir)

    df = pd.DataFrame(np.random.uniform(0, 100, size=(n_rows, n_cols)), columns=['col%d' % i for i in range(n_cols)])
    print('Saving', file_path)
    df.to_csv(file_path, index=False)
df.head()
