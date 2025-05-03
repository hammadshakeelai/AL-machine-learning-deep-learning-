import numpy as np
# arr = np.array([1,2,3])
# np.savez("fgfbf.npz",source=arr,target=arr*0.75)
# np.load("fgfbf.npz")
# np.savetxt("aaass.csv",arr,delimiter=',',header="column1,column2,column3")
# p=np.loadtxt("aaass.csv",dtype=str)
# p1=np.loadtxt("aaass.csv",dtype=str,skiprows=1,usecols=[0])
# p1=np.loadtxt("aaass.csv",delimiter=",")#specify the delimiter that you setted during loading
# print(p1)
#header column name
# np.load#--give function parameters
#npy is faster than csv
#as csv is openable in excel sheet
# ",".join[f"col{i}" for i in range(1,4)]
# .shape
# deamons
# pprocess withoit any link to anything
# parent process -> child
# kill 2583
# zombie process

# orphan
# process without its parent is a deamon
# !pwd # linux cammand
# !less main.py
# !head
# np.genfromtxt()#missing value
# np .gen fromtxt("aaass,csv",delimiter=',',dtype=None,encoding=None,skip_header=True,converters={0:lambda v:v*2},usecols=0,names=True)
# np.genfromtxt("aaass.csv",delimiter=',',names=True,dtype=None,encoding=None)#encoing for butes to string#nan = not a  number
# .astype("int16")
# ########
# print(np.array([[1],[2],[4]])**np.array([2,3,5]))
# output=np.empty((7,3),dtype='int8')
# np.add(a,b,out=output)
# print(output)
# #
# np.add(a,b,out=output,where=output==1)#add b to a where a value is 1
# np.power(np.array([11,2,3]),2)
# np.power([11,2,3],2)
# np.power((11,2,3),2)
# myarrayname.shape

# np.exp([2,3,4])
# np.expm1([2,3,5])
# np.maximum([1,3,4,5],[2,3,5,2])#give bigger value between 2 arrays
# np.minimum([1,3,4,5],[2,3,5,2])#give smaller value between 2 arrays
# np.fmax#to deal with Nan
# np.where
# np.floor([2.3,5.9,9.4])
# np.ceil([2.3,5.9,9.4])
# np.round([1.5,2.7,3.4,4.5])
# np.amin([[2,4,2,4],[5,3,8,6],[4,56,3,3]],axis=0)#column wise minimum
# np.amin([[2,4,2,4],[5,3,8,6],[4,56,3,3]],axis=1)#row wise minimum
