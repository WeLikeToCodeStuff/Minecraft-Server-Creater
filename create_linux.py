import os
os.system("clear")
print("Hello! Welcome to NeonDevelopment's Server creation script!")
print("Please enter one of the following server types to continue: ")
print("Vanilla, Spigot, CraftBukkit, Paper, BungeeCord, or FlameCord")
typerandom = input("Please enter a server type: ")
print("Example for server version: 1.16.4.\nFor BungeeCord & FlameCord, The latest version will be installed. This does not matter. ")
version = input("Please enter a server version: ")
serverram = input("Please enter an amount of ram for the server in GIGABYTES: ")
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
    elif jartype == "bungeecord":
        os.system("wget https://hostingfiles.gq/jars/bungeecord/bungeecord-latest.jar")
    elif jartype == "flamecord":
        os.system("wget https://hostingfiles.gq/jars/flamecord/flamecord-latest.jar")
    else:
        print("Jar not found.")
        exit()
    print("Accepting eula...")
    os.system("wget https://raw.githubusercontent.com/WeLikeToCodeStuff/Minecraft-Server-Creater/main/configs/eula.txt")
    #os.mknod('eula.txt')
    #f= open("eula.txt","a")
    #f.write("eula=true")
    f= open("start.sh","a")
    f.write("#!/bin/bash\n" + "java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar " + jartype + "-" + version + ".jar")
    print("Starting server...")
    os.system("java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar " + jartype + "-" + version + ".jar")
else:
    print("Server Starting...")
    os.system("java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar " + jartype + "-" + version + ".jar")
