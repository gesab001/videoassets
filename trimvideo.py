import subprocess

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
    command = "ffmpeg -ss " + start + " -i " +  filename + " -t "+end+" -c copy " +  draft
    subprocess.call(command, shell=True)
    command = "ffplay -i " + draft
    subprocess.call(command, shell=True)


filename = input("filename: ")
trimVideo(filename)
