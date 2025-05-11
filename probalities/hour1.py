# correlation coefficient 
#     strength
#     direction
#     -1 to +1 between them any continous values
        # +1 perfect positive correlation
        # -1 perfect inverse correlation
        #  0 no correlation
# np.corrcoef
# scipy.stats.pearsonr
import numpy as np
# x = np.array([1,2,3,4,5])
# x = np.array([-1,2,-3,4,5])
# y = np.array([10,20,30,40,50])
# y = np.array([10,20,30,40,50])[::-1]
# y = np.array([1,2,1,40,50])[::-1]
# y = np.array([1000,-2,1,0,50])[::-1]
# y = np.array([1000,-2,1,0,50])[::-1]
# print(np.corrcoef(x,y))#correlation matrix
# print("\n\n]n")
# x=np.linspace(-1,1,10)
# y=x**2
# print(np.corrcoef(x,y))#correlation matrix
# print("\n\n]n")

from scipy.stats import pearsonr
# x = np.linspace(-100,100,10)
# y = x** 2
# print( pearsonr(x,y))#shows p-value too
# if p<0.05 result is significant 
# p-value gives us the significance of the ___ if its less than 0.05 else insignificant
# 95% data is uneffected/ correct/ positive spuer strong correlation
# casuation
    # cause and effect
# correlation is not equal to casuation
# sensitive too outliers
# if dispersion is equal or less/

# experimental probability
# subjective probability

# sample space
    # all possible outcomes
# event
    # subset of outcomes
# complement
    # events not happening
    # P(E') =1-P(E)
# independent event
    # one events outcome does not effect outcome of other event
    # P(AnB) =P(A)xP(B)
    
# dependent events
# mutaully exclusive events
# two things that cant happen at once

# joint probability
# p(AnB)=p(A)*P(B)=.5*.5=.25#independent events
# p(AnB)=p(A)*P(B|A)=.5*.85=.25#dependent events

# p(MnAI)=P(M)*P(AI)

# conditional probability
# P(A|B) probbability of event A given that event B has occured
# b is birth a is death

# P(A|B) = P(AnB)/P(B)
    
random variable sampling any value based on distribution
mean average value
expected value == average value

x = np.random.int()
