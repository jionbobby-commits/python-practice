import requests
from moviepy import VideoFileClip, AudioFileClip
# 目标网站
video_url = ""
audio_url = ""

# 请求头
headers = {
    "User-Agent": "",
    "Referer": ""
}

# 发送GET请求
response1 = requests.get(video_url, headers=headers)
response2 = requests.get(audio_url, headers=headers)


# 创建一个文件对象，用于保存视频数据
with open("video.mp4", "wb") as f:
    f.write(response1.content)

# 创建一个文件对象，用于保存音频数据
with open("audio.mp3", "wb") as f:
    f.write(response2.content)

# 使用moviepy库为视频添加音频
video = VideoFileClip("video.mp4")
audio = AudioFileClip("audio.mp3")
video = video.with_audio(audio)
video.write_videofile("output.mp4")
