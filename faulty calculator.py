
#your program should take operator and the two numbers as input from the user and then return the result
#45*3=555 , 56+9=77 , 56/6=4
while True:
  n1=int(input("enter the 1st no.:"))
  n2=int(input("enter the 2nd no.:"))
  n3=input("enter the operation:+,*,/")
  if n3=='*':
    if n1==3  and n2 ==45 or n1==45 and n2==3:
       print("multiplication:",555)
    else:
       print("muliplication",n1*n2)
  if n3=='+':
    if n1==56 and n2==9 or n2==56 and n1==9:
       print("Addition:",77)
    else:
       print("Addition:",n1+n2)
  if n3=='/':
   if n1==56 and n2==6 or n1==6 and n2==56:
     print(4)
   else:
      print("Divison",n1/n2)




 


  
    




