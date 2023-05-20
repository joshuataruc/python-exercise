# def greet_someone():
#     name = input ('Please enter your name? ')
#     age = input('Please enter your age? ')
#     try:
#         int(age)
#     except ValueError:
#          print("Please enter a valid number")
#     print('Hi', name, 'from',  age)

# greet_someone()

# ------------------------------------------

# def calculate():
#     FirstNumber = input('Please enter the First number ')
#     SecondNumber = input('Please enter the Second number ')
#     equal = int(FirstNumber) + int(SecondNumber)
#     print(equal)
# calculate()

# ------------------------------------------

# def decisionMaking():
#     age = input('Please enter your age ')

#     if int(age) > int(18):
#         print("You're legal age")
#     elif int(age) == int(18):
#         print("comeback when you're 19")
#     else:
#         print("You're under age")
# decisionMaking()


# ------------------------------------------
# loops

# nums = [1,2,3,4]

# for num in nums:
#     print(num)

#The range() function can be used with the for loop to execute a block of code multiple times. The code below iterates between numbers 0 to 2 and prints each number.
# for i in range(5):
#     print(i)

#nested loop
# teams = [['Fred','John'],['Sean','Allen'],['Drel','Bagsic']]
# for team in teams:
#     for name in team:
#         print(name)

# Pass, Break, Continue
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

# for name in names:
#     if 'j' in name.lower():
#         pass
#     else:
#         print(name)
#-------------------
# for name in names:
#     if 'h' in name.lower():
#         break
#     else:
#         print(name)
#-------------------
# for name in names:
#     if 'a' in name.lower():
#         continue
#     else:
#         print(name)

#error Handling
# nums = ['x', 'y', 'z']
 
# try:
#    print(sum(nums))
 
# except:
#    print('Cannot print the sum! Your variables are not numbers.')
 
# finally:
#    print('Hope you got the result you want!')

def greet_someone():
    name = input ('Please enter your name? ')
    age = input('Please enter your age? ')
    try:
        int(age)
        print('Hi', name, 'from',  age)
    except:
         print("Please enter a valid number")
         exit()
        

greet_someone()