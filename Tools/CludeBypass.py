import os
import socket
import sys
import time
from colorama import init , Fore
#clude flare bypass == Obtain ip sections of the desired site 
init()
#--==--==--==--==--Variable--==--==--==--==-----------------------------------------------------------------------------------------------------------------------------------------------------------
R  = Fore.RED
LR = Fore.LIGHTRED_EX
G  = Fore.GREEN
LG = Fore.LIGHTGREEN_EX
W  = Fore.LIGHTWHITE_EX
Y  = Fore.YELLOW
LY = Fore.LIGHTYELLOW_EX
B  = Fore.BLUE
LB = Fore.LIGHTBLUE_EX
C  = Fore.CYAN
LC = Fore.LIGHTCYAN_EX
baner = (Fore.LIGHTYELLOW_EX + '\n\t██╗     ██╗████████╗████████╗██╗     ██████╗ ██╗███████╗██████╗\n'+'\t██║     ██║╚══██╔══╝╚══██╔══╝██║     ██╔══██╗██║██╔════╝██╔══██╗ ' + G + '   [!] '+ W +'Manufacturer : Arash GMH' + G + ' [!]\n' + LY +  '\t██║     ██║   ██║      ██║   ██║     ██║  ██║██║█████╗  ██████╔╝ ' + G + '   [!] ' + W +'Application type : Information'+ G + ' [!] \n' + LY +'\t██║     ██║   ██║      ██║   ██║     ██║  ██║██║██╔══╝  ██╔══██╗' + G + '    [!] ' + W + 'Language of construction : Python' + G +' [!]'+ LY + '\n' + '\t███████╗██║   ██║      ██║   ███████╗██████╔╝██║███████╗██║  ██║'+ G + '    [!] '+ W +'Version 1.8.2'+ G +' [!]\n'+LY+'\t╚══════╝╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝\n')
ENTERIN =(str( C + "┌─c " + R + "!" + LG + "Littldier" + R + "!" + W + "/" + LR + "Aim.election" + W + "/" + G + "@A" + LC + "5" + LC + "\n└──C\t:\t"))
#____________________________________Start____________________________________
def _Littldier_ ():
    os.system( "echo off" and "cls" )
    _sub_ = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql' , 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
    print ( baner )
    print ( R + '[?]' + W + ' In this section, you can find all the IP of the site or bypass Claude Fler in general ' + R + '[?]\n')
    print( LC + "_ Enter your URL _\n") 
    URL = input(ENTERIN + LR)
    if 'https://' in URL :
        print("http doesn't want to")
        time.sleep(2)
    elif URL == False :
        try:
            print( R + "[!]" +  LR + "You have not entered any addresses, re-enter." + R + "[!]")
            time.sleep(3)
            sys.exit
        except :
            return
    
    
    for  subdomin in _sub_ :
        try:
            IP_CFB = str(subdomin) + (".") + str(URL)
            _BE_ = socket.gethostbyname (IP_CFB)
            print ( R + "Original IP is : | " +  LB + (_BE_) + R + " | " + G + ">>>  " + R + "Address: | " + LB + (IP_CFB) + R + " | " +W+"\n")   
        except:
            pass
    
    input (W + "[*] It's over. 'Enter' to return to menu [*]")  
_Littldier_()