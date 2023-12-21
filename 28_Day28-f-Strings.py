from ast import pattern


letter = "Hey my name is {1} and I am from {0}"
country = "Bangladesh"
name = "Ratul"

print(pattern.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")

# New : Python 3.6
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())

print(f"{2 * 30}")
print(type(f"{2 * 30}"))