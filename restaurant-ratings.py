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

# 3 sort restaurant names alphabetically then call the associated values

	for key, value in sorted(restaurant_dict.items()):
# 4 print sorted dictionary (alphabetical order)
		print "{} has a rating of {}." .format(key, value)


sort_restaurant_ratings()