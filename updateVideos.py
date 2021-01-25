import subprocess
import json
import os, glob

files = os.listdir()
mp4s = [k for k in files if 'mp4' in k]

with open("../public/story/stories.json") as json_file:
    data = json.load(json_file)

for item in data["atoz"]:
    names = item["names"]
    for x in names:
        videoFilename = x["otherTitle"] + ".mp4"
        if (videoFilename in mp4s):
            print("yes")
        else:
            print("find this video " + videoFilename)
            url = input("url: ")
            filename = videoFilename
            command = "youtube-dl -f mp4 " + url + " --output " + filename
            subprocess.call(command, shell=True)
            command = "ffplay -i " + filename
            subprocess.call(command, shell=True)

