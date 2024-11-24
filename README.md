# Ai_Vision
This project is a Streamlit-powered web application designed to perform Scene Understanding and Object Detection using advanced AI technologies:

Features
1. Real-Time Scene Understanding:
Upload an image, and the application uses Google's Generative AI model (gemini-1.5-flash) to generate a descriptive textual output of the scene, helping users to understand the content effectively.
This feature is ideal for applications where users need quick descriptions of images, such as for accessibility, content analysis, or educational purposes.

2. Object Detection:
The application utilizes the SSD MobileNet V2 model hosted on TensorFlow Hub for object detection in uploaded images.
It automatically detects objects in the images (e.g., people, vehicles, animals, furniture) with high confidence scores, and highlights these objects using bounding boxes.
Objects with a confidence score higher than 0.5 will be displayed along with their labels and scores.


How It Works
1. Upload Image: Users upload an image using the file uploader interface.
2. Choose Function:
    Click on "Real-Time Scene Understanding" to get a textual description of the scene using Google's Generative AI model.
    Click on "Object and Obstacle Detection for Safe Navigation" to use the TensorFlow-based object detection model to identify and     highlight objects in the image.
3. View Results: After selecting a feature, the corresponding result will be displayed on the page:
    Scene Understanding results will appear in a text format.
    Object Detection results will display the annotated image with detected objects highlighted with green bounding boxes, object labels, and confidence scores.
4. Results Persistence: The results of the last action will remain visible until a new action is performed (i.e., until another button is clicked), helping users review the detected information without resetting the interface.

