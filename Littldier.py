#menu bar tool
import os
import sys
import time
from colorama import init , Fore
#is started menu for tools
init()

#--==--==--==--==--Ithem nided--==--==--==--==--
try:

    try :

        import subprocess

    except:

        print('You need the prerequisites of the program. Wait a few moments to install ...\n')
        os.system('pip install subprocess')
        
    try :

        from colorama import init , Fore

    except :

        print('You need the prerequisites of the program. Wait a few moments to install ...\n')
        subprocess.check_output('pip install colorama')

    try :

        import requests

    except:

        print('You need the prerequisites of the program. Wait a few moments to install ...\n')
        subprocess.check_output('pip install requests')

    try :

        import builtwith

    except:

        print('You need the prerequisites of the program. Wait a few moments to install ...\n')
        subprocess.check_output('pip install builtwith')
    
    try :

        import socket

    except:

        print('You need the prerequisites of the program. Wait a few moments to install ...\n')
        subprocess.check_output('pip install socket')

except:

    print('[!] Check the network connection [!]')    

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
ENTERIN =(str( C + "┌─c " + R + "!" + LG + "Littldier" + R + "!" + W + "/" + LR + "Aim.election" + W + "/" + G + "@A" + LC + "]" + LC + "\n└──C\t:\t"))


#____________________________________menu____________________________________
def _start_():
    try :
        os.system ( "echo off" and "cls")
        print(baner)
        print (Fore.LIGHTGREEN_EX+" Hello"+Fore.RED+", "+Fore.LIGHTBLUE_EX+"welcome "+Fore.YELLOW+"to " + Fore.LIGHTGREEN_EX+"the "+Fore.LIGHTRED_EX+"app "+Fore.GREEN +"("+Fore.LIGHTYELLOW_EX+'Littldier'+ Fore.GREEN +")" "\n" )
        input(LR + '>') 
        time.sleep(0.4) 
        os.system ( "echo off" and "cls")
        print(baner)
        print(Fore.LIGHTWHITE_EX + "\tWhat do you want?\n")
        print(Fore.LIGHTGREEN_EX + "\t[1] Bypass cloude \n")
        print(Fore.LIGHTGREEN_EX + "\t[2] Page Existence\n")
        print(Fore.LIGHTGREEN_EX + "\t[3] CMS ( Content, Management, System )\n")
        select = str(input(ENTERIN))
        if select == '1' :
            from Tools.CludeBypass import _Littldier_
        elif select == '2' :
            from Tools.PageExistence import _Littldier_
        elif select == '3' :
            from Tools.CMS import _Littldier_    
        else:
            sys.exit
    except :
        time.sleep(0.3)
        W
        sys.exit            
_start_()    
