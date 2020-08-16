j = r"""
 __  __
|  \/  | ___  ___  ___ _____      __
| |\/| |/ _ \/ __|/ __/ _ \ \ /\ / /
| |  | | (_) \__ \ (_| (_) \ V  V /
|_|  |_|\___/|___/\___\___/ \_/\_/
"""
print("\033[0;31m",j)
print("Tool by Moscow\n")

print("zhamra 99 banwsa bo darchon\n")
while True:
    a = str(input("tkaya Lyera commandea banwsa:  "))
    if (a=="ls"):
        print("\n\n{} ==> bo peshan dany filew folderkan\n\n".format(a))
        
    elif (a=="cd"):
        print("\n\n{} ==> bo chona naw folder\n\n".format(a))
        
    elif (a=="chmod 777"):
        print("\n\n{} ==> bo ezndan bo har filek\n\n".format(a))
    elif (a=="cd .."):
        print("\n\n{} ==> bo darchon la naw har folderyk\n\n".format(a))
        
    elif (a=="cd.."):
        print("\n\n{} ==> bo darchon la naw har folderyk\n\n".format(a))
        
    elif (a=="pkg install python"):
        print("\n\n{} ==> bo dabazandny pakge python yan har pakge tar batwya tanha python dasretwa bo nawi pakgeka\n\n".format(a))

    elif (a=="apt update"):
        print("\n\n{}bo ==> bo update krdny termux\n\n".format(a))
        
    elif (a=="apt upgrade"):
        print("\n\n{} ==> bo taza krdnwya hamw pakgekan\n\n".format(a))
    elif (a=="rm -rif"):
        print("\n\n{} ==> bo rash krdnwya har shtek batwya\n".format(a))
        print("rm -rif naw file yan folder\n")
        print("rm -rif moscow\n")
        print("rm -rif shell.py\n\n")
    elif(a=="python file.py"):
        print("\n\n{} ==> bo run krdny python\n".format(a))
        print("python naw fileka.py\n\n")
    elif (a=="nano"):
        print("\n\n{} ==> boa drost krdny yan edit krdny file\n".format(a))
        print("nano shell.py\n")
        print("nano moscow.php\n\n")
    elif (a=="touch"):
        print("\n\n{} ==> boa drost krdny file\n".format(a))
        print("touch moscow.py\n")
        print("touch shell.py\n\n")
    elif (a=="mkdir"):
        print("\n\n{} ==> boa drost krdny folder\n".format(a))
        print("mkdir naw folderka\n")
        print("mkdir moscow\n\n")
    elif (a=="id"):
        print("\n\n{} ==> bo awye bzanyn chan groupe terminal usere roote haya\n\n".format(a))
    elif (a=="whoami"):
        print("\n\n{} ==> bo awye bazanyn ema la chya userekyn\n\n".format(a))
    elif (a=="cp"):
        print("\n\n{} ==> boa copy krdny har filek yan folderyk\n".format(a))
        print("cp naw file yan folder")
        print("cp shell.py/sdcard\n\n")
    elif (a=="mv"):
        print("\n\n{} ==> bo naql krdny har filek yan folderyk\n".format(a))
        print("mv naw file yan folder\n")
        print("mv shell.py /sdcard\n\n")
    elif (a=="cat"):
        print("\n\n{} ==> boa peshan dany har nosenyke naw file\n".format(a))
        print("cat shell.py\n")
        print("cat moscow.txt\n\n")
    elif (a=="date"):
        print("\n\n{} ==> bo peshan dany katw barwar".format(a))
    elif (a=="clear"):
        print("\n\n{} ==> bo xawen kardnwya termux yan terminal\n\n".format(a))
    elif (a=="ifconfig"):
        print("\n\n{} ==> bo peshan dany ip xatakw mobilkwa\n\n".format(a))
    elif (a=="pwd"):
        print("\n\n{} ==> bo awye bzanyn la naw chy folderyken\n\n".format(a))  
    elif(a=="99"):
        break
    else:
        print("\naw commanda bony nya\n")
