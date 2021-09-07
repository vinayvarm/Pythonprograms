import pandas as pd
name=pd.Series([2,5,6,8],name="vinay")
# print(name)
# print((name.shape))
# print((name.sort_index))
# print((name.nlargest))
# print(name.max)
# print(name.round)
print(name.sum)


print(sum(name.values))
df=pd.DataFrame([[4,5],[3,6],[8,9]],index=["a","b","c"],columns=["d","e"])
print((df))
print(type(df["d"]))
print(df["e"])
df.to_csv("data.csv")
readdata=pd.read_csv("data.csv")
print(readdata)