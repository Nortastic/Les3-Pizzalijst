#Opdracht 1: Maak een variabele met minimaal 5 toppings
from selectors import SelectSelector

Pizza_toppings = ['salami','ham','ananas','paprika','uitjes']

#Opdracht 2: Laat je pizza zien:
# Laat zien wat jouw eerste topping is
# Laat zien wat jouw derde topping is
# Laat zien wat jouw laatste opping is
# Laat al je toppings zien.

print(f"De eerste topping op mijn pizza is {Pizza_toppings[0]}")
print(f"De tweede topping op mijn pizza is {Pizza_toppings[2]}")
print(f"De laatste topping op mijn is {Pizza_toppings[4]}")
print (f"Alle toppings voor de pizza's bevat {Pizza_toppings}")

#Opdracht 3: Een extra topping
Pizza_toppings.append(input("Welke topping wil je erbij hebben?"))
print(Pizza_toppings)


#Opdracht 4: Een topping verwijderen

while True:
    topping = input("Welke topping wil je er niet bij hebben?")
    if topping in Pizza_toppings:
        Pizza_toppings.remove(topping)
        print("Deze topping is verwijderd van de lijst.")
        print(f"Hier is uw aangepaste pizzalijst {Pizza_toppings}")
        break

    else:
        print("Deze topping staast niet in de lijst, probeer het nog een keer.")