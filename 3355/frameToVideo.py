import os
import cv2
from PIL import Image

# Checking the current directory path
print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated
os.chdir('C:/Users/jw969/Desktop/2019-2-OSSP1-3355-3-master/3355/성근')
path = 'C:/Users/jw969/Desktop/2019-2-OSSP1-3355-3-master/3355/성근'

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))
# print(num_of_images)

for file in os.listdir('.'):
    im = Image.open(os.path.join(path, file))
    width, height = im.size
    mean_width += width
    mean_height += height
    # im.show()   # uncomment this for displaying the image

# Finding the mean height and width of all images.
# This is required because the video frame needs
# to be set with same width and height. Otherwise
# images not equal to that width height will not get
# embedded into the video
mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

# print(mean_height)
# print(mean_width)

# Resizing of the images to give
# them same width and height
for file in os.listdir('.'):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
        # opening image using PIL Image
        im = Image.open(os.path.join(path, file))

        # im.size includes the height and width of image
        width, height = im.size
        print(width, height)

        # resizing
        imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
        imResize.save(file, 'JPEG', quality=95)  # setting quality
        # printing each resized image name
        print(im.filename.split('\\')[-1], " is resized")

    # Video Generating function


def generate_video():
    image_folder = '.'  # make sure to use your folder
    video_name = 'mygeneratedvideo.mp4'
    os.chdir("C:/Users/jw969/Desktop/2019-2-OSSP1-3355-3-master/3355/성근")

    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png")]

    # Array images should only consider
    # the image files ignoring others if any
    print(images)

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    # setting the frame width, height width
    # the width, height of first image
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 10, (width, height))

    # Appending the images to the video one by one
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

        # Deallocating memories taken for window creation
   # cv2.destroyAllWindows()
   # video.release()  # releasing the video generated

def play_video():
    capture = cv2.VideoCapture("C:/Users/jw969/Desktop/2019-2-OSSP1-3355-3-master/3355/성근/mygeneratedvideo.mp4")
    while True:
        if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
            capture.open("C:/Users/jw969/Desktop/2019-2-OSSP1-3355-3-master/3355/성근/mygeneratedvideo.mp4")

        ret, frame = capture.read()
        cv2.imshow("VideoFrame", frame)

        if cv2.waitKey(33) > 0: break

    capture.release()
    cv2.destroyAllWindows()

# Calling the generate_video function
generate_video()
play_video()





