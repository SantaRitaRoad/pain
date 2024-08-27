#user input at the very top 

userinput = input("Hi. My name is Rishyan. I draw flowers. What flower and how many would you like me to draw?").strip()

#use a list to split the user input into 2 elemts 

boingboing = userinput.split(" ")
i = 0
while i < len(boingboing):
    if boingboing[i].isdigit():
        print(i, boingboing[i])

    i += 1
#elemt one is the number 
#element two is the flower type 

# first we make mae a function to draw flower 
#this funciton will have 5 if and elif statements and will change the colors of the petals only base don the case 

# flower funciton has 3 parts 
#circle 
#stem
#pettles, these are the hardest which we keep till end 
