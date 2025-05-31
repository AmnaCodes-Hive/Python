# # x='my name is amna\n'
# # def addstr(x):
# #     y= "I am a BBIT student"
# #     print(x+y)
# # addstr()


# x=23
# y=45
# c=x+y
# print(c)
# p=float(c)
# print(p)
# print(type(p))

# list=["apple","mango","banana"]
# tpl=tuple(list)
# print(tpl)
# print(type(tpl))


# n = int(input().strip())
# if num%2!=0:
#     print('Weird')
# elif num%2==0 and 2<=num<=5:
#     print("Not Weird")
# elif num%2==0 and 6<=num<=20:
#     print("Weird")
# elif num%2==0 and num>20:
#     print("Not Weird")

# a=input()
# b=input()
# print(int(a//b))
# print(float(a/b))



# def is_leap(year):
#     if (year%4==0 and year%100!=0) or (year%400==0):
#         return True
#     else:
#         return False
# year = int(input())
# print(is_leap(year))


# n = int(input())
# for i in range(1,n+1):
#     print(i,end="")

# n=int(input())
# scores=list(map(int, input().split()))
# unique_scores=list(set(scores))
# unique_scores.sort(reverse=True)
# max_score=unique_scores[0]
# runner_up_score=unique_scores[1]
# print("this is the max number:" ,max_score)
# print("this is the runner up score:" ,runner_up_score)



# n=int(input())
# students=[]
# for _ in range(n):
#     names=input()
#     score=float(input())
#     students.append([names,score])
# scores=sorted(set([student[1] for student in students]))
# if len(scores) < 2:
#     print("No second lowest score exists.")
# else:
#     second_lowest_score=scores[1]
#     second_lowest_students= [student[0] for student in students if student[1]==second_lowest_score]
#     second_lowest_students.sort()
#     for name in second_lowest_students:
#         print(name)


# num=int(input())
# if num>=90:
#     print('congratulation you got A+')
# elif num>=80:
#     print("You got A")
# else:
#     print("You achieve B")



# CGPA=float(input())
# IQ=int(input())
# if CGPA>=3.5 and IQ>=90:
#     print("You have high chance of getting job")
# elif  3.5<CGPA>=3.0 and 90<IQ>=80:
#     print("You have 50% of chances")
# else:
#     print("You are rejected")

# i=100
# while i>0:
#     i=i-1
#     print(i)

# for i in range (100,2,-3):
#     print(i)





# class Car:
#     def __init__(self,color,model,year):
#         self.color=color
#         self.year=year
#         self.model=model
        
#     def show_color(self):
#         print(f"This car is {self.color}") 

# car1 = Car("red",'100cc',2004)  
# car2 = Car("blue",'200cc',2007)  


# car1.show_color()  
# car2.show_color() 

# i=1000
# while i <=2000:
#     print(i)
#     i +=2

# class Animal:
#     def sound(self):
#         print("animal makes sound")
# class Dog(Animal):
#     def bark(self):
#         print("Dogs are barking ")
# dog=Dog()
# dog.sound()
# dog.bark()

# class Father:
#     def work(self):
#         print("Father is working")
# class Mother:
#     def house_work(self):
#         print("Mather is Housewife")
# class Child(Father,Mother):
#     def play(self):
#         print("child is playing")
# child=Child()
# child.work()
# child.house_work()
# child.play()

# class Grandfather:
#     def __init__(self,wisdom):
#         self.wisdom=wisdom
#     def wisdom(self):
#         print("he was wise")
# class Father(Grandfather):
#     def anger(self):
#         print("He was hot-tempered")
# class Child(Father, Grandfather):
#     def distinguishable(self):
#         print("child is not same to both of them")
# child=Child()
# child.wisdom()
# child.anger()
# child.distinguishable()

# class Car:
#     def __init__(self,brand,cost):
#         self.brand=brand
#         self.cost=cost
#     def show(self):
#         print(f"{self.brand} cost {self.cost} PKR")
    
# c1=Car("toyota", "200k")
# c2=Car("Hondaa", "800k")
# c1.show()
# c2.show()


# class Bankaccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     def get_balance(self):
#         print(f"My account balance is {self.__balance} PKR only.")
# B=Bankaccount(1000)
# B.get_balance()

# class Bird:
#     def sound(self):
#         print("Birds chirp")
# class Dog:
#     def sound(self):
#         print("Dogs Bark")
# def make_sound(animal):
#     animal.sound()
    
# sparrow=Bird()
# puppy=Dog()
# make_sound(sparrow)
# make_sound(puppy)

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass  # No implementation here (hidden details)

# class Car(Vehicle):
#     def start(self):
#         print("Car engine starts.")

# my_car = Car()
# my_car.start()

# n=int(input("enter"))
# for i in range(100,n-1,-2):
#     print(i)

# n=9
# for i in range (n):
#     for j in range (i,n):
#         print("$", end=" ")
#     print()   
    
# n=4
# for i in range (n):
#     for j in range (i,n):
#         print("$", end=" ")
#     print()  


     
# n=6
# for i in range (n):
#     for j in range (i,n):
#         print(" ", end="")
#     for j in range (i+1):
#         print("*", end=" ")  
#     for j in range(i,n-1):
#         print(" ", end=" ")
#     for j in range (i+1):
#         print("*", end=" ") 
          
#     print()       




# n=5
# for i in range (n):
#     for j in range (i+1):    
#         print(" ",end=" ")
#     for j in range (i,n):
#         print("^",end=" ")
#     print()
    
# n=10
# for i in range(0, n ,+1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()
    
# n=10
# for i in range (n):
#     for j in range(i,n):
#         print("^", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")

#     print()    
    


# n=50
# i=2
# # print(n)
# while i<=n:
#     print(i)
#     i+=2
    
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def average(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print("hi",self.name,"my avaerage score is", sum/len(self.marks))
         
# s1 = Student("Amna", [90,89,66])
# s1.average() 
# s1.name="maleeka"
# s1.average()   


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     @staticmethod    
#     def announcement():
#         print("Hello today is the result day!")
        
#     def average(self):
#         num=sum(self.marks)
#         avg=num/len(self.marks)        
#         print("hi",self.name,"my class average score is:", round(avg, 3))
    
         
# s1 = Student("Amna", [90,89,66])
# s1.announcement()   
# s1.average() 
# s1.name="maleeka"
# s1.average()  




# cost_price = float(input("Enter the cost price of the bike (in Rs): "))


# if cost_price < 50000:
#     tax_rate = 0.05
# elif 50000 <= cost_price <= 100000:
#     tax_rate = 0.10
# else:
#     tax_rate = 0.15

# tax_amount = cost_price * tax_rate

# print(f"The road tax to be paid is: Rs. {tax_amount:.2f}")


# class Solution:
#     def palindrome(self,num):
#         num_str = str(num) 
#         if num_str == num_str[::-1] :
#             return True
#         else:
#             return False
# solution = Solution()
# result = solution.palindrome("amma")
# print(result)


# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# num = is_prime(3)
# print(num)



# def i_function():
#     print("Hello i am a function")
# i_function()



# def Nme(username):
#     print("Welcome:", username)
# Nme("Aneeza")


# def Greater_one(a , b):
#     if a > b:
#         return a
#     elif b > a:
#         return b
#     else:
#         return ("Both are equal")
    
# num1 = int(input("enter number1 here"))
# num2 = int(input("enter number2 here")) 

# result = Greater_one(num1 , num2)
# print(result)


# def sum_num():
#     total=0
#     num = list(map(int, input("enter number here").split()))   
#     for i in num:
#         total+=i
#     return total
# def average(total , num):
#     avg = total/len(num)
#     return avg
# sum=sum_num()
# avgra=average(total , num)

# print("Sum:", sum)
# print("Average:", avgra)



# def sum_num():
#     num = list(map(int, input("Enter numbers here: ").split()))   
#     total = 0
#     for i in num:
#         total += i
#     return total, num

# def average(total, num):
#     avg = total / len(num)
#     return avg

# total, num = sum_num()
# avgra = average(total, num)

# print("Sum:", total)
# print("Average:", avgra)






# def convertCtoF(Celsius):
#     fahrenheit = (Celsius * 9/5) + 32
#     return(fahrenheit)
# C = convertCtoF(92)
# print(C)



# def evenOrOdd(num):
#     if num%2==0:
#         return "Its even"
#     else:
#         return "Its odd"
# EoO = evenOrOdd(2224)
# print(EoO)


# def checkNumber(num):
#     if num > 0:
#         return "Its positive"
#     elif num < 0:
#         return "Its negative"
#     else:
#         return "Its zero"
# nPZ = checkNumber(34)
# print(nPZ)


# num = int(input("Enter a number"))
# def Dividable(num):
#     if num%3==0 and num%5==0:
#         return "Yeah Its Divisible By Both"
#     else:
#         return "We're Sorry"
# D = Dividable(num)
# print(D)


# num1 = int(input("Enter a number"))
# num2 = int(input("Enter a number"))
# num3 = int(input("Enter a number"))
# def largestNum(num1,num2,num3):
#     if num1 >= num2 and num2 >= num3:
#             return "Num1 is the largest number"
#     if num2 >= num1 and num1 >= num3:
#             return "Num2 is the largest number"
#     else: 
#         return "Num3 is the largest"
    
# L = largestNum(num1,num2,num3)
# print(L)



# for i in range(1 , 11):
#     print(i)
            
            
             
# num = int(input("Enter a number"))
# for i in range(1, 11):
#     print(f" {i} x {num} == {i*num}")        
    


# n = int(input("Enter a number"))
# sum = 0
# for i in range(1 , n):
#     sum+=i
# print(sum)



# for i in range(1 , 50):
#     if i%2==0:
#         print(i)
        
        
# for i in range(2 , 50 , 2):
#         print(i) 


# for i in range(1, 6):
#     print("*" * i) 



# my_list = [5 , 6 , 4 , 7 , 3]  
# for i in my_list:
#     if i%2==0:
#         print("This are the even numbers from my_list:", i)


# my_list = [5 , 6 , 4 , 7 , 3]
# num1 = my_list[0] 
# num2 = my_list[0]  
# for i in my_list:
#     if i > num1:
#         num1 = i
# for i in my_list:
#     if i < num2:
#         num2 = i
# print(f"This is the largest number from my_list: {num1}, This is the smallest number: {num2}")
# print("This is the largest number from my_list:" , num1, "This is the smallest number:" , num2)




# my_list = [12 , 22 , 34 , 56 , 77 , 88]
# rev = my_list[::-1]
# print(rev)


# word = "huhahahuh"
# rev = word[::-1]
# if word == rev:
#     print("Yes its a palindrome")
# else:
#     print("No its a palindrome")


# word = "Amna You are great person"
# vowels = "AEIOUaeiou"
# for i in word:
#     if i in vowels:
#         print(i , end="  ")


sentence = "Hello this is meow"
word = sentence.split()
for i in word:
    print(i)


