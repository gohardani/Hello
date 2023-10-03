
li = [11, 11, 21, 31, 80]
print('Mean: ', sum(li) / len(li))

#------------------------------
ki = set(li)
print(ki)
#--------------------------------
print('max:', max(li))
print('min:', min(li))
#--------------------------------
string = 'My name is Mostafa'
print("".join(reversed(string)))
#---------------------------------

number = 87659
number_string = str(number)
print(type(number))
print(type(number_string))
#--------------------------------------
string = str(input('string: '))
print(string[::-1])
#--------------------------------------

my_string = str(input('Enter your string: '))
my_char = str(input('Enter your character: '))
print(my_string.count(my_char))
#-------------------------------------------------

my_string = str(input('Enter your string: '))
print(my_string.upper())
print(my_string.lower())
#---------------------------------------------------

my_string = str(input('Enter your string: '))
my_char = str(input('Enter your character: '))
print(my_string.find(my_char))
#---------------------------------------------------

txt = "welcome to my home"
x = txt.split()
print(x)