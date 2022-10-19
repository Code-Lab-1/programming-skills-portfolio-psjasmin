## Solutions for Chapter 7: Functions

# Exercise 5: Cities
# Write a function called describe_city() that accepts the name of a city and its country.

def describe_city(city_name, country="Philippines"):
    """Printing Cities"""
    print(f"""- {city_name} is in the {country}.""")

print(f"\n\033[1;32;40m╔══════════════════════════════════════════════════╗\033[0m")
describe_city("Makati")
describe_city("Ras Al Khaimah", "United Arab Emirates")
describe_city("Cebu City")
print("\033[1;32;40m╚══════════════════════════════════════════════════╝\n\033[0m")