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
   
2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv

3. **Activate the Virtual Environment**:
   Activate the virtual environment to isolate your project dependencies.
   On Windows:
   ```bash
   .\venv\Scripts\activate

   On macOS/Linux:
   ```bash
   source venv/bin/activate

4. **Install Required Dependencies**
   Install the necessary dependencies using pip:
   ```bash
   pip install streamlit google-generativeai pillow tensorflow tensorflow-hub numpy

5. **Set Up the Google API Key**:
   - Obtain an API key from the Google Cloud Console.
   - Save the API key in a file named gemini.txt in your project directory.
     
6. **Run the Application**:
   Once the dependencies are installed and the API key is set up, you can run the Streamlit application using:
   ```bash
   python ai_vision.py

7. **Access the Application**:
    ```bash
    http://localhost:8501/
    ```
    Here, you can interact with the application by uploading an image and choosing between the Scene Understanding and Object Detection features.



### Code Overview:
**Key Functions**:
- collect_image(): Lets users upload images through the Streamlit file uploader.
- ai_title(): Displays the title "AI Vision" on the web page.
- scene_understanding(image): Uses Google Generative AI to generate a textual description of the uploaded image.
- object_detection(image): Uses TensorFlow's SSD MobileNet V2 to detect and highlight objects within the uploaded image.
- button_handling(image): Handles button clicks, performs the corresponding action (scene understanding or object detection), and displays results.


**TensorFlow Model**
The application uses the SSD MobileNet V2 pre-trained model available on TensorFlow Hub for object detection. It identifies a variety of objects (people, cars, animals, etc.) and marks them with green bounding boxes.

### Example Output:
1. **Scene Understanding**:
- Input: An image of a park.
- Output: "The uploaded image contains a park with trees, people, and a playground."
2. **Object Detection**:
- Input: An image containing a person and a car.
- Output: The image will be annotated with bounding boxes around the detected person and car, along with their respective confidence scores.
    
### Troubleshooting
1. Issue: Model Loading Error
- Ensure that your TensorFlow and TensorFlow Hub versions are compatible by installing the required packages.
2. Issue: Permission Denied
- If you're on Windows, ensure you have proper permissions for reading from and writing to the directories you're working with.   

### Future Enhancements
1. **More Object Categories**: Enhance object detection by adding more classes or models.
2. **Enhanced Scene Understanding**: Improve text generation for more complex scenes.
3. **Real-Time Processing**: Implement live image processing using webcam input.
4. **Accessibility Features**: Add text-to-speech functionality for scene descriptions to improve accessibility.



