import os
import requests , builtwith
import sys
import time
from colorama import Fore , init
#CMS == To get the technologies used on the site
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
def _Littldier_():
    os.system('cls')
    print (baner)
    print (R + '[?]' + W + ' This tool is used to obtain system, management, content ' + R + '[?]\n')
    print (LC + '_ Enter your URL _\n')
    URL = str(input(ENTERIN + LR))
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

    Domin = 'https://' + URL
    Tek = builtwith.parse(Domin)
    for NamT in Tek:
        Snol  = str(Tek[NamT])
        NamT = NamT.replace('-' , ' ')
        Snol = Snol.replace("'" , ' ')    
        print (LY + '\t[*] ' + LB + NamT + LY + ' : ' + LB + Snol + LY + ' [*]\n')
    
    input (W + "[*] It's over. 'Enter' to return to menu [*]")               


_Littldier_()    