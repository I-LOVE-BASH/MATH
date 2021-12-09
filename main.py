import  os
import time
os.system("clear && figlet MATH")
print("""
\033[1;96m1)\033[1;94m|x+a|=c\033[1;97m
\033[1;96m2)\033[1;94m|ax|=c\033[1;97m
\033[1;96m3)\033[1;94m|x/a|=c\033[1;97m
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
if r == "2" :
        y=input("A \033[1;92m==>\033[1;91m ")
        z=input("C \033[1;92m==>\033[1;91m ")
        a=int(y)
        c=int(z)
        print("\033[0;92m| \033[0;94mx *\033[0;94m",y,"\033[0;92m| =\033[0;94m",z)
        print("\033[0;92m( \033[0;94mx *\033[0;92m\033[0;94m",y,"\033[0;92m) =\033[0;94m",z,"or \033[0;92m-( \033[0;94mx *\033[0;94m",y,"\033[0;92m) =\033[0;94m",z)
        x=c/a
        x2=-c/a
        print("\033[0;94mX1 \033[0;92m=\033[0;91m",x)
        print("\033[0;94mX2 \033[0;92m=\033[0;91m",x2)
        if z < "0":
                os.system("clear")
                print("\033[1;93mC can't be negative")
                time.sleep(2)
                os.system("python main.py")
if r == "3":
        y=input("A \033[1;92m==>\033[1;91m ")
        z=input("C \033[1;92m==>\033[1;91m ")
        a=int(y)
        c=int(z)
        print("\033[0;92m| \033[0;94mx /\033[0;94m",y,"\033[0;92m| =\033[0;94m",z)
        print("\033[0;92m( \033[0;94mx /\033[0;92m\033[0;94m",y,"\033[0;92m) =\033[0;94m",z,"or \033[0;92m-( \033[0;94mx /\033[0;94m",y,"\033[0;92m) =\033[0;94m",z)
        x=c*a
        x2=-c*a
        print("\033[0;94mX1 \033[0;92m=\033[0;91m",x)
        print("\033[0;94mX2 \033[0;92m=\033[0;91m",x2)
        if z < "0":
                os.system("clear")
                print("\033[1;93mC can't be negative")
                time.sleep(2)
                os.system("python main.py")

