import customtkinter as ctk
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_ALL, DND_FILES
from PIL import Image
import cv2

from tools import Camera
from config import *

class Window():
    def __init__(self, model=None, video=VIDEO_TEST_PATH):
        self.main = ctk.CTk(TkinterDnD.DnDWrapper)
        
        self.main.title("App")
        self.main.geometry("1280x1080")
        
        self.display_frame = self.__add_frame('Display Frame')
        self.mode_cb = self.__add_cb('Video',  0, 0.71)
        self.mode_entry = self.__add_entry(width=400, relx=0.2, rely=0.71, inputmode=True)
        
        self.camera = Camera(model=model, video=video)
        self.prev_video = video
        
    def __add_frame(self, text):
        frame = Frame(self.main, text)
        frame.place(relx=0, rely=0.35, x=0, anchor='w')
        return frame
    
    def __add_cb(self, text, relx, rely):
        cb = CheckBox(self.main, text, relx, rely)
        return cb
    
    def __add_entry(self, width, relx, rely, inputmode):
        entry = Entry(self.main, width=width, relx=relx, rely=rely, inputmode=inputmode)
        return entry

    def loop(self):
        frame = self.camera.read_video(show=False)
        self.display_frame.img_update(frame)
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

class Entry(ctk.CTkEntry):
    def __init__(self, container, width, relx, rely, inputmode=False) :
        ctk.CTkFrame.__init__(self, width=width)
        self.place(relx, rely)

        if inputmode:
            
            def drop(event):
                # do operations with event.data file
                container.file_path = event.data[1:-1]
                self.configure(placeholder_text=event.data)
                
            self.drop_target_register(DND_ALL)
            self.dnd_bind("<<Drop>>", drop)

class CheckBox(ctk.CTkCheckBox):
    def __init__(self, container, text, relx, rely, variable=None):
        ctk.CTkCheckBox.__init__(self, 
                                 container, 
                                 text=text, 
                                 variable=tk.StringVar(container, 'on'), 
                                 command=self.callback
                                 )
        
        self.place(relx=relx, rely=rely)
        # self.setup(text, relx, rely)
    
    def setup(self, text, relx, rely):
        self.out = ctk.CTkLabel(self, text=text, font= ("sans-serif", 15))
        self.out.place(relx=relx, rely=rely)
    
    def callback(self):
        print("checkbox toggled, current value:", self._variable.get())

def _convert_to_pil(img, length, width):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ctk.CTkImage(img, size=(length, width))
    return img

if __name__ == "__main__":
    window = Window(
        # model=get_model()
        )
    window.run()