# Variables in Python

first_name = 'Sandra'
last_name = 'Torres'
country = 'Mexico'
city = 'Aguascalientes'
age = 18
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Sandra', 
    'lastname':'Torres', 
    'country':'Mexico',
    'city':'Aguascalientes'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Sandra', 'Torres', 'Mexico', 19, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

##Area del circulo 

radio= int(input("Ingrese radio del circulo: "))
print (type(radio))
pi = 3.14159 
areaOfCircle = pi * radio ** 2 
circumOfCircle = 2 * pi * radio 
print ("The area of the circule is", areaOfCircle )
print ("The circumference of the circle is", circumOfCircle) 

name= input("Primer nombre") 
lastname= input("Primer apellido")
country= input("Pais de origen")
age=input("Tu edad")
print("Tu nombre es: " + name + " " + lastname)
print("eres de : "+ country )
print("Tu edad es:" + age ) 
