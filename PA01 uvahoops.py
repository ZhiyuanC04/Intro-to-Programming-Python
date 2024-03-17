a = input("What player would you like to calculate statistics for? ")
b = input("What team was the opponent in the game you would like to calculate statistics for? ")
c = input("How many 3's did " + a + " attempt this game? ")
d = input("How many 3's did " + a + " make this game? ")
e = input("How many 2's did " + a + " attempt this game? ")
f = input("How many 2's did " + a + " make this game? ")
g = input("How many free throws did " + a + " attempt this game? ")
h = input("How many free throws did " + a + " make this game? ")

c = int(c)
d = int(d)
e = int(e)
f = int(f)
g = int(g)
h = int(h)

i = (d + f)/(c + e)
i = i*100
j = h / g
j = j*100

k = 3 * d + 2 * f + h

print(a + " had a " + str(i) + "%" + " field goal percentage and a " + str(j) + "%" + " free throw percentage")
print(a + " scored " + str(k) + " points against " + b + "." + " Wahoowa!")
