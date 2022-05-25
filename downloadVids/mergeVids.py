import os
from moviepy.editor import *

# Load clips
vid_path = '/home/davidvalorwork/projects/personal/downloadVids/vids'
files = os.listdir(vid_path)
clips = []

for file in files:
    clips.append(VideoFileClip(vid_path+'/'+file))

# Join + write
result_clip = concatenate_videoclips(clips)
result_clip.write_videofile('result.mp4')
