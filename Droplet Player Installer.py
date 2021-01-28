import os
import getpass
import time

os.system("title Install Droplet Player")
roaming = os.listdir(f"C:\Users\{getpass.getuser()}\%appdata%\Roaming")
if "Droplet Player" in roaming:
    print("You Seem to Have Droplet Player Already Installed, Would You Like to Re-download? (Y/N)")
    input()
    if "y" in input or "Y" in input:
        os.remove(f"C:\Users\{getpass.getuser()}\%appdata%\Roaming\Droplet Player")
        os.remove(f"C:\Users\{getpass.getuser()}\Desktop\Droplet Player\Droplet Player.ink")
#Installation
time.sleep(1)
os.system("cls")
print("Step 1/2: Install Data")
print("Creating Files..")
os.mkdir(f"C:\Users\{getpass.getuser()}\%appdata%\Roaming\Droplet Player")
open(f"C:\Users\{getpass.getuser()}\%appdata%\Roaming\Droplet Player\emulate.html", "w+")
open(f"C:\Users\{getpass.getuser()}\%appdata%\Roaming\Droplet Player\d.txt", "w+")
os.mkdir(f"C:\Users\{getpass.getuser()}\%appdata%\Roaming\Droplet Player\ffiles")
newmain = open(f"C:\Users\{getpass.getuser()}\%appdata%\Roaming\Droplet Player\Droplet Player.txt", "w+")

print("Downloading Executions..")
newmain.write("""
import os
import getpass

print(\"Opening Library..\")
#Library Setup
n = 0
n2 = 0
lines = []
code =[]
html = ""

files = os.listdir(f\"C:\Users\{getpass.getuser()}\%appdata%\Roaming\Droplet Player\ffiles\")
while not n == len(files)-1:
    n += 1
    print(f\"({n}){files[n]}\")
input()
def emulate():
    os.rename(f\"C:\Users\{getpass.getuser()}\%appdata%\Roaming\ffiles\{files[input]}\", f\"C:\Users\{getpass.getuser()}\%appdata%\Roaming\ffiles\{files[input]}.txt\")
    os.rename(f\"C:\Users\{getpass.getuser()}\%appdata%\Roaming\emulate.html\", f\"C:\Users\{getpass.getuser()}\%appdata%\Roaming\emulate.txt\")
    code = open(f"C:\Users\{getpass.getuser()}\%appdata%\Roaming\ffiles\{files[input]}.txt")
    html = open(\"emulate.txt\")
    for line in code.read():
        lines.append(line)
    n2 = 0
    dt = 0
    while not n2 == len(lines)-1:
        n2 += 1
#0 = null
#1 = Script
#10 = Tran. from Script
        #Read ActionScript

        if dt == 10:
            html.write(\"</script>\")

        if \"//\" in lines[n2]:
            html.write(f\"<!--{lines[n2]}-->\")

        if lines[n2] == \"/*\":
            n2 += 1
            while not lines[n2] == \"*\\":
                n += 1
                html.write(f\"<!--{lines[n2]}-->\")

        if lines[n2] == \"this.onButton_btn.onRelease = function(){\":
            if dt != 1:
                dt = 1
                html.write(\"<button>null</button>\")
                html.write(\\"<input id=\\"button\\" type=\\"submit\\" name=\\"button\\" onclick=\\"myFunction();\\" value=\\"enter\\"/>\")
                html.write(\"\"\"
                <script>
                function myFunction(){
                \"\"\")
            else:
                if lines[n2] == \"};\":
                    html.write(\"};\")
                    dt = 0

print(\"Preparing...\")
emulate()
os.rename(f"C:\Users\{getpass.getuser()}\%appdata%\Roaming\ffiles\{files[input]}.txt", f"C:\Users\{getpass.getuser()}\%appdata%\Roaming\ffiles\{files[input]}.txt"
print(\"Executing..\")
os.system(\"start C:\Users\%USERNAME%\Desktop\Droplet Player\imgs\Logo.png\")
os.system(\"start C:\Users\%USERNAME%\%appdata%\Droplet Player\emulate.html\")
""")
#Make Shortcut
print("Step 2/2: Create Shortcut")
shortcut = open("Droplet Player.txt", "w+")
shortcut.write(newmain.read())
os.rename(f"C:\Users\{getpass.getuser()}\Desktop\Droplet Player\Droplet Player.txt", f"C:\Users\{getpass.getuser()}\Desktop\Droplet Player\Droplet Player.ink")
os.rename(f"C:\Users\{getpass.getuser()}\Desktop\Droplet Player\Droplet Player.txt", f"C:\Users\{getpass.getuser()}\%appdata%\Roaming\Droplet Player\Droplet Player.py")
time.sleep(1)
print("You're All Done! Click on Droplet to Start Playing Flash Again!")
os.system("pause")
