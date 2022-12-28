import pandas as pd
mydataset = {'bikes':["honda","splender","scooty"], 'meilage':[40,50,35]}
mydata =pd.DataFrame(mydataset)
#we can also change the index values
#Inder_change = pd.DataFrame(mydataset, index = ['b1','b2','b3'])
#print(Inder_change)
#print(Inder_change.loc['b2'
print(mydata)
print(mydata.loc[0])

#print(mydata.loc[[0,1]])
#loc - locate is used to print only required things : compare the above two for more understanding
#to check the version of the pandas we can use _version_
#using pandas Series is used to print the data in column type one by one,[one dimensional array] and it also defines the dtype
a = [1,6,5]
series = pd.Series(a)
print(series)
HAPPY = pd.Series(a, index = [10,20,30])
print(HAPPY) #Lables - it can be used to access a specified value, similiar to our indexes


#we can also locate rows in DataFrames

#comma seperated files
df=pd.read_csv('Data1.txt')
print(df)
#read_csv is used to read the custom document
#read_json is similar csv , json is mainly used when the data is vey big
#to_string is used to print the entire data
#head() function is used to get the topdata of the document
#if we give head() then the 1st five data elements will print automatically
#tail() is opposite to head()
#info() gives more information about the dataset
#non null value indicates there is no value presents, not a 0

print(df.head(2))
print(df.tail(2))
print(df.info())
import numpy as np
import pandas as pd

# Series - Creating a Series by passing a list of values, letting pandas create a default integer index:

s = pd.Series([1, 3, 5, np.nan, 6, 8])

print(s)
print(s[0])

s1 = pd.Series([1, 3, 5, 6, 8])

print(s1)

# Creating a DataFrame by passing a NumPy array, with a datetime index using date_range() and labeled columns:


dates = pd.date_range("20130101", periods=6)

print(dates)

# random float values
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df)



print(df)

df.groupby("A")[["C", "D"]].sum()


print(df.groupby(["A", "B"]).sum())


tuples = list(
    zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )
)


index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

df2 = df[:4]

df2

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
#
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)

print(df)

# another complex data
print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))


# time series

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

plt.legend(loc='best');