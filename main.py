import tkinter as tk
from tkinter import filedialog
import yolo

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", fg_placeholder="gray", bg="white", width=50, borderwidth=2, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.placeholder = placeholder
        self.fg_placeholder = fg_placeholder
        
        self.configure(bg=bg, width=width, borderwidth=borderwidth)
        
        self.bind('<FocusIn>', self.on_entry_click)
        self.bind('<FocusOut>', self.on_focus_out)
        
        self.insert_placeholder()
    
    def insert_placeholder(self):
        self.insert(0, self.placeholder)
        self.config(fg=self.fg_placeholder)
    
    def on_entry_click(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg='black')
    
    def on_focus_out(self, event):
        if self.get() == '':
            self.insert_placeholder()

# Create the GUI window
window = tk.Tk()
window.title("Water Level Detection")

# Create labels for user inputs
firstCoordinate_label = tk.Label(window, text="Enter the starting point's coordinates of the perpendicular line:")
firstCoordinate_label.pack()
firstCoordinate_entry = EntryWithPlaceholder(window, placeholder="E.g: 1094 231", bg="white", width=50, borderwidth=2)
firstCoordinate_entry.pack(padx=10, pady=5)

secondCoordinate_label = tk.Label(window, text="Enter the ending point's coordinates of the perpendicular line:")
secondCoordinate_label.pack()
secondCoordinate_entry = EntryWithPlaceholder(window, placeholder="E.g: 1083 403", bg="white", width=50, borderwidth=2)
secondCoordinate_entry.pack(padx=10, pady=5)

pixelsInAMeter_label = tk.Label(window, text="Enter the number of pixels equivalent to a meter in real life:")
pixelsInAMeter_label.pack()
pixelsInAMeter_entry = EntryWithPlaceholder(window, placeholder="E.g: 15", bg="white", width=50, borderwidth=2)
pixelsInAMeter_entry.pack(padx=10, pady=5)

tipHeight_label = tk.Label(window, text="Enter the real-life height (meters) of the higher point in line:")
tipHeight_label.pack()
tipHeight_entry = EntryWithPlaceholder(window, placeholder="E.g: 15", bg="white", width=50, borderwidth=2)
tipHeight_entry.pack(padx=10, pady=5)

warningLevel_label = tk.Label(window, text="Enter the water level (meters) that triggers the warning:")
warningLevel_label.pack()
warningLevel_entry = EntryWithPlaceholder(window, placeholder="E.g: 10", bg="white", width=50, borderwidth=2)
warningLevel_entry.pack(padx=10, pady=5)

def select_video():
    video_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi")])
    if video_path:
        yolo.yolo(video_path, float(firstCoordinate_entry.get().split()[0]), float(firstCoordinate_entry.get().split()[1]), float(secondCoordinate_entry.get().split()[0]), float(secondCoordinate_entry.get().split()[1]), float(pixelsInAMeter_entry.get()), float(tipHeight_entry.get()), float(warningLevel_entry.get()))
        notice_label = tk.Label(window, text="Result is saved to Output Video.mp4")
        notice_label.pack()

# Set the window size
window.geometry("600x400")  # Set the width and height according to your preference

# Create a button to select the video file
select_button = tk.Button(window, text="Select Video", command=select_video)
select_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
