import os
import pyfiglet
#Text in slant font
out = pyfiglet.figlet_format("Smart Cyber-Sec Kit", font="slant")
print(out)
ans=True
while ans:
    print("""
    1.Scan all the ports of the target
    2.Detect sql injection in a website 
    3.IP Lookup
    4.Detect Arp Spoofing
    5.Encrypt and Decrypt Files
    6.Detect Spam or Ham [HIT CTRL-C TO STOP THIS PROCESS OF RUNNING WEB SERVER]

    7.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
    	os.system('python3 Portscanner.py')
    elif ans=="2":
    	os.system("python3 sqli.py") 
    elif ans=="3":
        os.system("python3 Iplocator.py")
    elif ans=='4':
        os.system("sudo python3 Arpspoofdetector.py")
    elif ans== '5':
        os.system("python3 filencdec.py")
    elif ans == '6':
        os.system("streamlit run main.py")
    elif ans=="7":
      print("\n Goodbye") 
      ans = None
    else:
       print("\n Not Valid Choice Try again")
