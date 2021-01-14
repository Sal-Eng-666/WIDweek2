#create your own DFD, a subject of your own choice and convert it into code
def procedure_1(inp_menuoption):
    beer = 1
    cider = 2
    wine = 3
    non_alcoholic = 4

#choose a drink
print("Hello, what drink would you like?")
menuoption = int(input("Select an option 1 for beer, 2 for cider, 3 for wine or 4 for a non alcoholic drink"))
if menuoption ==1:
        print("Would you like a Lager, Ale or Stout?")
elif menuoption ==2:
        print("Dry , Sweet or Fruit based?")
elif menuoption ==3:
        print("Red, White, Rose or Sparkling?")
elif menuoption == 4:
        print("Tea, Coffee, or Soft Drink?")

def procedure_3(inp_menuoption):
    lager = 5
    ale = 6
    stout = 7
    dry = 8
    sweet = 9
    fruit = 10
menuoption2 = input("Will that be a pint or a half?")
if (menuoption2 == 5, 6, 7 ,8 ,9, 10):
    print("Will that be a pint or a half?")

