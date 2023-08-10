# importing libraries
import os
import cv2
# from PIL import Image
import datetime

# Checking the current directory path
# from src.DBConnection import iud
import subprocess

print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated

path = r"E:\django\signlanguage\static\hand"

# Video Generating function

def generate_video(hi):

    fn=datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    fn1=fn+".mp4"

    fn=fn+".avi"
    video_name = r"E:\django\signlanguage\static\video/"+fn #'mygeneratedvideo.avi'
    # os.chdir("static")

    images = []
    for i in hi:
        if i==" ":
            images.append("0.jpg")
        else:
            images.append(i+".jpg")

    # Array images should only consider
    # the image files ignoring others if any
    print(images)
    print(os.path.join(path, images[0]),"========================")
    frame = cv2.imread(os.path.join(path, images[0]))

    # setting the frame width, height width
    # the width, height of first image
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(path, image)))


    # Deallocating memories taken for window creation



    cv2.destroyAllWindows()
    video.release()

    inputfile = video_name
    des=r"E:\django\signlanguage\static\video/"
    print('[INFO] 1', inputfile)
    outputfile = os.path.join(des, fn1)
    # subprocess.call([r'E:\django\signlanguage\sign\ffmpeg.exe', '-i', inputfile, outputfile])
    # subprocess.call([r'E:\django\signlanguage\sign\ffmpeg.exe', '-i', inputfile, outputfile])
    # os.system('E:\\django\\signlanguage\\sign\\ffmpeg.exe -i E:\\django\\signlanguage\\static\\video\\'+fn+' E:\\django\\signlanguage\\static\\video\\'+fn1 )
    # subprocess.call(['E:\\django\\signlanguage\\sign\\ffmpeg.exe', '-i', 'E:\\django\\signlanguage\\static\\video\\'+fn,'E:\\django\\signlanguage\\static\\video\\'+fn1] )
    input_file='E:\\django\\signlanguage\\static\\video\\'+fn
    output_file='E:\\django\\signlanguage\\static\\video\\'+fn1
    ffmpeg_cmd = ['E:\\django\\signlanguage\\sign\\ffmpeg.exe', '-i', input_file, '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', output_file]
    # subprocess.call(ffmpeg_cmd)
    print(fn1)
    from moviepy.editor import VideoFileClip

    def convert_avi_to_mp4(input_file, output_file):
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')

    # Usage example

    convert_avi_to_mp4(input_file, output_file)
    return fn1




# generate_video("hello how are you")