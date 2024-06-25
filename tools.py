from config import *

import cv2
from ultralytics import YOLO

def annotate_image(image, results):
    print(results)
    for result in results:
        if result.boxes:
            for i in range(len(result.boxes)):
                box = result.boxes[i]
                index = int(box.cls.item())
                tensor = box.xyxy[0]
                x1 = int(tensor[0].item())
                y1 = int(tensor[1].item())
                x2 = int(tensor[2].item())
                y2 = int(tensor[3].item())
                cv2.rectangle(image,(x1,y1),(x2,y2),COLOR[index],1)
    return image

def read_video(video_path,
               model=None):
    cap = cv2.VideoCapture(video_path)
    totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    
    # if myFrameNumber >= 0 & myFrameNumber <= totalFrames:
    #     # set frame position
    #     cap.set(cv2.CAP_PROP_POS_FRAMES,myFrameNumber)
    
    while True : 
        ret, frame = cap.read()     
        if model is not None : 
            results = model.predict(frame)
            frame = annotate_image(frame, results)
        cv2.imshow(f"{video_path}", frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    VIDEO_PATH = 'datasets\VIDEO CCTV\VIDEO CCTV\D01_20240605095005.mp4'
    MODEL = get_model()
    print('HAHA')
    read_video(VIDEO_PATH,
               model=MODEL
               )