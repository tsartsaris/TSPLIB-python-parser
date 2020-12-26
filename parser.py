#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import re
import matplotlib.pyplot as plt

#  We use a regex here to clean characters and keep only numerics

cities_set = []
cities_tups = []
cities_dict = {}
#  we open the TSP file and put each line cleaned of spaces
#  and newline characters in a list 
def read_tsp_data(tsp_name):
	tsp_name = tsp_name
	with open(tsp_name) as f:
		content = f.read().splitlines()
		cleaned = [x.lstrip() for x in content if x != ""]
		return cleaned
"""
We return a list like 
['NAME: ulysses16.tsp',
'TYPE: TSP',
'COMMENT: Odyssey of Ulysses (Groetschel/Padberg)',
'DIMENSION: 16',
'EDGE_WEIGHT_TYPE: GEO',
'DISPLAY_DATA_TYPE: COORD_DISPLAY',
'NODE_COORD_SECTION',
'1 38.24 20.42',
'2 39.57 26.15',
'3 40.56 25.32',
................
'EOF']
"""

"""
Check for the line DIMENSION in the file and keeps the numeric value
"""
def detect_dimension(in_list):
	non_numeric = re.compile(r'[^\d]+')
	for element in in_list:
		if element.startswith("DIMENSION"):
			return non_numeric.sub("",element)

"""
Iterate through the list of line from the file
if the line starts with a numeric value within the 
range of the dimension , we keep the rest which are
the coordinates of each city
1 33.00 44.00 results to 33.00 44.00
"""
def get_cities(list,dimension):
	dimension = int(dimension)
	for item in list:
		for num in range(1, dimension + 1):
			if item.startswith(str(num)):
				index, space, rest = item.partition(' ')
				if rest not in cities_set:
					cities_set.append(rest)
	return cities_set


"""
Brake each coordinate 33.00 44.00 to a tuple ('33.00','44.00')
"""
def city_tup(list):
	for item in list:
		first_coord, space, second_coord = item.partition(' ')
		cities_tups.append((first_coord.strip(), second_coord.strip()))
	return cities_tups

"""
We zip for reference each city to a number
in order to work and solve the TSP we need a list 
of cities like 
[1,2,3,4,5,...........]
with the dictionary we will have a reference of the coordinates of each city 
to calculate the distance within (i + 1, i) or (2 - 1) were 2 and 1 represents each city
"""
def create_cities_dict(cities_tups):
	return zip((range(1,len(cities_tups)+1)),cities_tups)

"""
Just to plot the results
"""
def plot_cities(cities_tups):
	plt.clf()
	plt.scatter(*zip(*cities_tups))
	plt.plot(*zip(*cities_tups))
	plt.show()


"""
Putting it all together
"""
def produce_final(file="ulysses16.tsp"):
	data = read_tsp_data(file)
	dimension = detect_dimension(data)
	cities_set = get_cities(data,dimension)
	cities_tups = city_tup(cities_set)
	cities_dict = create_cities_dict(cities_tups)
	plot_cities(cities_tups)
	print (str(cities_dict))
	



if __name__ == '__main__':
	produce_final()
	# or produce_final("berlin52.tsp") or whatever filename you wish to have
	
