import tkinter as tk
from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Video Converter")
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
        bg_image = tk.PhotoImage(file=image_path)
        background_label = tk.Label(self, image=bg_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_widgets(self):
        self.url_label = tk.Label(self, text="Enter Youtube URL: ")
        self.url_label.pack()

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack()

        self.select_button = tk.Button(self, text="Select Save Directory", command=self.select_directory)
        self.select_button.pack()

        self.save_dir_label = tk.Label(self, text="")
        self.save_dir_label.pack()

        self.download_button = tk.Button(self, text="Download", command=self.download_video)
        self.download_button.pack()

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

        self.pb = ttk.Progressbar(self, orient='horizontal', length=200, mode='determinate')
        self.pb.pack()

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

