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
                                   ==================Created By Farhan==============""")
 username = 'user'
password = 'pass'
 
def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)
 
def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")
		os.system('clear')
		print('')
 
		if pwd == password:
                        print ("\033[32;1m")
                        print("\033[1;32;40m You have log in successfully\n")
                        print ("\033[35;1m")
                        os.system("date")
                        print ("\033[36;1m_________________________________________\033[37;1m>")
                        print ("\033[36;1m| \033[34;1mAuthor   \033[35;1m: \033[32;1mMr. Ism1 ")
                        print ("\033[36;1m| \033[34;1mTEAM     \033[35;1m: \033[32;1mMUSLIM CYBER ARMY COMUNITI ")
                        print ("\033[36;1m| \033[34;1mContack  \033[35;1m: \033[32;1mFacebook \033[35;1m$\033[37;1mAkhy Abdillah Tampanz ")
                        print ("\033[36;1m| \033[34;1mE-Mail   \033[35;1m: \033[32;1moppocybera39@gmail.com ")
                        print ("\033[36;1m|________________________________________\033[37;1m>")
			print ("\033[31;1m[~]\033[33;1m============================================\033[31;1m[~]")
			print ("\033[33;1m<----------[ \033[36;1mWellcome To My Terminal \033[33;1m]----------->")
			print ("\033[31;1m[~]\033[33;1m============================================\033[31;1m[~]")
			sys.exit()
 
		else:
                        print ("\033[35;1m")
			print ("Password Yang Anda Masukkan Salah")
                        print ("\033[34;1mLogin Kembali")
                        time.sleep(2)
                        os.system('clear')
			restart()
 
	else:
                print ("\033[35;1m")
		print ("Username yang Anda Masukkan Salah")
                print ("\033[34;1mLogin Kembali")
                time.sleep(2)
                os.system('clear')
		restart()
 
try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
