# Program to display the Fibonacci series upto nth term 

n = int(input())


n1, n2 = 0, 1
count = 0



if n <= 0:
   print("Please enter a natural number ")

elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)

else:
   print("Fibonacci series : ")
   while count < n:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
