import  os
import time
import math
os.system("clear && figlet MATH")
# Regular Colors  
Black="\[\033[0;30m\]" # Black
Red="\[\033[0;31m\]" # Red
Green="\[\033[0;32m\]" # Green
Yellow="\[\033[0;33m\]" # Yellow
Blue="\[\033[0;34m\]" # Blue
Purple="\[\033[0;35m\]" # Purple
Cyan="\[\033[0;36m\]" # Cyan
White="\[\033[0;37m\]" # White
# High Intensty
IBlack="\[\033[0;90m\]" # Black
IRed="\[\033[0;91m\]" # Red
IGreen="\[\033[0;92m\]" # Green
IYellow="\[\033[0;93m\]" # Yellow
IBlue="\[\033[0;94m\]" # Blue
IPurple="\[\033[0;95m\]" # Purple
ICyan="\[\033[0;96m\]" # Cyan
IWhite="\[\033[0;97m\]" # White
# Bold High Intensty
BIBlack="\[\033[1;90m\]" # Black
BIRed="\[\033[1;91m\]" # Red
BIGreen="\[\033[1;92m\]" # Green
BIYellow="\[\033[1;93m\]" # Yellow
BIBlue="\[\033[1;94m\]" # Blue
BIPurple="\[\033[1;95m\]" # Purple
BICyan="\[\033[1;96m\]" # Cyan
BIWhite="\[\033[1;97m\]" # White
print("""
\033[1;96m1)\033[1;94m|x+a|=c\033[1;97m
\033[1;96m2)\033[1;94m|x*a|=c\033[1;97m
\033[1;96m3)\033[1;94m|x/a|=c\033[1;97m
\033[1;96m4)\033[1;94m|x-a|*|x+b|=c\033[1;97m
\033[1;96m5)\033[1;94m|x-a|/|x+b|=c\033[1;97m
\033[1;96m6)\033[1;94m|x+a|-|x-b|=c\033[1;97m
\033[1;96m7)\033[1;94m|x+a|+|x-b|=c\033[1;97m
\033[1;93mC can't be negative""")
r=input("\033[1;92m==>\033[1;91m ")
if r == "1" :
    y=input("A \033[1;92m==>\033[1;91m ")
    z=input("C \033[1;92m==>\033[1;91m ")
    a=int(y)
    c=int(z)
    if y < "0":
            print("\033[0;92m| \033[0;94mx\033[0;94m",y,"\033[0;92m| =\033[0;94m",z)
            print("\033[0;92m( \033[0;94mx\033[0;92m\033[0;94m",y,"\033[0;92m) =\033[0;94m",z,"or \033[0;92m-( \033[0;94mx\033[0;94m",y,"\033[0;92m) =\033[0;94m",z)
            a2=a-2*a
            x=c+a2
            x2=-c+a2
            print("\033[0;94mX1 \033[0;92m=\033[0;91m",x)
            print("\033[0;94mX2 \033[0;92m=\033[0;91m",x2)
    if y > "0":
            print("\033[0;92m| \033[0;94mx +\033[0;94m",y,"\033[0;92m| =\033[0;94m",z)
            print("\033[0;92m( \033[0;94mx +\033[0;92m\033[0;94m",y,"\033[0;92m) =\033[0;94m",z,"or \033[0;92m-( \033[0;94mx +\033[0;94m",y,"\033[0;92m) =\033[0;94m",z)
            x=c-a
            x2=-c-a
            print("\033[0;94mX1 \033[0;92m=\033[0;91m",x)
            print("\033[0;94mX2 \033[0;92m=\033[0;91m",x2)
    if z < "0":
            os.system("clear")
            print("\033[1;93mC can't be negative")
            time.sleep(2)
            os.system("python main.py")
else :
    print("programe not complet u can use : 1")
    os.system("python main.py")
