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




# 1.Write a program that takes your name and age as input and prints them.
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


# 2.Write a program that adds two numbers entered by the user.
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



# 3.Convert temperature from Celsius to Fahrenheit.
# Formula: F = (C × 9/5) + 32
# def convertCtoF(Celsius):
#     fahrenheit = (Celsius * 9/5) + 32
#     return(fahrenheit)
# C = convertCtoF(92)
# print(C)



# 4.Check whether a number is even or odd.
# def evenOrOdd(num):
#     if num%2==0:
#         return "Its even"
#     else:
#         return "Its odd"
# EoO = evenOrOdd(2224)
# print(EoO)



# 5.Write a program that checks whether a number is positive, negative, or zero.
# def checkNumber(num):
#     if num > 0:
#         return "Its positive"
#     elif num < 0:
#         return "Its negative"
#     else:
#         return "Its zero"
# nPZ = checkNumber(34)
# print(nPZ)



# 6.Take a number from the user and check if it's divisible by 3 and 5 both.
# num = int(input("Enter a number"))
# def Dividable(num):
#     if num%3==0 and num%5==0:
#         return "Yeah Its Divisible By Both"
#     else:
#         return "We're Sorry"
# D = Dividable(num)
# print(D)



# 7.Write a program to find the largest among three numbers.
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



# 8.Print numbers from 1 to 10 using a for loop.
# for i in range(1 , 11):
#     print(i)
            
            
            
# 9.Print the multiplication table of a number entered by the user.        
# num = int(input("Enter a number"))
# for i in range(1, 11):
#     print(f" {i} x {num} == {i*num}")        
    


# 10.Calculate the sum of all numbers from 1 to n.
# n = int(input("Enter a number"))
# sum = 0
# for i in range(1 , n):
#     sum+=i
# print(sum)



# 11.Print all even numbers between 1 and 50.
# for i in range(1 , 50):
#     if i%2==0:
#         print(i)
# or       
# for i in range(2 , 50 , 2):
#         print(i) 



# 12.Create a simple pattern:
# *
# **
# ***
# ****
# for i in range(1, 6):
#     print("*" * i) 



# 13.Store 5 numbers in a list and print only the even ones.
# my_list = [5 , 6 , 4 , 7 , 3]  
# for i in my_list:
#     if i%2==0:
#         print("This are the even numbers from my_list:", i)



# 14.Find the largest and smallest number in a list.
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



# 15.Reverse a list without using the built-in reverse function.
# my_list = [12 , 22 , 34 , 56 , 77 , 88]
# rev = my_list[::-1]
# print(rev)



# 16.Check whether a word is a palindrome (same forward and backward)
# word = "huhahahuh"
# rev = word[::-1]
# if word == rev:
#     print("Yes its a palindrome")
# else:
#     print("No its a palindrome")



# 17. Count the number of vowels in a string.
# word = "Amna You are great person"
# vowels = "AEIOUaeiou"
# for i in word:
#     if i in vowels:
#         print(i , end="  ")



# 18.Take a sentence and print each word on a new line.
# sentence = "Hello this is meow"
# word = sentence.split()
# for i in word:
#     print(i)



# 20.Write a function that returns the factorial of a number.
# def factorial(num):
#     factorial_num = 1
#     for i in range(1 , num+1):
#         factorial_num*=i
#         print(f"{i} x {num} = {factorial_num}")
#     return factorial_num , num
# Fac = factorial(5)
# print(Fac)
# or
# def factorial(num):
#     factorial_num = 1
#     steps = " "
#     for i in range(1 , num+1):
#         factorial_num *= i
#         steps += str(i)
#         if i != num:
#             steps += " * "
#         else:
#             steps += " = "
#     steps += str(factorial_num)
#     print(steps)
#     return factorial_num
# factorial(5)
     


# 20.Write a function to check if a number is prime.
# def prime_num(num):
#     if num <= 1:
#         return "Sorry"
#     for i in range(2 , num):
#         if num % i == 0:
#             return False
#     return True  
# Pm = prime_num(4)
# print(Pm)



# 21.Find the greatest common divisor (GCD) of two numbers.
# def gcd(a , b):
#     while b != 0:
#         a , b = b , a % b 
#     return a 
# a = int(input("Enter number for a here:"))
# b = int(input("Enter number for b here:"))

# print("the GCD for" , a, "and" , b, "is" , gcd(a , b))



# 22.Check if a number is a perfect square.
# def isPsQr(num):
#     if num < 0:
#         print("Negative number can't be perfect square" )
#         return False
#     for i in range(1 , num+1):
#         if i * i == num:
#             print(f"its a perfect square , {i} x {i} = {i*i}")
#             return True
#     print("its not a perfect square" )
#     return False
# isPsQr(16)


# 23.Generate Fibonacci series up to n terms.
# def fibonacci(num):
#     a , b = 0 , 1
#     for i in range(num):
#         print(a , end=", ")
#         a , b = b , a+b
# fibonacci(12) 


       


# def calculator():
#     print("Welcome to the simple calculator!")
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     choice = input("Enter choice (1/2/3/4): ")

#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter numeric values.")
#             return

#         if choice == '1':
#             print(f"The result is: {num1 + num2}")
#         elif choice == '2':
#             print(f"The result is: {num1 - num2}")
#         elif choice == '3':
#             print(f"The result is: {num1 * num2}")
#         elif choice == '4':
#             if num2 != 0:
#                 print(f"The result is: {num1 / num2}")
#             else:
#                 print("Error: Cannot divide by zero.")
#     else:
#         print("Invalid choice. Please select 1, 2, 3, or 4.")

# calculator()



# Create a calculator that can add, subtract, multiply, or divide two numbers.
# def calculator():
#     choice = str(input("Enter the operator (+,-,/,*)"))
#     if choice in ("+" , "-" , "/" , "*" ):
#         try:
#             num1 = int(input("Enter the number 1 here"))
#             num2 = int(input("Enter the number 2 here"))
#         except ValueError:
#             print("Invalid input. Please enter numeric values.")
#             return
#         if choice == "+":
#             print(f"the sum of both number is {num1 + num2}")
#         elif choice == "-":
#             print(f"the substract of both number is {num1 - num2}")
#         elif choice == "*":
#             print(f"the multiplication of both number is {num1 * num2}")  
#         elif choice == "/":
#             if num2 != 0:
#                 print(f"the division of both number is {num1 / num2}") 
#             else:
#                 print("Error: Cannot divide by zero.")
    
#     else:
#          print("Invalid Choice (+,-,/,*)")       
        
# calculator()



# 24.Write a program to check if a number is a prime number.
# num = int(input("Enter number here"))
# if num <= 1:
#     print("they are not prime numbers" , num)
# elif num == 2:
#     print("Its a prime number")
# else:
#     for i in range(3 , num+1):
#         if num % i == 0:
#          print(f"{num} is not a prime number") 
#          break
#     else:
#         print(f"{num} is not a prime number") 



# 25.Remove all duplicates from a list.
# num = input("Enter numbers separated by spaces: " )
# my_list = [int(x) for x in num.split()]
# num_list = []
# for i in my_list:
#     if i not in num_list:
#         num_list.append(i)
# num_list.sort()
# print("List without duplicates:", num_list)
# OR
# num = input("Enter numbers separated by spaces: " )
# my_list = [int(x) for x in num.split()]
# num_list = []
# for i in my_list:
#     if i not in num_list:
#         num_list.append(i)
# num_list.sort(reverse=True)
# print("List without duplicates:", num_list)



# 26. Count how many times each number appears in a list.
# num = input("Enter numbers separated by spaces: " )
# my_list = [int(x) for x in num.split()]
# num_list = {}
# for i in my_list:
#     if i in num_list:    
#         num_list[i] += 1
#     else:
#         num_list[i] = 1
# print(num_list)



# 27.Replace all spaces in a string with hyphens.
# num = input("Enter numbers: " )
# my_list = num.replace("","-")
# print(my_list)
# or
# num = input("Enter numbers: " )
# num_list = ""
# for i in num:
#     if i == " ":    
#         num_list += "-"
#     else:
#         num_list += i
# print(num_list)
# or

# num = input("Enter sentence: " )
# num_list = ""
# for char in num:
#     if char == " ":    
#         num_list += "-"
#     else:
#         num_list += char
# print(num_list)



# list1 = [1,3,5,6,7,8,9]
# list2 = [1,4,3,77,88,5,3,2]
# list12 = list1 + list2
# list12.sort()
# new_list = []
# for items in list12:
#     if items not in new_list:
#         new_list.append(items)
# print(list12)
# print("this the new list: " , new_list)



# tell = "blue" == "Blue"
# print(tell)

# number = 4
# if number * 4 < 15:
#  print(number / 4)
# elif number < 5:
#  print(number + 3)
# else:
#  print(number * 2 % 5)



# def greater_value(x, y):
#     if x > y:
#         return x
#     else:
#        return y


# print(greater_value(10,3*5))


# if ((10 >= 5*2) and (10 <= 5*2)):
#     print(True)
# else:
#     print(False)


# for x in range(1,11):
#   print(x**3)


input = "Four score and seven years ago"
# for c in input:
#   if c.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print(c)
# print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])
for c in range(len(input)):
  if c in ['a', 'e', 'i', 'o', 'u']:
    print(c)