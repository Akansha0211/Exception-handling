n=int(input("Enter number of test cases you want to perform"))
for i in range(0,n):
      a,b=(input("enter").split(","))
      try:
          c=int(a)//int(b)
          print(c)
      except ZeroDivisionError as e:
          print("Error Code:",e)
      except ValueError as f:
          print("Error Code:",f)
