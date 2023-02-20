from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

os.system("cls")

beginMin = int(input("begin-minute = "))
beginSec = int(input("begin-second = "))

endMin = int(input("end-minute = "))
endSec = int(input("end-second = "))

begin = beginMin * 60 + beginSec
end = endMin * 60 + endSec

ffmpeg_extract_subclip("file.mp4", begin, end, targetname="result.mp4")