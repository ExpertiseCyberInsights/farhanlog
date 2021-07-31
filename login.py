#python
import os
os.system("clear")
 
print("\033[1;32;40m CyberClan The IT society of SGNDKC\n")
print("\033[1;33;40m This tool halping you to get new hint for your new question\n")
 
print("""\033[1;32;40m                                                                               _____

 $$$$$$\            $$\                            $$$$$$\  $$\                     
$$  __$$\           $$ |                          $$  __$$\ $$ |                    
$$ /  \__|$$\   $$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$ /  \__|$$ | $$$$$$\  $$$$$$$\  
$$ |      $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$ |      $$ | \____$$\ $$  __$$\ 
$$ |      $$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|$$ |      $$ | $$$$$$$ |$$ |  $$ |
$$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|$$ |      $$ |  $$\ $$ |$$  __$$ |$$ |  $$ |
\$$$$$$  |\$$$$$$$ |$$$$$$$  |\$$$$$$$\ $$ |      \$$$$$$  |$$ |\$$$$$$$ |$$ |  $$ |
 \______/  \____$$ |\_______/  \_______|\__|       \______/ \__| \_______|\__|  \__|
          $$\   $$ |                                                                
          \$$$$$$  |                                                                
           \______/                                                                 
                                 ========created By Farhan==============""")
correctpass = "farhan"

while True:
    
    a = input("Eneter the password: --> ")
    if a == correctpass:
        print("You have logged into secret account")
        ex = input("to exit press 'e' to continue press 'y'")
        if ex  == 'e':
            break
        else:
            continue
    else:
        print("The password is wrong try again")


