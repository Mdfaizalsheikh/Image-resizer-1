import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class ImageConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")

        self.file_path = ""
        
        
        file_frame = tk.Frame(root)
        file_frame.pack(pady=20)
        
        
        upload_button = tk.Button(file_frame, text="Upload Image", command=self.upload_image)
        upload_button.pack(side=tk.LEFT, padx=10)
        
        
        self.file_label = tk.Label(file_frame, text="No file selected")
        self.file_label.pack(side=tk.LEFT, padx=10)
        
        
        format_label = tk.Label(root, text="Select Format:")
        format_label.pack(pady=5)
        
        self.format_var = tk.StringVar()
        self.format_var.set("PNG")
        format_dropdown = tk.OptionMenu(root, self.format_var, "PNG", "JPEG", "BMP")
        format_dropdown.pack(pady=5)
        
        
        convert_button = tk.Button(root, text="Convert & Save Image", command=self.convert_and_save)
        convert_button.pack(pady=20)
        
    def upload_image(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if self.file_path:
            self.file_label.config(text=self.file_path)
        
    def convert_and_save(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file selected!")
            return
        
        try:
            img = Image.open(self.file_path)
            target_format = self.format_var.get().lower()
            save_path = filedialog.asksaveasfilename(defaultextension=f".{target_format}", filetypes=[(f"{target_format.upper()} files", f"*.{target_format}")])
            if save_path:
                img.save(save_path, format=target_format.upper())
                messagebox.showinfo("Success", f"Image saved as {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert image: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverter(root)
    root.mainloop()
