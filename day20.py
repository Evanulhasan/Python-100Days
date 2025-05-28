def calculateGmean(a,b):
    mean  = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    elif(a==b):
        print("Equal number")
    else:
        print("Second number is greater")
        
def isLesser(a,b):
    pass
    
a = 9 
b = 8 
isGreater(a,b)
calculateGmean(a,b)
print("\n")
c = 8
d = 74
isGreater(c,d)
calculateGmean(c,d)