import sys

def sort_restaurant_ratings():
# 1 open file

    file_name = sys.argv[1]


# 2 create a dictionary (Name:Rating) from file
    restaurant_dict = {}
    
    for line in open(file_name):
        line = line.rstrip()
        words = line.split(":") 
        restaurant_dict[words[0]] = words[1]

# 3 sort restaurant names alphabetically and print w/rating

    # for key, value in sorted(restaurant_dict.items()):
    #   print "{} has a rating of {}." .format(key, value)

# 4 Prompt User for restaurant name and score(integer) - raw_input
    restaurant_name = raw_input("Please enter restaurant name: ")
    restaurant_rating = raw_input("Please enter the restaurant's rating: ")

# 5 Store new restaurant/rating in the dictionary
    restaurant_dict[restaurant_name.title()] = restaurant_rating
# 6 Print all of the rating in alphabetical order
    for key, value in sorted(restaurant_dict.items()):
        print "{} has a rating of {}." .format(key, value)

sort_restaurant_ratings()