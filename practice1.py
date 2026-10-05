print("####  CALCULATOR  ####")
i1 = int(input("Select one of the items below to find the area of"))
print("1/2/3/4")
print(".................")
print("1.CIRCLE")
print(".................")
print("2.RECTANGLE")
print(".................")
print("3.SQUARE")
print(".................")
print("TRIANGLE")
print(".................")

if "1" in i1:
    r = int(input("entre the radius of the circle"))
    area = 3.14 * r * r 
    print(f"are if the circle is {area} ")


