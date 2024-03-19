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
folder1 = "packages"
file1 = "https://raw.githubusercontent.com/Lichen13/Exodux/main/centroped/centroped_packages/test"
inside_file1 = subprocess.run(["curl", "-s", file1], stdout=subprocess.PIPE)
inside_file1_output = str(inside_file1.stdout)

# >=> PACKAGE DICTIONNARY <=<
packages = {
	"test": "https://raw.githubusercontent.com/Lichen13/Exodux/main/version.txt"
}


# >=> SCRIPT <=<
def set_files_environment():
	if os.path.exists(folder1):
		return True
	
	else:
		os.makedirs(folder1)
		return True


def package_to_install():
	global input1
	print("┃")
	print("┃[ CENTROPED ]")
	print("┃Enter a valid name for the package that will be installed.")
	input1 = input("┃Name of package : ")		
	
	if input1 in packages:
		print(f"┃[!]-Package : {input1} found.")
		input2 = input("┃Proceed? [Y/N] : ")

		if input2 == "Y":
			print("┃")
			return True
		
		else:
			print("┃")
			print("┗[✓]-Abort.\n")
			return 
	
	else:
		print("┃")
		print(f"┗[✗]-Error: [ExoduxPackageNotFoundError]: Package '{input1}' doesn't exists.\n")
		return 


def verify_package():
	if not os.path.exists(os.path.join(folder1, input1)):
		return True
	
	else:
		print("┃")
		print("┗[✗]-Error: [ExoduxPackageFoundError]: The package you are trying to install already exists.\n")
		return


def loading():
	while thread1.is_alive():
		characters = [" [-[-[-[:}", "< -[-[-[:}", "<[ [-[-[:}", "<[- -[-[:}", "<[-[- -[:}", "<[-[-[ [:}", "<[-[-[- :}", "<[-[-[-[ }", "<[-[-[-[: ", "<[-[-[-[:}"]
		for char in characters:
			print(f"┃ {char} ➜  Centroped is working. Please wait.", end="\r")
			time.sleep(0.1)
	print(f"┗[✓] <[-[-[-[:}} ➜  Package : {input1} is now INSTALLED.\n")


def install_package():
	with open(input1, "w") as file:
		file.write(inside_file1_output)
		try:
			shutil.move(input1, folder1)
			time.sleep(3)
			return True
		
		except shutil.Error:
			print("┃")
			print("┗[✗]-Error: [ExoduxShutilError]: Error when using module 'shutil'.\n")
			return


def main():
	global thread1
	if set_files_environment():
		if package_to_install():
			if verify_package():
				thread1 = threading.Thread(target=install_package)
				thread2 = threading.Thread(target=loading)

				thread1.start()
				thread2.start()
				thread1.join()
						

if __name__ == "__main__":
	main()

else:
	print("Error: [ExoduxImportError]")

# Error : ExoduxShutilError
# Error : ExoduxPackageFoundError
# Error : ExoduxPackageNotFoundError
# Error : ExoduxImportError
