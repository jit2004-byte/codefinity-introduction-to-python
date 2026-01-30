grocery_items = "milk cheese bread apples oranges chicken"
#Slicing method to extract Milk, Cheese and Bread
dairy1 = grocery_items[0:4]
dairy2 = grocery_items[5:11]
dairy3 = grocery_items[12:17]
#Print following message with aisle details
message1 = dairy1 + "," + dairy2 
aisle = 5
message = f"We have dairy and bakery items : {message1}, and {dairy3} in aisle {aisle}"
print(message)