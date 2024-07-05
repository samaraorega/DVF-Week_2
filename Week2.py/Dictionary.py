#dict name = {"key" : "value"}

ice_cream_preferences = {"Mike":"Vanilla", "Rose":"Strawberry", "Denise":"Mocha"}

#Assigning attributes and exploring the edge cases

ice_cream_preferences["Rosa"] = "Biscotti"
print(ice_cream_preferences)
del ice_cream_preferences["Mike"]
print(ice_cream_preferences)

#help(dict)  Shows all of the methods available to dictionary objects

ice_cream_preferences["Prices"] = [450, 500, 230]
print(ice_cream_preferences)
print(ice_cream_preferences["Prices"][1])