import os
import sys
import requests

os.system('clear')
if os.path.exists("plugins/"):
    os.system("cd plugins")
    print("Starting download...")
    link = "https://github.com/EssentialsX/Essentials/releases/download/2.18.2/EssentialsX-2.18.2.0.jar"
    file_name = "EssentialsX-2.18.2.0.jar"
    with open(file_name, "wb") as f:
    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')
    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
            sys.stdout.flush()
    link = "https://github.com/EssentialsX/Essentials/releases/download/2.18.2/EssentialsXAntiBuild-2.18.2.0.jar"
    file_name = "EssentialsXAntiBuild-2.18.2.0.jar"
    with open(file_name, "wb") as f:
    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')
    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
            sys.stdout.flush()
    link = "https://github.com/EssentialsX/Essentials/releases/download/2.18.2/EssentialsXChat-2.18.2.0.jar"
    file_name = "EssentialsXChat-2.18.2.0.jar"
    with open(file_name, "wb") as f:
    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')
    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
            sys.stdout.flush()       
    link = "https://github.com/EssentialsX/Essentials/releases/download/2.18.2/EssentialsXGeoIP-2.18.2.0.jar"
    file_name = "EssentialsXGeoIP-2.18.2.0.jar"
    with open(file_name, "wb") as f:
    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')
    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
            sys.stdout.flush()            
    link = "https://github.com/EssentialsX/Essentials/releases/download/2.18.2/EssentialsXProtect-2.18.2.0.jar"
    file_name = "EssentialsXProtect-2.18.2.0.jar"
    with open(file_name, "wb") as f:
    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')
    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
            sys.stdout.flush()
    link = "https://github.com/EssentialsX/Essentials/releases/download/2.18.2/EssentialsXSpawn-2.18.2.0.jar"
    file_name = "EssentialsXSpawn-2.18.2.0.jar"
    with open(file_name, "wb") as f:
    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')
    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
            sys.stdout.flush()          
    link = "https://github.com/EssentialsX/Essentials/releases/download/2.18.2/EssentialsXXMPPd-2.18.2.0.jar"
    file_name = "EssentialsXXMPP-2.18.2.0.jar"
    with open(file_name, "wb") as f:
    print("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')
    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )
            sys.stdout.flush()            
