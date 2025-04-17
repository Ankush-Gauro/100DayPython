import cv2
import numpy as np
from collections import Counter
from flask import Flask, render_template, request
from PIL import Image
import io

app = Flask(__name__)

def extract_colors(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Flatten image to get all pixels
    pixels = image.reshape(-1, 3)
    
    # Convert to tuple for easier counting
    pixels = [tuple(pixel) for pixel in pixels]
    
    # Get most common colors
    color_counts = Counter(pixels)
    common_colors = color_counts.most_common(10)
    
    # Convert RGB to HEX
    hex_colors = ['#' + ''.join(f'{x:02x}' for x in color[0]) for color in common_colors]
    
    return hex_colors

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['file']
        image_bytes = file.read()
        
        # Convert bytes to image
        image = Image.open(io.BytesIO(image_bytes))
        image.save('uploaded_image.jpg')
        
        # Extract the top 10 colors
        colors = extract_colors('uploaded_image.jpg')
        
        return render_template('result.html', colors=colors)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)