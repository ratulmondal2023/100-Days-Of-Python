# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia")      #add item
# temp.pop(3)                #remove item
# temp[2] = "Finland"
# countries = tuple(temp)
# print(countries)


# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
res = tuple1.index(3, 4, 8)
print('Count of 3 in Tuple is:', res)