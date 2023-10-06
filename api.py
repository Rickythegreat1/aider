import tkinter as tk
from tkinter import messagebox, filedialog
import os
import yaml

def create_config_file(api_key, path):
    config = {
        'openai_api_key': api_key
    }
    with open(os.path.join(path, '.aider.conf.yml'), 'w') as f:
        yaml.dump(config, f)

def browse_directory():
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def submit_config():
    api_key = api_key_entry.get()
    path = folder_path.get()
    create_config_file(api_key, path)
    messagebox.showinfo("Success", "Config file created successfully!")

root = tk.Tk()

api_key_label = tk.Label(root, text="OpenAI API Key:")
api_key_label.pack()

api_key_entry = tk.Entry(root)
api_key_entry.pack()

folder_path = tk.StringVar()
folder_label = tk.Label(root, text="Folder Path:")
folder_label.pack()

folder_entry = tk.Entry(root, textvariable=folder_path)
folder_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack()

submit_button = tk.Button(root, text="Submit", command=submit_config)
submit_button.pack()

root.mainloop()
