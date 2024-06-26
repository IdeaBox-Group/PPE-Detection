from config import *

import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator


class Camera:
    def __init__(self,
                 video=0,
                 model=None):
        self.video = video
        self.model = model
        self.cap = cv2.VideoCapture(video)

    def annotate_image(self, image):
        annotator = Annotator(image,
                              font_size=1,
                              )
        results = self.model.predict(image)
        for r in results:
            if r.boxes:
                for box in r.boxes:
                    bbox = box.xyxy[0]
                    class_names = self.model.names[int(box.cls)]
                    annotator.box_label(bbox, class_names, color=(
                        0, 0, 255), txt_color=(255, 255, 255))

        image = annotator.result()
        return image

    def read_image(self,
                   image_path,
                   save_to=None,
                   show=True):
        image = cv2.imread(image_path)
        if self.model is not None:
            image = self.annotate_image(image)
        
        if not show:
            return image
        
        cv2.imshow(f"{image_path}", image)
        
        if save_to is not None:
            cv2.imwrite(self.save_to, image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def read_video(self,
                   save_to=None,
                   show=True):
        
        # totalFrames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)

        # if save_to is not None:
        #     frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #     frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        #     out_video = cv2.VideoWriter(save_to,
        #                                 cv2.VideoWriter_fourcc(*'mp4v'),
        #                                 20,
        #                                 (frame_width, frame_height))
        if not show: 
            _, frame = self.cap.read()     
            if self.model is not None : 
                frame = self.annotate_image(frame) 
            return frame 
        
        while True : 
            _, frame = self.cap.read()     
            if self.model is not None : 
                frame = self.annotate_image(frame)   
            
            cv2.imshow(f"{self.video}", frame)
            
            # if save_to is not None:
            #     out_video.write(frame)
                
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        
        # if save_to is not None:
        #     out_video.release()
            
        cv2.destroyAllWindows()
