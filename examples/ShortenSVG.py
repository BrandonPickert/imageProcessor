import xmltodict
import json
import shutil

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
			delete_indices.append(i)
		# test 2, is width
		vector = []
		for i in vector:
			if i.isalpha():
				height.append(i)
			else:
				height.append(0)
		vector_alpha = []
		i = 0
		for c in height:
			try:
				if c.isalpha() == True:
					vector_alpha.append(i)
					# print("hi")
			except Exception:
				pass

			i += 1
		print(height)
		# print(vector_alpha)
		height
		for i in vector:
			if i == 'h':
				if i == 0:
					pass


		# import re
		# newstring = re.split('h', vector)
		# print(newstring)
		# if len(vector) > :
		# 	pass
		# else:
		# 	delete_indices.append(i)



delete_indices.reverse()

for i in delete_indices:
	del d['svg']['path'][i]

# print(d)
# print(json.dumps(d, indent=4))


with open('outputNew.svg', 'w') as file:
	file.write(json.dumps(d))






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