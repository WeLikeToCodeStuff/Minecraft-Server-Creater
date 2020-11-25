import os
os.system("clear")
print("Hello! Welcome to NeonDevelopment's Server creation script!")
print("Please enter one of the following server types to continue: ")
print("Vanilla, Spigot, CraftBukkit, Paper")
typerandom = input("Please enter a server type: ")
print("Example for server version: 1.16.4")
version = input("Please enter a server version: ")
serverram = input("Please enter an amount of ram for the server in MEGABYTES: ")
jartype = typerandom.lower()

# Code to wget the url and download the jar

#os.system("wget https://hostingfiles.gq/jars/" + jartype + "/release/" + jartype + "-" + version + ".jar")


os.system("clear")
if not os.path.exists('eula.txt'):
    print("Downloading jar...")
    if jartype == "spigot":
        os.system("wget https://hostingfiles.gq/jars/spigot/spigot-" + version + ".jar")
    elif jartype == "paper":
        os.system("wget https://hostingfiles.gq/jars/papermc/papermc-" + version + ".jar")
    elif jartype == "craftbukkit":
        os.system("wget https://hostingfiles.gq/jars/craftbukkit/craftbukkit-" + version + ".jar")
    elif jartype == "vanilla":
        os.system("wget https://hostingfiles.gq/jars/vanilla/release/vanilla-" + version + ".jar")
    else:
        print("Jar not found.")
        exit()
    print("Accepting eula...")
    os.system("wget https://raw.githubusercontent.com/WeLikeToCodeStuff/Minecraft-Server-Creater/main/configs/eula.txt")
    #os.mknod('eula.txt')
    #f= open("eula.txt","a")
    #f.write("eula=true")
    print("Starting server...")
    os.system("java -Xmx" + serverram + "M" + "-Xms" + serverram + "M" + "-jar " + jartype + "-" + version + ".jar")
else:
    print("Server Starting...")
    os.system("java -Xmx" + serverram + "M" + "-Xms" + serverram + "M" + "-jar " + jartype + "-" + version + ".jar")
