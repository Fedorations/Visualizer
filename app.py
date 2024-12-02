from pystyle import Write, Colorate, Colors, Center
import os as o
import sys as s
import subprocess

userName = Write.Input("Name [>] ", Colors.blue_to_purple, interval=0.01)
userPass = Write.Input("Pass [>] ", Colors.blue_to_purple, interval=0.01)
o.system("cls")


with open("login.txt", "a") as database_login:
    database_login.write(f"{userName}:{userPass}\n")

def login():
    userName = Write.Input("Login Name [>] ", Colors.blue_to_purple, interval=0.01)
    userPass = Write.Input("Login Pass [>] ", Colors.blue_to_purple, interval=0.01)
    with open("db/login.txt", "r") as database_login:
        credentials = dict(line.strip().split(":") for line in database_login)
    if userName in credentials and credentials[userName] == userPass:
        print(Colorate.Horizontal(Colors.green_to_white, "Login Successful, Bringing you to the main page", 1))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, "Login Failed!", 1))
        s.exit()
login()

parse_hwid = subprocess.check_output('wmic csproduct get uuid', shell=True).decode().splitlines()
main_hwid = [line.strip() for line in parse_hwid if line.strip() and "UUID" not in line][0]

pcName = o.getlogin()

def data():
    hwd = "HWID:" + main_hwid
    pc = "Name: " + pcName
    data1 = Center.XCenter(hwd)
    data2 = Center.XCenter(pc)
    print(data1)
    print(data2)
    input("Exit.. ")

data()
