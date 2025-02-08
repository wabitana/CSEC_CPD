a=int(input("Enter A:"))
b=int(input("Enter B:"))

def yeartake(a,b):
    y=0
    while a<=b:
        a*=3
        b*=2
        y+=1
    print(y)
    
yeartake(a,b)      
      
   
