import os
import tkinter as tk
from tkinter import messagebox
from imageCompressor import compress_and_downscale_images

def discover_subfolders(base_folder="./uncompressed/"):
    return [
        os.path.join(base_folder, name) for name in os.listdir(base_folder)
        if os.path.isdir(os.path.join(base_folder, name))
    ]

def start_batch_compression():
    try:
        quality = int(quality_var.get())
        max_width = int(width_var.get())
    except ValueError:
        messagebox.showerror("Error", "Quality and Width must be numbers.")
        return

    subfolders = discover_subfolders()
    if not subfolders:
        messagebox.showerror("Error", "No subfolders found in ./uncompressed/")
        return

    for folder in subfolders:
        folder_name = os.path.basename(folder.rstrip('/\\'))
        output_folder = os.path.join("./compresssed", f"{folder_name}_Compressed")
        os.makedirs(output_folder, exist_ok=True)
        compress_and_downscale_images(folder, output_folder, quality, max_width)

        # Optional Rename
        if rename_var.get():
            apply_rename(output_folder, folder_name)

    messagebox.showinfo("Done", "Batch Compression Completed!")

def apply_rename(output_folder, original_folder_name):
    instagram = instagram_var.get().strip()
    venue = venue_var.get().strip()
    date = date_var.get().strip()

    for idx, filename in enumerate(os.listdir(output_folder), start=1):
        file_path = os.path.join(output_folder, filename)
        if not os.path.isfile(file_path):
            continue

        ext = os.path.splitext(filename)[1]
        new_name = f"{instagram} - {original_folder_name} - {venue} - {date} - {idx:03d}{ext}"
        new_path = os.path.join(output_folder, new_name)

        os.rename(file_path, new_path)

root = tk.Tk()
root.title("Image Compressor - Subfolder Mode with Rename")

# Quality Input
tk.Label(root, text="Quality (1-100):").grid(row=0, column=0, sticky="w")
quality_var = tk.StringVar(value="85")
tk.Entry(root, textvariable=quality_var, width=5).grid(row=0, column=1, sticky="w")

# Max Width Input
tk.Label(root, text="Max Width (px):").grid(row=1, column=0, sticky="w")
width_var = tk.StringVar(value="1000")
tk.Entry(root, textvariable=width_var, width=5).grid(row=1, column=1, sticky="w")

# Rename Options
rename_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Enable Rename", variable=rename_var).grid(row=2, columnspan=2, sticky="w")

tk.Label(root, text="Instagram @").grid(row=3, column=0, sticky="w")
instagram_var = tk.StringVar(value="@handle")
tk.Entry(root, textvariable=instagram_var, width=30).grid(row=3, column=1, sticky="w")

tk.Label(root, text="Venue").grid(row=4, column=0, sticky="w")
venue_var = tk.StringVar()
tk.Entry(root, textvariable=venue_var, width=30).grid(row=4, column=1, sticky="w")

tk.Label(root, text="Date").grid(row=5, column=0, sticky="w")
date_var = tk.StringVar()
tk.Entry(root, textvariable=date_var, width=30).grid(row=5, column=1, sticky="w")

# Start Button
tk.Button(root, text="Start Compression (./uncompressed/)", command=start_batch_compression).grid(row=6, columnspan=2, pady=10)

root.mainloop()
