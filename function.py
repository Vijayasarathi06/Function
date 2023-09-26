##def myfunction():
##    print("Welcome to my shop sir")
##    sales=str(input("what you want sir"))
##    print("Take it sir")
##myfunction()
##Task 1
def myshop():
    shop={"Munch":10,"Milky bar":15,"five star":5}
    Man=str(input("Welcome sir,What you want:"))
    if Man in myshop():
        print("yes sir,This product available in this shop")
        a=int(input("How many chocolate you want sir"))
        b=a*(shop[Man])
        print("Take it sir,your amount is",b)
    else:
        print("sorry sir,This product not available")
myshop()
##Task 2
def mynumber():
    list1=[]
    num=int(input("enter the value"))
    for i in range(num):
        a=int(input("enter the value"))
        list1.append(a)
    print(list1)
mynumber()






##Task 3
def addition():
    list1=[]
    num=int(input("enter the value"))
    for i in range(num):
        a=int(input("enter the value"))
        list1.append(a)
    print(list1)
    sum=0
    for i in list1:
        sum+=i
    print(sum)
addition()
##Task 4
def secondvalues():
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    c=int(input("enter the value of c:"))
    if(a<b)and(a>c):
        print("a is largest number")
    elif(b<a)and(b>c):
        print("b is largest number")
    elif(c<a)and(c>b):
        print("c is largest number")
secondvalues()
##Task 5
def average():
    list1=[12,34,56,7,8]
    a=0
    for i in range(len(list1)):
        a+=list1[i]
        result=a/len(list1)
    print("the average number is",result)
average()




























