userInput = int(input("enter the number : "))

number =0
mod = userInput % 2
if mod > 0:
    print("this is an odd")
    for number in range(userInput , 3 , 2):
        print(number)
        

else: 
    print("this is an even number")
        
