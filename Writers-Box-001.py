#To begin you need a 0 in the file below
#open("numb.txt", "x")
file-num = int(open("numb.txt", "rt"))
print("Welcome to Writer's Box")
select1 = int(input("Would you like to create a new file(1), edit a prexisting file(2), or view a file(3)?"))

if select1 == 1:
    #Create file selection
elif select1 == 2:
    #edit file selection
elif select1 == 3:
    select2edit=int(input("This will overwrite file --- are you sure?"))
else:
    print("error try entering a value 1, 2 or 3")
