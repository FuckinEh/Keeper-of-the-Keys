### THIS IS A HELPER CLASS. IT CREATES A JSON FILE FOR THE SPRITESHEET. 

### THIS IS DESIGNED TO WORK FROM THE GRAPHICS DIRECTORY



import os
import sys


filename = sys.path[0]
filename = os.path.join(filename, "letters_spritesheet.json")

file = open(filename, "w+")

file.write("{\"frames\" : {\n\n")

frame_size = 25

for i in range(36):
	if i < 26:
		letter = chr(97+i)
	else:
		letter = chr(48+i-26)

	for j in range(3):

		file.write(f"\"{letter}_{j}\" :\n" + "{\n")

		file.write(f"\t\"x\" : {j * frame_size},\n")
		file.write(f"\t\"y\" : {i * frame_size},\n")
		file.write(f"\t\"w\" : {frame_size},\n")
		file.write(f"\t\"h\" : {frame_size}\n")

		if i == 35 and j == 2:
			file.write("}\n")
		else:
			file.write("},\n")
		

	file.write("\n\n\n")

file.write("} }")

file.close
