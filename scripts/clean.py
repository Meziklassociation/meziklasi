import os
import shutil

os.chdir(os.path.dirname(os.path.realpath(__file__)))                                   
os.chdir("..")

file_remove = list()
dir_remove = list()

for root, dirs, files in os.walk(os.getcwd()):
	for file in files:
		if file.endswith(".un~"):
			file_remove.append(os.path.join(root, file))

	for dir in dirs:
		if dir.endswith(".sass-cache") or dir.endswith(".DS_Store"):
			dir_remove.append(os.path.join(root, dir))

print("Are you sure you want to permanently remove these items? :")
print("\tfiles:")
for f in file_remove:
	print("\t\t" + f.replace(os.getcwd(), ""))

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
