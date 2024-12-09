a=input("Enter your numbers(please insert a space between two numbers):")
count=0
list=[]
b=a.split()
for c in b:
    if type(c)==str:
        list.append(int(c))
    else:
        print("Wrong Input")
for d in list:
    if d<0:
        count+=1
if count==0:
    e=sum(list)/len(list)
    print("The average of your input numbers is:",e)
else:
    print("Your input has",count,"negative numbers")
print("The largest number from your input is", max(list))