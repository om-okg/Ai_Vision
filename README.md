# Ai_Vision
This project is a Streamlit-powered web application designed to perform Scene Understanding and Object Detection using advanced AI technologies:

Features
Real-Time Scene Understanding:

Upload an image, and the application uses Google's Generative AI model (gemini-1.5-flash) to generate a descriptive textual output of the scene, helping users to understand the content effectively.
This feature is ideal for applications where users need quick descriptions of images, such as for accessibility, content analysis, or educational purposes.
Object Detection:

The application utilizes the SSD MobileNet V2 model hosted on TensorFlow Hub for object detection in uploaded images.
It automatically detects objects in the images (e.g., people, vehicles, animals, furniture) with high confidence scores, and highlights these objects using bounding boxes.
Objects with a confidence score higher than 0.5 will be displayed along with their labels and scores.

