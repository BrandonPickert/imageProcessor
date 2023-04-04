import xmltodict
import re

d = None
delete_indices = []

# shutil.copyfile('output.svg', 'outputNew.svg')
with open('output.svg', 'r+') as f:
	d = xmltodict.parse(f.read())
	for i in range(0,len(d['svg']['path'])):
		p = d['svg']['path'][i]

		# Tests for deletion
		vector = p['@d']
		# test 1, long paths can be ignored
		if len(vector) > 20:
			pass
		else:
			# Use regular expressions to find all the x and y values
			x_values = re.findall(r'h(-?\d+)', vector)
			y_values = re.findall(r'v(-?\d+)', vector)
				# Convert the strings too integers
			x_values = [int(x) for x in x_values]
			y_values = [int(y) for y in y_values]
			if sum(x_values) > 1 or sum(y_values) > 1:
				pass
			else:
				# pass
				delete_indices.append(i)

delete_indices.reverse()

for i in delete_indices:
	del d['svg']['path'][i]

path_dict = []
for path in d['svg']['path']:
	for i in path.values():
		path_dict.append(i)

svg_version = d['svg']['@version']
svg_viewBox = d['svg']['@viewBox']
svg_xmlns = d['svg']['@xmlns']
svg_string = f'<svg version="{svg_version}" viewBox="{svg_viewBox}" xmlns="{svg_xmlns}">\n'  # <path d="m32 64v-1h-1v1z" fill="#e8002e" fill-opacity=".043"/>
counter = 0
for i in path_dict:
	if counter == 0 or counter % 2 == 0:
		svg_string += f'<path d="{i}" fill="'
		counter += 1
	else:
		svg_string += f'{i}"/>\n'
		counter += 1

svg_string += "</svg>"
print(svg_string)
with open("cool.svg", 'w') as file:
	file.write(svg_string)
