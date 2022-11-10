## Solutions for Chapter 3: Data Structures

# Exercise 7: Seeing the World
# Think of at least five places in the world you’d like to visit.

places = ["Matamata", "Bora Bora", "Bollenstreek", "Edinburgh", "Maldives"]

print("\n\033[1mRaw List:\033[0m")
print(places)

print("\n\033[1mAlphabetical Order -sorted():\033[0m") #using sorted()
print(sorted(places))

print("\n\033[1mOriginal Order:\033[0m")
print(places)

print("\n\033[1mReverse Alphabetical Order -sorted():\033[0m") #using sorted()
print(sorted(places, reverse=True))

print("\n\033[1mOriginal Order:\033[0m")
print(places)

print("\n\033[1mReverse Order:\033[0m") #using reverse()
places.reverse()
print(places)

print("\n\033[1mReverse Order (original):\033[0m") #using reverse()
places.reverse()
print(places)

print("\n\033[1mAlphabetical Order -sort():\033[0m")  #using sort()
places.sort()
print(places)

print("\n\033[1mReverse Alphabetical Order -sort():\033[0m")
places.sort(reverse=True)
print(places)
print()