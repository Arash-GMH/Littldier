import os
import requests
import sys
import time
from colorama import Fore , init
#Page Existence == Finds all sections on the site
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
#____________________________________start____________________________________
def _Littldier_():
    D_Page = ['robots.txt','search/','admin/','login/','sitemap.xml','sitemap2.xml','config.php','wp-login.php','log.txt','update.php','INSTALL.pgsql.txt','user/login/','INSTALL.txt','profiles/','scripts/','LICENSE.txt','CHANGELOG.txt','themes/','inculdes/','misc/','user/logout/','user/register/','cron.php','filter/tips/','comment/reply/','xmlrpc.php','modules/','install.php','MAINTAINERS.txt','user/password/','node/add/','INSTALL.sqlite.txt','UPGRADE.txt','INSTALL.mysql.txt']
    os.system("cls")
    print(baner + "\n\n")
    print (R + " [?] " + W + "With this tool, you can find the sections on a web page" + R + " [?]\n")
    print(LC + "_ Enter your URL _\n")
    URL = str(input(ENTERIN + LR))
    if 'http' in URL :
        print("http doesn't want to")
        time.sleep(2)
    elif URL == False :
        try:
            print( R + "[!]" +  LR + "You have not entered any addresses, re-enter." + R + "[!]")
            time.sleep(3)
            sys.exit
        except :
            return

    
    Domin = "https://"+URL+"/"
    for _Existence_ in D_Page :
        PageX = requests.get(Domin+_Existence_)
        Scode = str(PageX.status_code)
        if Scode[0] == '2':
            print(G + "[+] |" + LG + Domin+_Existence_ +G+ '| >>> ' + LG + _Existence_ + G + "| [+] \n")
        else:
            print(R + "[-] |" + LR + Domin+_Existence_ +R+ '| >>> ' + LR + _Existence_ + R + "| [-] \n")
    input (W + "[*] It's over. 'Enter' to return to menu [*]")
_Littldier_()    