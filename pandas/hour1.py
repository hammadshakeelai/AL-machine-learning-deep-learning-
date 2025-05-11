# # series 1D
# # dataframe 2D

# # missing data as Nan

# # data wrangling rearranging data /playing with data/data maniplation
import pandas as pd
import numpy as np
# s = pd.Series([45,50,55,60,65,70],index=[10,2,3,4,5,6])
# s = pd.Series([45,50,55,60,65,70],index=range(0,6))#default
# print(s)
# s.index

# random_arr = np.random.randint(10,size=(100))
# random_arr.shape

# # np.hist()

# print(pd.Series(random_arr).values)
# print(pd.Series(random_arr).index)
# print(pd.Series(random_arr))
# print(pd.Series(random_arr,index=[f"index-{i}"for i in range(1,101)]))

# print()
# print(pd.Series(random_arr))
# print(pd.Series(random_arr)+2)
      
# e=np.array([2]*100)

# age = pd.Series([29,24,19,20],index=[4.6,"bob",5,"ghulam"])
# age = pd.Series([29,24,19,20],index=["alice","bob","kamran","ghulam"])
# print(age)
# print(age.values)
# print(age["alice"])



# print(pd.DataFrame({"name":["nkx","cds","dfs","svs"],"age":[1,2,3,4]}))

# print(pd.DataFrame([["aja","uhh","bjk","byu"],[1,2,3,4]],columns=["name","age"]))
# print(pd.DataFrame([["a",1],["b",2],["c",3],["d",4]],columns=["name","age","j","k"],index=[1,2,3,4]))
# print(pd.DataFrame([["a",1],["b",2],["c",3],["d",4]],columns=["name","age","j","k"],index=[1,2,3,4]))#with tupples
pd.read_csv("multi_index_practice.csv",sep=",",header=[0,1])
pd.read_csv("multi_index_practice.csv",sep=",",header=2)
pd.read_csv("multi_index_practice.csv",sep=",",header=1)
pd.read_csv("multi_index_practice.csv",sep=",",header=[0,1],index_col=["name"])
pd.read_csv("multi_index_practice.csv",sep=",",header=[0,1],index_col=["name","position",""])
pd.read_csv("multi_index_practice.csv",sep=",",header=[0,1],index_col=[0])
# df = pd.read_csv("multi_index_practice.csv",sep=",",header=[0,1],index_col=[0,2],usecols=[0,1,3])R
# df = pd.read_csv("D:\Github\multi_index_practice.csv",
#             sep=",",
#             header=1,
#             # dtype={"Name":int,"Position":int},
#             usecols=["Name","Position","Salary"],
#             # converters={"Name":lamda x:":"+x,"Salary":lamda x: x/1000000})
# )
# df.index
# df.dtypes
# pd.string
# #string==object

# df.head()#first five
# df.tail()#;ast five
# df.describe()
# df.value_counts()
# df.set_index("department").value_counts()
# df["department"].unique()
# type(df["department"])
# df.columns
# df.isnull().sum()
# df.notnull().sum()
# df.map
# df["Name".map(lambda x:x.replace(":",","))]