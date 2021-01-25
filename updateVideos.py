import subprocess
import json
import os, glob

files = os.listdir()
mp4s = [k for k in files if 'mp4' in k]

with open("../public/story/stories.json") as json_file:
    data = json.load(json_file)

count = 0
selection = []
for item in data["atoz"]:
    names = item["names"]
    for x in names:
        videoFilename = x["otherTitle"] + ".mp4"
        if (videoFilename not in mp4s):
           print(str(count) + ". " + videoFilename)
           selection.append(videoFilename)
           count = count + 1
        
while True:
    print("find this video " + videoFilename)
    filechoice = int(input("title number: "))
    filename = selection[filechoice]
    print("filename: " + filename)
    url = input("url: ")
    command = "youtube-dl -f mp4 " + url + " --output " + filename
    subprocess.call(command, shell=True)
    command = "ffplay -i " + filename
    subprocess.call(command, shell=True)
    subprocess.call("git pull", shell=True)
    subprocess.call("git add "+filename, shell=True)
    subprocess.call("git commit -m " + "added + " + filename)
    subprocess.call("git push --all")
        

