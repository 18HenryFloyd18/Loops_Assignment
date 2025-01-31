numbersList = [1,1,2,3,5,8,13]#Print list of numbers
totalNumber = []#New list for the sum of all the variables
while numbersList:#While there is a numbers list list stay in the loop
    for each in numbersList: #For each number in the list add it to the others called x
        for x in numbersList:
            total = each + x#Add each number of the list to the other numbers of the list and then put them in a variable called total
            totalNumber.append(total)#Add the total number of the numbers added to the new list called totalNumber        
    break#Break out of the for loop
print("This is the list that we are using for the calculations of the numbers in the list:",numbersList)#Tell the user what the numbers we are getting are
print("Each number is a number from the list added to itself and the other numbers in the list")#Telling the user what the numbers mean
print(totalNumber)#Print all the numbers added
        

 
    