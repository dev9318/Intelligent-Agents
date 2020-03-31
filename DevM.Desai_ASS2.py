from random import seed
from random import randint
import matplotlib.pyplot as plt 

# seed random number generator
seed(1)

a=[0]
no_of_1=[1]   #y axis variable
n=0

for i in range(999):
    a.append(0)

#my random 1
a[201]=1

while(1):
   #the magic basically adding 1s
   for i in range(1000):
        if(a[i]==1):
            if(randint(0,1)==0):
                a[i-1]=1
            else:
                a[(i+1)%1000]=1
   #swapping
   x=randint(0,999)
   y=randint(0,999)
   a[x]=a[y]+a[x]
   a[y]=a[x]-a[y]
   a[x]=a[x]-a[y]
   n=n+1
   #caz lists go out of range
   no_of_1.append(0)
   #counting 1s
   for i in range(1000):
       if(a[i]==1):
            no_of_1[n]=no_of_1[n] + 1
   if((int)(no_of_1[n])==1000):
      break


x1=[1]  #x axis variable
for i in range(n):
    x1.append(i+2)

print(no_of_1)
print(x1)
#plotting
plt.plot(x1,no_of_1)
plt.xlabel('no of repetitions')
plt.ylabel('no of 1s')
plt.show()
