import os
import tkinter as tk
from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Video Converter")
        self.default_directory = os.path.join(os.path.expanduser('~'), 'Downloads')  # Default directory
        self.initialize_ui()

    def initialize_ui(self):
        self.configure_window()  
        self.create_widgets()

    def configure_window(self):
        self.iconbitmap("assset/logo.ico")
        # Set the window size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = int(screen_width * 0.6)  # 60% of screen width
        window_height = int(screen_height * 0.6)  # 60% of screen height
        window_size = f"{window_width}x{window_height}"
        self.geometry(window_size)
        self.resizable(False,False)
        # background image
        image_path = "assset/background.png"
        original_image = Image.open(image_path)
        self.resized_image = original_image.resize((self.winfo_width(), self.winfo_height()))        
        self.tk_image = ImageTk.PhotoImage(self.resized_image)

        # self.background_label = tk.Label(self, image=self.tk_image)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_widgets(self):
        self.left_frame()
        self.right_frame()

    def left_frame(self):
        self.left_frame = tk.Frame(self, bg='white')  # Set a white background color for the frame
        self.left_frame.place(x=0, y=0, relwidth=0.6, relheight=1)
        self.background_label = tk.Label(self.left_frame, image=self.tk_image)
        self.background_label.place(x=0, y=0, relwidth=1.6, relheight=1)

        self.url_frame()
        self.dir_label_frame_()
        self.download_label_frame_()

    def url_frame(self):
        self.url_widgets = tk.Frame(self.left_frame)
        self.url_widgets.place(relx=0.2,rely=0.2)
    
        self.url_label = tk.Label(self.url_widgets, text="Enter Youtube URL: ")
        self.url_label.pack()

        self.url_entry = tk.Entry(self.url_widgets, width=50)
        self.url_entry.pack()

    def dir_label_frame_(self):
        self.dir_label_frame = tk.Frame(self.left_frame)
        self.dir_label_frame.place(relx=0.2,rely=0.4)

        self.select_button = tk.Button(self.dir_label_frame, text="Select Save Directory", command=self.select_directory)
        self.select_button.pack()

        self.save_dir_label = tk.Label(self.dir_label_frame, text="")
        self.save_dir_label.pack()

    def download_label_frame_(self):
        self.download_label_frame = tk.Frame(self.left_frame)
        self.download_label_frame.place(relx=0.2,rely=0.6)

        self.download_button = tk.Button(self.download_label_frame, text="Download", command=self.download_video)
        self.download_button.pack()

        self.status_label = tk.Label(self.download_label_frame, text="")
        self.status_label.pack()

        self.pb = ttk.Progressbar(self.download_label_frame, orient='horizontal', length=200, mode='determinate')
        self.pb.pack()

    def right_frame(self):
        left_frame_width = int(self.winfo_width() * 0.6)
        self.right_frame = tk.Frame(self, bg="red")
        self.right_frame.place(x=left_frame_width, y=0, relwidth=0.401, relheight=1)
        self.background_label = tk.Label(self.right_frame, image=self.tk_image)
        self.background_label.place(x= -left_frame_width, y=0, relwidth=2.5, relheight=1,anchor='nw')

    def select_directory(self):
        directory = filedialog.askdirectory()
        self.save_dir_label.config(text=directory)
        return directory

    def download_video(self):
        url = self.url_entry.get()
        directory = self.save_dir_label.cget("text")

        if url and directory:
            yt = YouTube(url, on_progress_callback=self.progress_callback)
            video = yt.streams.get_highest_resolution()
            video.download(directory)
            self.status_label.config(text="Download successful!")
        else:
            self.status_label.config(text="Please provide both URL and save directory.")

    def progress_callback(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        progress = (bytes_downloaded / total_size) * 100
        self.pb['value'] = progress


if __name__ == "__main__":
    app = App()
    app.mainloop()

