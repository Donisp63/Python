bottles = 99

while bottles != 0:
    if bottles > 2:
        print(str(bottles) + " bottles of beer on the wall\n" +str(bottles) + " bottles of beer\nTake one down, pass it around")

        bottles -= 1
        
        print(str(bottles) + " bottles of beer on the wall!\n")
        
    elif bottles == 2:
        print(str(bottles) + " bottles of beer on the wall\n" +str(bottles) + " bottles of beer\nTake one down, pass it around")

        bottles -= 1

        print(str(bottles) + " bottle of beer ont the wall!\n")
    
    elif bottles == 1:
        print(str(bottles) + " bottle of beer on the wall\n" + str(bottles) + " bottle of beer\ntake it down, pass it around")

        bottles -= 1
    
print("No bottles of beer on the wall!")    
    
