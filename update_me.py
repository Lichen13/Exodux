#####################################################
#  COPYRIGHT (C) LICHEN 2024 | ALL RIGHTS RESERVED  #       
#####################################################

# >=> IMPORTS <=<
# Based on python, these packages do not required an additionnal installation.
import subprocess
import threading
import shutil
import time
import os

# >=> FILES VARIABLES <=<
folder1 = "updates"
file1 = "version.txt"
file2 = "https://raw.githubusercontent.com/Lichen13/Exodux/main/command/version.txt"
inside_file2 = subprocess.run(["curl", "-s", file2], stdout=subprocess.PIPE, text=True)
inside_file2 = inside_file2.stdout

file3 = "centroped.py"
file3_url = "https://raw.githubusercontent.com/Lichen13/Exodux/main/command/centroped.py"
inside_file3 = subprocess.run(["curl", "-s", file3_url], stdout=subprocess.PIPE, text=True)
inside_file3 = inside_file3.stdout

file4 = "update_me.py"
file4_url = "https://raw.githubusercontent.com/Lichen13/Exodux/main/command/update_me.py"
inside_file4 = subprocess.run(["curl", "-s", file4_url], stdout=subprocess.PIPE, text=True)
inside_file4 = inside_file4.stdout

# >=> SCRIPT <=<
def set_files_environment():
	try:
		os.makedirs(folder1)
		if os.path.exists(os.path.join(folder1, file1)):
			try:
				shutil.move(file1, folder1)
				return True

			except shutil.Error:
				print("┃")
				print("┗[✗]-Error : [ExoduxShutilError]: Error when using the module 'shutil'.\n")
				return
		
		else:
			with open(file1, "w") as file:
				file.write("Please update exodux to remove this message.")
				try: 
					shutil.move(file1, folder1)
					return True

				except shutil.Error:
					return True

	except FileExistsError:
		if os.path.exists(os.path.join(folder1, file1)):
			try:
				shutil.move(file1, folder1)
			
			except shutil.Error:
				return True
		
		else:
			with open(file1, "w") as file:
				file.write("Please update exodux to remove this message.")
				try:
					shutil.move(file1, folder1)
					return True
				
				except Exception as e:
					print("┃")
					print("┗[✗]-Error: [ExoduxShutilError]: Error when using the module 'shutil'.\n")
					return


def loading():
	while thread1.is_alive():
		characters = ["|", "/", "-", "\\"]
		for char in characters:
			print(f"┃[{char}]-Updating Exodux...", end="\r")
			time.sleep(0.07)
	print("┗[✓]-Exodux is now up-to-date!\n")
	return True


def update_system():
	with open(os.path.join(folder1, file1), "w") as file:
		file.write(inside_file2)
		time.sleep(2)
	with open(file3, "w") as file:
		file.write(inside_file3)
		time.sleep(2)
	with open(file4, "w") as file:
		file.write(inside_file4)
	return True


def main():
	global thread1
	if set_files_environment():
		thread1 = threading.Thread(target=update_system)
		thread2 = threading.Thread(target=loading)
		thread1.start()
		thread2.start()
		thread1.join()
	else:
		return
else:
	return

if __name__ == "__main__":
	main()
else:
	print("Error: [ExoduxImportError]")

# Error : ExoduxImportError
# Error : ExoduxShutilError
