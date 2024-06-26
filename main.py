from tools import Camera
from config import *

if __name__ == '__main__':
    
    MODEL = get_model()
    
    camera = Camera(
        model=MODEL,
        video=VIDEO_TEST_PATH)
    camera.read_video()