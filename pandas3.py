# time series
import pandas as pd
import numpy as np
rng = pd.date_range("1/1/2012", periods=100, freq="S")

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

print(ts)

ts.resample("5Min").sum()


import matplotlib.pyplot as plt

plt.close("all")


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

ts = ts.cumsum()

print(ts)

ts.plot();


df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)

df = df.cumsum()

print(df)

plt.figure();

df.plot();

plt.legend(loc='best')