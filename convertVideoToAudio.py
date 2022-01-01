import moviepy.editor as mp

video = mp.VideoFileClip('S:/ViolenceDetectionProject/RealLifeViolenceDataset/Violence/V_11.mp4')
#Add code to check if the video was without any audio (video.audio == None)
video.audio.write_audiofile('S:/ViolenceDetectionProject/RealLifeViolenceDataset/ViolenceAudio/A_11.mp3')