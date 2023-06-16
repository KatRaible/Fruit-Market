print("Welcome to the GC Fruit Market!")

name = input("Hello, what is your name?  ")

apple = int(2)
grape = int(1)
orange = int(3)

fruits = ["1. apple for $2", "2. grape for $1", "3. orange for $3"]

print("Welcome " + name + ". Which fruit would you like to buy?  ")

for f in fruits:
    print(f)
#print(fruits[0]) #apple
#print(fruits[1]) #grapes
#print(fruits[2]) #orange

new_subtotal = 0
apple_subtotal = 0
grape_subtotal = 0
orange_subtotal = 0

purchase = input(">  ")

if purchase == "1":
    print("You bought an apple at $", apple)
    new_subtotal += apple
    apple_subtotal += 1
elif purchase == "2":
    print("You bought grapes for $", grape)
    new_subtotal += grape
    grape_subtotal += 1
elif purchase == "3":
    print("You bought an orange at $", orange)
    new_subtotal += orange
    orange_subtotal += 1
    # there is likely a better/more efficient way to write this

answer = input("Would you like to buy another piece of fruit? y/n  ")

## and then ask the loop again

## establish a boolean here for y/n?
##y = True
##n = False
## i don't think I have to be this literal about *establishing* a boolean
#loops and conditionals operate ON a boolean expression


while answer == "y":
    print("Welcome " + name + ". Which fruit would you like to buy?  ")
    print(fruits[0]) #apple
    print(fruits[1]) #grapes
    print(fruits[2]) #orange
    purchase = input(">  ")
    if purchase == "1":
        print("You bought an apple at $", apple)
        new_subtotal += apple
        apple_subtotal += 1
    elif purchase == "2":
        print("You bought grapes for $", grape)
        new_subtotal += grape
        grape_subtotal += 1
    elif purchase == "3":
        print("You bought an orange at $", orange)
        new_subtotal += orange
        orange_subtotal += 1
    answer = input("Would you like to buy another piece of fruit? y/n  ")
else:
    print("Order for",name)


print(apple_subtotal, "apple(s) at $2 apiece")
print(grape_subtotal, "grapes(s) at $1 apiece")
print(orange_subtotal, "orange(s) at $3 apiece")

subtotal = int(new_subtotal)
print("Sub Total:  $", subtotal)

tax = float(subtotal * .05)
print("5% tax: $", tax)

Total = subtotal + tax
print("Total: $",Total)




##Welcome name. Which fruit would you like to buy?
##create a continuous loop
##Would you like to buy another piece of fruit? y/n
##A receipt will read Order for Name
##Declare quantity of fruit, including price
##Subtotal followed by 5% tax
##Final total including tax
## "You bought one apple at $2
## "You bought one order of grapes at $1
## "You bought one orange at $3
## apple(s) for $2 apiece
## grape(s) for $1 apiece
## orange(s) for $3 apiece
## Subtotal
## 5% tax
## Total: