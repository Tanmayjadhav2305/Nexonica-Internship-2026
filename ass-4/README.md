# Assignment 4: Image Processing Operations

This assignment demonstrates various image processing operations using OpenCV in Python. Each script performs a specific transformation on an input image named "image.jpeg" (which must be present in the same directory).

## Files Description

### app.py
- **Purpose**: Basic image loading and display
- **Functionality**: Loads an image file and displays it in a window using OpenCV
- **Requirements**: OpenCV (`pip install opencv-python`)

### gray.py
- **Purpose**: Convert image to grayscale
- **Functionality**: Converts a color image to grayscale by averaging the RGB values of each pixel
- **Algorithm**: For each pixel, calculates average of R, G, B values and sets all channels to this average

### binarize.py
- **Purpose**: Convert image to binary (black and white)
- **Functionality**: Applies thresholding to create a binary image
- **Algorithm**: Pixels with average value > 127 become white (255,255,255), others become black (0,0,0)

### mirror.py
- **Purpose**: Create horizontal mirror image
- **Functionality**: Flips the image horizontally
- **Algorithm**: Copies pixels from right to left for each row

### rotate.py
- **Purpose**: Rotate image 90 degrees clockwise
- **Functionality**: Rotates the image by 90 degrees in clockwise direction
- **Algorithm**: Creates new image with swapped dimensions and maps pixels accordingly

### bluish.py
- **Purpose**: Apply bluish tint to image
- **Functionality**: Makes the image appear bluish
- **Algorithm**: Sets blue channel to 255, red and green channels to the average of original RGB

### greenish.py
- **Purpose**: Apply greenish tint to image
- **Functionality**: Makes the image appear greenish
- **Algorithm**: Sets green channel to 255, red and blue channels to the average of original RGB

### reddish.py
- **Purpose**: Apply reddish tint to image
- **Functionality**: Makes the image appear reddish
- **Algorithm**: Sets red channel to 255, green and blue channels to the average of original RGB

## Requirements
- Python 3.x
- OpenCV: `pip install opencv-python`
- Input image: "image.jpeg" in the same directory as the scripts

## Usage
Run any script using: `python <script_name>.py`

Each script will:
1. Load the image
2. Apply the transformation
3. Display both original and transformed images
4. Wait for key press to close windows

## Notes
- All scripts assume the input image is in JPEG format named "image.jpeg"
- Scripts use nested loops for pixel manipulation (educational purposes)
- OpenCV windows will remain open until a key is pressed