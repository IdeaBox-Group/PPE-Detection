from tools import Camera
from config import *

if __name__ == '__main__':
    
    MODEL = 'ALTERNATIVE' # 'CLIENT' OR 'ALTERNATIVE'
    VIDEO = 0 # 0 for camera, input videp path for video, for test input VIDEO_TEST_PATH
    
    camera = Camera(
        model=get_model(MODEL),
        video=0)
    camera.read_video()