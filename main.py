from tools import *
from config import *

if __name__ == '__main__':
    VIDEO_PATH = 'datasets\VIDEO CCTV\VIDEO CCTV\D01_20240605095005.mp4'
    IMAGE_PATH = 'datasets\\test_image.jpg'
    MODEL = get_model()
    
    read_video(0,
               model=MODEL
               )