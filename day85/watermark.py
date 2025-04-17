import tkinter as tk

from tkinter import filedialog, messagebox

from PIL import Image, ImageTk, ImageDraw, ImageFont



class WatermarkApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Image Watermarker")



        self.image_path = None

        self.image = None

        self.tk_image = None



        self.label = tk.Label(root, text="No image selected", font=("Arial", 14))

        self.label.pack(pady=10)



        self.canvas = tk.Canvas(root, width=400, height=300, bg="gray")

        self.canvas.pack()



        tk.Button(root, text="Upload Image", command=self.upload_image).pack(pady=5)



        self.watermark_entry = tk.Entry(root, width=40)

        self.watermark_entry.pack(pady=5)

        self.watermark_entry.insert(0, "Enter watermark text here")



        tk.Button(root, text="Add Watermark", command=self.add_watermark).pack(pady=5)



    def upload_image(self):

        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])

        if file_path:

            self.image_path = file_path

            self.image = Image.open(self.image_path).convert("RGBA")

            resized = self.image.resize((400, 300))

            self.tk_image = ImageTk.PhotoImage(resized)

            self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

            self.label.config(text="Image loaded!")



    def add_watermark(self):

        if not self.image:

            messagebox.showerror("Error", "No image loaded!")

            return



        text = self.watermark_entry.get()

        watermark = Image.new("RGBA", self.image.size)

        draw = ImageDraw.Draw(watermark)



        font_size = int(min(self.image.size) / 10)

        font = ImageFont.truetype("arial.ttf", font_size)



        text_width, text_height = draw.textsize(text, font)

        x = self.image.size[0] - text_width - 20

        y = self.image.size[1] - text_height - 20



        draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))



        combined = Image.alpha_composite(self.image, watermark)

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        if save_path:

            combined.convert("RGB").save(save_path)

            messagebox.showinfo("Saved", f"Watermarked image saved to:\n{save_path}")



# Run the app

if __name__ == "__main__":

    root = tk.Tk()

    app = WatermarkApp(root)

    root.mainloop()
