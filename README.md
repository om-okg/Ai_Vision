# AI Vision Application

This project is a Streamlit-powered web application that allows users to upload images and leverage **AI-based Scene Understanding** and **Object Detection** features. The application integrates Google's **Generative AI** for scene description and **TensorFlow's SSD MobileNet V2 model** for object detection. 

## Features
1. **Real-Time Scene Understanding**:
   - Upload an image to get a descriptive textual output using Google's **Generative AI** (`gemini-1.5-flash` model). 
   - Ideal for understanding the content of images for accessibility, analysis, or educational purposes.

2. **Object and Obstacle Detection**:
   - Using **TensorFlow's SSD MobileNet V2** model, the app detects objects within the image (e.g., people, cars, animals, etc.) and highlights them with bounding boxes and labels.
   - Objects are only shown if the model's confidence score is above 0.25.

## How It Works
1. **Upload Image**: Users upload an image file (JPG, PNG, JPEG).
2. **Choose Action**:
   - **Scene Understanding**: Click on the "Real-Time Scene Understanding" button to get a textual description of the uploaded image.
   - **Object Detection**: Click on the "Object and Obstacle Detection for Safe Navigation" button to get bounding boxes and labels for the objects detected in the image.
3. **View Results**:
   - **Scene Understanding**: A textual description is displayed.
   - **Object Detection**: The image will be annotated with detected objects, their class IDs, and confidence scores.

The results will persist on the page until a new button is clicked.

## Installation

### Requirements:
- **Python 3.7+**
- **Pip** for package installation.

### Step-by-Step Instructions:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repository-url.git
