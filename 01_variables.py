my_string_variable = 'Helloooo'
my_integer_variable = 5
my_boolean_variable = True

print(my_string_variable)
print(type(my_string_variable))

print(my_integer_variable)
print(type(my_integer_variable))

print(my_boolean_variable)
print(type(my_boolean_variable))

print(len(my_string_variable))

# 1. Declara y asigna valores a las siguientes variables:
# â€¢	name: una cadena que contenga tu nombre.
# â€¢	age: un nÃºmero entero que represente tu edad.
# â€¢	height: un nÃºmero flotante que represente tu altura.
# â€¢	Imprime cada variable en una lÃ­nea separada.
name = "Jason"
age = 34
height = 176.0

print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.
age = str(age)
print(type(age))

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segÃºn corresponda e imprÃ­mela.
is_student = True
print(is_student)

# 4. Usa la funciÃ³n len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable.
name_len = len(name)

# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
name, lastname, city = ("Jason", "Sepulveda", "Santiago")
print(name)
print(lastname)
print(city)

# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.
color = input("what is your favorite color?: ")
print(color)

# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

fruit = "Banana"
print(fruit)
fruit = "Apple"
print(fruit)

# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.

price = 99.50
print(type(price))
price = int(price)
print(price)
print(type(price))


# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address = "Street 2, 09799, FL"
address_len = len(address)
print(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().

phone: int = 56988598741
phone = 12352568964
print(phone)
print(type(phone))
