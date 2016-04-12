# import sys

# def sort_restaurant_ratings():
# # 1 open file

#     file_name = sys.argv[1]


# # 2 create a dictionary (Name:Rating) from file
#     restaurant_dict = {}
    
#     for line in open(file_name):
#         line = line.rstrip()
#         words = line.split(":") 
#         restaurant_dict[words[0]] = words[1]

# # 3 sort restaurant names alphabetically and print w/rating

#     # for key, value in sorted(restaurant_dict.items()):
#     #   print "{} has a rating of {}." .format(key, value)

# # 4 Prompt User for restaurant name and score(integer) - raw_input
#     restaurant_name = raw_input("Please enter restaurant name: ")
#     restaurant_rating = raw_input("Please enter the restaurant's rating: ")

# # 5 Store new restaurant/rating in the dictionary
#     restaurant_dict[restaurant_name.title()] = restaurant_rating
# # 6 Print all of the rating in alphabetical order
#     for key, value in sorted(restaurant_dict.items()):
#         print "{} has a rating of {}." .format(key, value)

# sort_restaurant_ratings()

import sys
import random

def sort_restaurant_ratings():

    file_name = sys.argv[1]

    restaurant_dict = {}
    
    for line in open(file_name):
        line = line.rstrip()
        words = line.split(":") 
        restaurant_dict[words[0]] = words[1]
    return restaurant_dict


def revise_restaurant_ratings():
    restaurant_dict = sort_restaurant_ratings()
    user_ratings = 0
    user_name = raw_input("Hello. Please enter your name: ")
    
    while user_ratings != "q":
    # Pull random data random.choice(restaurant_dict.keys())
    # Then tell the user what the randomly generated restaurant rating is
    # and ask them if they want to revise it
    # restaurant_name = raw_input("Please enter restaurant name: ")
    # restaurant_rating = raw_input("Please enter the restaurant's rating: ")

    # restaurant_dict[restaurant_name.title()] = restaurant_rating

    for key, value in sorted(restaurant_dict.items()):
        print "{} has a rating of {}." .format(key, value)

revise_restaurant_ratings()