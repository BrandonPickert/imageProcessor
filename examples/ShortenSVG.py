import xmltodict
import json
import shutil
import re
import svgwrite

d = None

delete_indices = []

shutil.copyfile('output.svg', 'outputNew.svg')
with open('outputNew.svg', 'r+') as f:
	d = xmltodict.parse(f.read())
	for i in range(0,len(d['svg']['path'])):
		p = d['svg']['path'][i]

		# Tests for deletion
		vector = p['@d']
		# test 1, long paths can be ignored
		if len(vector) > 20:
			pass
		else:
			# pass
			# delete_indices.append(i)
		# test 2, is length > 1
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

new_json_image = json.dumps(d, indent=1)
# print(d)
print(json.dumps(d, indent=4))

json_data = json.loads(json.dumps(d, indent=1))
path_list = [path for path in json_data['svg']['path']]
# for path in path_list:
# 	print(path)

SVG_string = str('<svg version="1.1" viewBox="0 0 250 250" xmlns="http://www.w3.org/2000/svg">')
# print(SVG_string)
for path in path_list:
	for path1 in path:
		pass
		# print(path1)
	# SVG_string += "\n" + '<path d="' + path + "/>"

# print(SVG_string)


# path_strings = []
# for path in d['svg']['path']:
# 	path_strings.append(path)

# path_list = [path for path in d['svg']['path']]
# for path in path_list: print(path)
# for path in path_strings:
# 	print(path_strings)

# with open('outputNew.svg', 'w') as file:
# 	file.write(json.dumps(d))
# 	drawing = svgwrite.Drawing(filename='output.svg', size=(d['width'], d['height']))
# 	for shape in d['shapes']:
# 		if shape['type'] == 'rectangle':
# 			drawing.add(drawing.rect(insert=(shape['x'], shape['y']), size=(shape['width'], shape['height']), fill=shape['color']))
# 		elif shape['type'] == 'circle':
# 			drawing.add(drawing.circle(center=(shape['cx'], shape['cy']), r=shape['r'], fill=shape['color']))
# 		# Add more shape types as needed

# new_json_image.save('outputNewj.txt')
with open('d.json', 'w') as personal_data:
	json.dump(d, personal_data)






# import shutil
#
# shutil.copyfile('output.svg', 'outputNew.svg')
#
# with open('outputNew.svg', 'r') as svgR:
#     lines = svgR.readlines()
# with open('outputNew.svg', 'w') as svg:
#     for line in lines:
#         if line[0:5] == "<path" and line.find(' d="')>0:
#             d = line.find(' d="')
#             h = line.find('h', d)
#             v = line.find('v', d)
#             z = line.find('z') + 1
#             if h < v:
#                 vector_string = line[h:z]
#                 print(line[h:z])
#             else:
#                 vector_string = line[v:z]
#                 print(line[v:z])
#         else:
#             svg.write(line)