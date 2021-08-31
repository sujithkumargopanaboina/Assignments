a=[1,2,3,4,5,6,7,8,9,10,11,12,1342,43,12342,232342,342,123,213214,123]
eve=0
odd=0
for i in a:
    if(i==1):
        eve=eve+1
    elif(i%2==0):
        eve=eve+1
    else:
        odd=odd+1
print("number of even numbers:",eve)
print("number of odd numbers:",odd)