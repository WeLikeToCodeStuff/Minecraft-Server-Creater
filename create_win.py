import os
os.system("cls")
print("Hello! Welcome to NeonDevelopment's Server creation script!")
print("Please enter one of the following server types to continue: ")
print("Vanilla, Spigot, CraftBukkit, Paper, BungeeCord, or FlameCord")
typerandom = input("Please enter a server type: ")
print("Example for server version: 1.16.4.\nFor BungeeCord & FlameCord, The latest version will be installed. This does not matter. ")
version = input("Please enter a server version: ")
serverram = input("Please enter an amount of ram for the server in GIGABYTES: ")
jartype = typerandom.lower()

# Code to curl the url and download the jar

#os.system("curl https://hostingfiles.gq/jars/" + jartype + "/release/" + jartype + "-" + version + ".jar")


os.system("clear")
if not os.path.exists('eula.txt'):
    print("Downloading jar...")
    if jartype == "spigot":
        os.system("curl https://hostingfiles.gq/jars/spigot/spigot-" + version + ".jar" + "--output " + jartype + version + ".jar")
    elif jartype == "paper":
        os.system("curl https://hostingfiles.gq/jars/papermc/papermc-" + version + ".jar" + "--output " + jartype + version + ".jar")
    elif jartype == "craftbukkit":
        os.system("curl https://hostingfiles.gq/jars/craftbukkit/craftbukkit-" + version + ".jar" + "--output " + jartype + version + ".jar") 
    elif jartype == "vanilla":
        os.system("curl https://hostingfiles.gq/jars/vanilla/release/vanilla-" + version + ".jar" + "--output " + jartype + version + ".jar")
    elif jartype == "bungeecord":
        os.system("curl https://hostingfiles.gq/jars/bungeecord/bungeecord-latest.jar --output bungeecord.jar")
    elif jartype == "flamecord":
        os.system("curl https://hostingfiles.gq/jars/flamecord/flamecord-latest.jar --output flamecord.jar")
    else:
        print("Jar not found.")
        exit()
    print("Accepting eula...")
    os.system("curl https://raw.githubusercontent.com/WeLikeToCodeStuff/Minecraft-Server-Creater/main/configs/eula.txt")
    #os.mknod('eula.txt')
    #f= open("eula.txt","a")
    #f.write("eula=true")
    print("Saving start.cmd")
    f= open("start.cmd","a")
    f.write("@echo off\n" + "java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar " + jartype + "-" + version + ".jar")
    print("Starting server...")
    os.system("java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar " + jartype + "-" + version + ".jar")
else:
    print("Server Starting...")
    os.system("java -Xmx" + serverram + "G" + " -Xms" + serverram + "G" + " -jar " + jartype + "-" + version + ".jar")
