age = 18 
hight = 1.65
numcom = 8j
print (type(age), age)
print (type(hight), hight)
print (type(numcom), numcom)

#Program 4
# Write a script that prompts the user to enter base and height 
# of the trianngle and calculate an area of this triangle
# (area = 0.5 x b x h). 
base = float(input ("Ingresa el valor de la base: "))
altura = float(input("Ingresa el valor de la altura: "))
area = print ("El area del triangulo es: ", base*altura/2)

#Ahora esto
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
#  Calculate the perimeter of the triangle (perimeter = a + b + c).
sideA = float (input("Ingresar el valor de sideA")) 
sideB = float (input("Ingresar el valor de sideB"))
sideC = float (input('Ingresar el valor de sideC'))
perimeter= print ("El valor del perimetro del triangulo es:", sideA + sideB + sideC )

#Get length and width of a rectangle using prompt.
#  Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
largo = float (input("ingresa el largo del rectangulo"))
ancho = float(input("ingresa el ancho del triangulo"))
Area = print("El area del triangulo es de:", largo * ancho)
perimeter = print("El perimetro del triangulo es de:",2 * (largo + ancho))

#Get radius of a circle using prompt.
#  Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
r = float (input("ingresa el valor del radio"))
Area = print("El area del circulo es de :", pi * r * r )
circunferencia = print("La circunferencia del circulo es de :", 2 * pi * r)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
pendiente = 2
interceptY = -2
interceptX = interceptY / pendiente
print("la pendiente de la recta es de :", pendiente)
print("La interseccion en el eje Y es:", interceptY)
print(" La interseccion en el eje X es:", interceptX)

#Slope is (m = y2-y1/x2-x1).
# Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math 
x1, y1  = (2,2) 
x2, y2 = (6,10)
slope = (y2 - y1) / (x2 - x1)
print("La pendiente (m) es:, " "slope")
distancia = (math.sqrt(x2 - x1) ** 2 + (y2-y1) ** 2)
print("la distancia euclinada es:""(slope)")