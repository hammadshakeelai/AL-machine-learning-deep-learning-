import numpy as np
# print(np.ones((4,4)))
# print(np.arange(0,50,10))#makes an array with value according to values
# print(np.random.randint(0,101,size=(3,3)))#make array cording to size with random values
########
# a=np.arange(1,11,1)
# print(a)
# a=np.insert(a,2,99)
# print(a)
# a=np.delete(a,2)
# print(a)
# a=np.sort(a)
# print(a)
# a=np.reshape(a,(2,5))
#seed forces a startpattern to random function
print(np.random.seed(100),np.random.randint(1,10,7))# start ,end excluded , number of values
# print(a)
#########
# a=np.random.randint(0,101,size=(2,3,4))
# print(a)
# # print(np.mean(a, axis=1))
# # print(a*3)
# a-=3
# print(a)
# print(a-(np.random.randint(0,101,size=(2,3,4))))
# print(np.transpose(a, (1, 0, 2)))
# print(np.sum(a, axis=0))