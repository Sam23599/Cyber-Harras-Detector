import os

Y = '\033[33m' # yellow
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def title():
    os.system("clear")
    print(Y)
    print(" ____             _       _   ____                                       ")
    print("/ ___|  ___   ___(_) __ _| | / ___|  ___ _ __ __ _ _ __  _ __   ___ _ __ ")
    print("\___ \ / _ \ / __| |/ _` | | \___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__|")
    print(" ___) | (_) | (__| | (_| | |  ___) | (__| | | (_| | |_) | |_) |  __/ |   ")
    print("|____/ \___/ \___|_|\__,_|_| |____/ \___|_|  \__,_| .__/| .__/ \___|_|   ")
    print("                                                  |_|   |_|")

    print(Y+"Creators:\n")
    print("\t"+Y+"Satyam Singh Virat"+W+"<satym23599@gmail.com>")
    print("\t"+Y+"Sapna Rawat"+W+"<RawatSapna22@gmail.com>")
   
    print("_"*83)
    print("\n")
