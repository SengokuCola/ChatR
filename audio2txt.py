import json
import openai
from pydub import AudioSegment
import os

api_key = "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"
openai.api_key = api_key
count = 0
# 切割音频文件
def split():
    split_time = 800000
    count = 0
    audio = AudioSegment.from_file("media.mp3", format="mp3")
    file_name, file_ext = os.path.splitext("media.mp3")
    for i, chunk in enumerate(audio[::split_time]):
        # 生成新文件名
        new_file_name = f"{i+1}{file_ext}"
        # 保存分割后的文件
        chunk.export(new_file_name, format="mp3")
        count=count+1
        
# 调用whisper函数的转文字方法
def AudioToText(path):
    MODEL = "whisper-1"
    audio_file = open(path,"rb")
    transcript = openai.Audio.transcribe("whisper-1",audio_file)
    return transcript["text"]

#按照顺序转换
def trans():
    for i in range(count):
        print(i+1) 
        audio_path = f"{i+1}.mp3"
        au2txt = AudioToText(audio_path)
        with open("audio_to_txt.txt","a") as file:
                file.write(au2txt)
count = 2
# split()
trans()
# split()