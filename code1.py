my_list=[1,2,2,4,4,5,6,8,10,13,22,35,52,83]
list=[]
for x in my_list:
     if(x >= 10):
        list.append(x)
print(list)
num1=int(input("enter the number:"))
list1=[i for i in my_list if i >= num1]
print(list1)
