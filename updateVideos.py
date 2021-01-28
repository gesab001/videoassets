import subprocess
import json
import os, glob
import readline

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

def gitpush(filename):
    subprocess.call("git pull", shell=True)
    subprocess.call("git add "+filename, shell=True)
    subprocess.call("git commit -m '" + "added + " + filename + "'")
    subprocess.call("git push --all")
        
def rlinput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   try:
      return input(prompt)  # or raw_input in Python 2
   finally:
      readline.set_startup_hook()

def trimVideo(filename):
    startH = input("start-hour: ")
    startM = input("start-minute: ")
    startS = input("start-second: ")
    start = startH + ":" + startM + ":" + startS + ".00"
    endH = input("end-hour: ")
    endM = input("end-minute: ")
    endS = input("end-second: ")
    end = endH + ":" + endM + ":" + endS + ".00"
    draft = "draft"+filename
    command = "ffmpeg -ss " + start -i filename -t end -c copy draft
    subprocess.call(command, shell=True)
    command = "ffplay -i " + draft
    subprocess.call(command, shell=True)
    isSave = input("save?")
    if (isSave=="y"):
        subprocess.call("rm " + draft, shell=True)
        gitpush(filename)
        
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
    isTrim = input("trim video? ")
    if(isTrim=="y"):
        trimVideo(filename)
    else:    
        gitpush(filename)
        

