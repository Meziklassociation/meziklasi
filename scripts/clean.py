import os
import shutil

os.chdir(os.path.dirname(os.path.realpath(__file__)))                                   
os.chdir("..")

file_remove = list()
dir_remove = list()

props_to_remove = [".un~", ".sass-cache", ".DS_Store"]

for root, dirs, files in os.walk(os.getcwd()):
	for file in files:
		for prop in props_to_remove:
			if file.endswith(prop):
				file_remove.append(os.path.join(root, file))

	for dir in dirs:
		for prop in props_to_remove:
			if dir.endswith(prop):
				dir_remove.append(os.path.join(root, dir))

if len(file_remove) > 0 and len(dir_remove) > 0:
	print("Are you sure you want to permanently remove these items? :")

	if len(file_remove) > 0:
		print("\tfiles:")
		for f in file_remove:
			print("\t\t" + f.replace(os.getcwd(), ""))

	if len(dir_remove) > 0:
		print("\tdirectories:")
		for d in dir_remove:
			print("\t\t" + d.replace(os.getcwd(), ""))

	print("\n[Y/N]")
	agreement = input()

	if agreement.lower() == "y":
		for file in file_remove:
			print("REMOVING FILE:\t\t" + file)
			os.remove(file)
		for dir in dir_remove:
			print("REMOVING DIRECTORY:\t" + dir)
			shutil.rmtree(dir)

os.chdir(os.path.dirname(os.path.realpath(__file__)))
