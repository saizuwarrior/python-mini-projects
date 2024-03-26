from moviepy.editor import *

clip1 = VideoFileClip("WhatsApp Video 2024-03-26 at 11.29.03 AM.mp4").subclip(0,5)
clip2 = VideoFileClip("WhatsApp Video 2024-03-26 at 11.50.56 AM.mp4").subclip(0,5)

clip1 = clip1.set_fps(30)
clip2 = clip2.set_fps(30)

clip1 = clip1.resize((1920,1080))
clip2 = clip2.resize((1920,1080))

final_video = concatenate_videoclips([clip1, clip2])
final_video.write_videofile("new_video.mp4", codec='libx264', audio_codec='aac')