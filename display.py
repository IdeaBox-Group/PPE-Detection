import customtkinter as ctk
from PIL import Image
import cv2

from tools import Camera
from config import *

class Window():
    def __init__(self, model=None):
        self.main = ctk.CTk()
        self.main.title("App")
        self.main.geometry("1280x1080")
        
        self.__add_frame()
        
        self.camera = Camera(model=model, video=VIDEO_TEST_PATH)
    
    def __add_frame(self):
        self.frame_display = Frame(self.main, 'Frame')
        self.frame_display.place(relx=0, rely=0.4, x=0, anchor='w')
    
    def loop(self):
        frame = self.camera.read_video(show=False)
        self.frame_display.img_update(frame)
        self.main.after(1, self.loop)
    
    def run(self):
        self.loop()
        self.main.mainloop()

class Frame(ctk.CTkFrame):
    def __init__(self, container, text, side='left'):
        ctk.CTkFrame.__init__(self, container)
        self.setup(text=text, side=side)
        self.config_size = {
            'image_size': [640, 480],
            'current_size': [640, 480],
            'min_size': [100, 100],
        }
    
    def setup(self, text, side):
        self.out = ctk.CTkLabel(self, text=text, font= ("sans-serif", 15))
        self.out.pack(fill='both', expand=True, padx=5, pady=5)
        self.out.configure(anchor='center')
        self.img_label = ctk.CTkLabel(self, text="")
        self.img_label.pack(side=side, fill='both', expand=True, padx=5, pady=5)
    
    def img_update(self, img):
        img= _convert_to_pil(img, self.config_size['image_size'][0], self.config_size['image_size'][1])
        self.img_label.configure(image=img)
        self.img = img

def _convert_to_pil(img, length, width):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ctk.CTkImage(img, size=(length, width))
    return img
    
if __name__ == "__main__":
    window = Window(model=get_model())
    window.run()