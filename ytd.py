import tkinter as tk
from pytube import YouTube
from tkinter import filedialog
from tkinter import ttk

# Save Directory Button
def select_directory():
    directory = filedialog.askdirectory()
    save_dir_label.config(text=directory)
    return directory

def download_video():
    url = url_entry.get()
    directory = save_dir_label.cget("text")  # Get the selected directory from the label
    
    if url and directory:
        yt = YouTube(url, on_progress_callback=progress_callback)
        video = yt.streams.get_highest_resolution()
        video.download(directory)
        status_label.config(text="Download successful!")
    else:
        status_label.config(text="Please provide both URL and save directory.")
 
def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = (bytes_downloaded / total_size) * 100
    pb['value'] = progress

window = tk.Tk()
window.title("YouTube Video Downloader")
window.geometry("500x500")

url_label = tk.Label(window, text="Enter Youtube URL: ")
url_label.pack()

url_entry = tk.Entry(window, width=50)
url_entry.pack()

select_button = tk.Button(window, text="Select Save Directory", command=select_directory)
select_button.pack()

save_dir_label = tk.Label(window, text="")
save_dir_label.pack()

download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

pb = ttk.Progressbar(window, orient='horizontal', length=200, mode='determinate')
pb.pack()

window.mainloop()
