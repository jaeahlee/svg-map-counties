import csv
import pdb
from bs4 import BeautifulSoup

# Read in unemployment rates

unemployment = {}
min_value = 100; max_value = 0
reader = csv.reader(open('unemployment09.csv'), delimiter=",")
for row in reader:
	try:
		full_fips = row[1] + row[2]
		rate = float( row[8].strip() )
		unemployment[full_fips] = rate
		
	except:
		pass

# Load the SVG map

svg = open('counties.svg', 'r').read()

# Load into Beautiful Soup

soup = BeautifulSoup(svg)

# Find counties

paths = soup.findAll('path')

# Map colors

colors = ["#eeeeee", "#d4b9da", "#c994c7", "#df65b0", "#dd1c77", "#980043"]

# County style

path_style = 'font-size:12px;fill-rule:nonzero;stroke:#ffffff;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'

# Color the counties based on unemployment rate

for p in paths:
	
	if p['id'] not in ["State_Lines", "separator"]:
		
		# pass
		
		try:
			rate = unemployment[p['id']]
		
		except:
			continue
			
		if rate > 10:
			color_class = 5
		
		elif rate > 8:
			color_class = 4
			
		elif rate > 6:
			color_class = 3
		
		elif rate > 4:
			color_class = 2
			
		elif rate > 2:
			color_class = 1
		
		else:
			color_class = 0
			
		
		color = colors[color_class]
		p['style'] = path_style + color
			
# Output map

print soup.prettify()
		

		
		
		
		
		
		
		
		
		
		 