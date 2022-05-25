import os
def wait():
    os.system("tput setaf 3")
    input("Press Enter to continue.....")
    os.system("tput sgr 0")

def design(symbol,sn,color):
    width = os.get_terminal_size().columns
    text = '{0}'.format(symbol)*sn
    os.system("tput setaf {}".format(color))
    print('{0}'.format(text).center(width))
    os.system("tput sgr 0")

def figlet(title,font,color):
    os.system("tput bold")
    os.system("tput setaf {}".format(color))
    os.system("figlet -w 200 -ck -f %s '%s'"%(font,title))
    os.system("tput sgr 0")
