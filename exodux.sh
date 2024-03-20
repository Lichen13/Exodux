#####################################################
#  COPYRIGHT (C) LICHEN 2024 | ALL RIGHTS RESERVED  #       
#####################################################

first_run="run_once.flag"

if [ ! -f "$first_run" ]; then
	echo ""
	echo -e "\033[1m< Welcome to Exodux! >\033[0m"
	echo ""
	echo -e "\033[1mNOTE:\033[0m When using Exodux, this message will be displayed until the program is not fully installed. Also, if you want more information about Python3, please visit : 'https://www.python.org/'."
	echo ""
	echo -e "\033[1mMessage from Dev:\033[0m First of all, thank you very much for installing Exodux! We hope that it will help as many people as possible in many daily or more difficult tasks."
	echo ""
	echo -e "\033[1mREAD THIS:\033[0m Exodux required some installation from your terminal to work properly. We designed Exodux to be as independent as possible from other systems, but Exodux at least needs 'Python3' installed to work. You can check in the section called 'NOTE' for more informations about Python3."
	echo ""

	while true; do
		read -p "Install Exodux & required installation [Y/N] : " proceed
		
		if [ "$proceed" = "Y" ]; then
			sudo apt install python3
			result1=$? 

			if [ $result1 -eq 126 ]; then
				echo ""
				echo "ERROR : Error related to permissions for Exodux. Try doing this command before trying the installation again."
				echo -e "\033[1mchmod +x exodux.sh\033[0m"
				echo ""
				exit

			elif [ $result1 -eq 0 ]; then
				curl -sO "https://raw.githubusercontent.com/Lichen13/Exodux/main/command/update_me.py"
				result2=$?

				if [ $result2 -eq 0 ]; then
					curl -sO "https://raw.githubusercontent.com/Lichen13/Exodux/main/command/centroped.py"
					result3=$?

					if [ $result3 -eq 0 ]; then
						echo "done"
						touch $first_run
						exit
					
					elif [ $result3 -ne 0 ]; then
						echo "Error"
						exit
					fi

				elif [ $result1 -ne 0 ]; then
					echo "Error"
					exit 
				fi

			elif [ $result1 -ne 0 ]; then
				echo "Error"
				exit
			fi

		elif [ "$proceed" = "N" ]; then
			echo ""
			echo "Abort. Have a nice day."
			exit
		fi
	done
fi


while true; do
	read -p "┏[ Exodux ] > " command

	if [ $command = "help" ]; then
		echo "┃"
		echo "┃[ HELP COMMAND ]"
		echo "┃➜ help       :  Display this message."
		echo "┃➜ exit       :  Leave the program."
		echo "┃➜ update     :  Update Exodux."
		echo "┃➜ manual     :  Check manual for more help. NOT SET" 
		echo "┗➜ centroped  :  Install packages with Centroped. NOT SET"
		echo ""

	elif [ $command = "exit" ]; then
		echo "┃"
		echo "┗Exiting Exodux. Have a nice day."
		echo ""
		break

	elif [ $command = "update" ]; then
		echo "┃"
		echo "┃[ UPDATE COMMAND ]"
		echo "┃➜ update-info  :  Get more information about the updates."
		echo "┗➜ update-me    :  Update Exodux."
		echo ""

	elif [ $command = "update-info" ]; then
		output=$(curl -s "https://raw.githubusercontent.com/Lichen13/Exodux/main/update/update_information")
		echo -e "$output" | less -R
		echo "┃"
		echo "┗Showing information about updates."
		echo ""

	elif [ $command = "update-me" ]; then
		python3 update_me.py

	elif [ $command = "centroped" ]; then
		echo "┃"
		echo "┗Command is incomplete enter: 'centroped-help' for help."
		echo ""

	elif [ $command = "centroped-help" ]; then
		echo "┃"
		echo "┃[ CENTROPED HELP ]"
		echo "┃➜ centroped-install  :  Install a package with Centroped."
		echo "┃➜ centroped-upgrade  :  Update a specific package. / NOT SET"
		echo "┗➜ centroped-list     :  Display a list of your packages. / NOT SET"
		echo ""	

	elif [ $command = "centroped-install" ]; then
		python3 centroped.py

	else
		echo "┃"
		echo "┗[✗]-Command: '$command' not found."
		echo ""
	fi
done

