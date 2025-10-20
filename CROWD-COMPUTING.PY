from statistics import mean,median
from scipy import stats
import matplotlib.pyplot as plt
Data = [1000,150,120,180,25,2,5,6,99,7,5,8,9,6,2,1,4,5,5,4,5,4,5,4,5,4,5,48,9,7,8,151,18,151,48]
Data.sort()
# td  = int(0.1 * len(Data))
# Data = Data[td:len(Data)-td]
# print("The trimmed Mean is :",mean(Data))




# Direct computation of trimmed mean
m = stats.trim_mean(Data,0.1)
print("The trimmed Mean is :",m) 
y = []
for i in range(len(Data)):
    y.append(5)
plt.plot(Data,y,'r--')
plt.plot(mean(Data),5,'g^',label='Mean')
plt.plot(median(Data),5,'bs',label='Median')

plt.show()