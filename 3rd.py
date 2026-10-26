# python casting

# age = 23
# number=float(age) # to convert the integer value of age into float
# khan=str(age)
# print(number) # to print the float value of age
# print(khan) # to print the string value of age
# print(type(khan))

# string to integer conversion
# name = "23"
# price=100
# age = int(name)

# print(age*price) # to print the integer value of age
# print(type(age))

# print("5"*5) # its work like a loop and print 5 five times

# price = 250
# tax = 0.15
# total = float(price)+(price*tax) # to convert the integer value of price into float
# print(total)

# m="pakIStan"

# print(m.capitalize())

# word = "hello"
# letters = list(word)   # ['h', 'e', 'l', 'l', 'o']
# letters[1] = "E"       # change the letter at index 1
# word = "".join(letters)
# print(word)

# x="hellow"
# print(x[1:1])
# print(x[1:4]) # it will print the string from index 1 to 4
# print(x[1:]) # it will print the string from index 1 to end

# x=int(input("Enter a number: "))
# for i in range (1,3):
#     print(x,"x",i,"=",x*i)

# # concatenation 
# first_name = "John"
# last_name = "Doe"
# full_name = first_name + " " + last_name
# print(full_name)

# string modification 
message = "Hello, World!"
print(message.upper())  # Convert to uppercase
print(message.lower())  # Convert to lowercase

print(message.title())  # Convert to title case

print(message.replace("World", "Python"))  # Replace substring
print(message)


price = 125.687

print(f"Price: {price:.2f}")