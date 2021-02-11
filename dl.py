import subprocess

url = input("url: ")
filename = input("filename: ")
command = "youtube-dl -f mp4 " + url + " --output " + filename
subprocess.call(command, shell=True) 
