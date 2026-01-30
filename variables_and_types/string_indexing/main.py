grocery_item = "Grilled Chicken Salad"
#Find length of the string, which includes space
length_of_item = len(grocery_item)
#Using positive index to get first,second & third character
first_char = grocery_item[0]
second_char = grocery_item[8]
third_char = grocery_item[16]
#Using negetive index to get last characters
last_char1 = grocery_item[-1]
last_char2 = grocery_item[-7]
last_char3 = grocery_item[-15]


# Testing
print("Length of item name:", length_of_item)
print("First character of each word:", first_char, second_char, third_char)
print("Last character of each word:", last_char1, last_char2, last_char3)