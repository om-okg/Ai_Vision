import streamlit as st
import google.generativeai as genai
from PIL import Image, ImageDraw
import time
import tensorflow as tf
import numpy as np
import tensorflow_hub as hub

def collect_image():
    image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    return image

def ai_title():
    st.markdown(
    """
    <style>
    .custom-text {
        font-size: 50px;
        font-weight: bold;
        color: #002244 !important; /*Dark Midnight Blue*/
    }
    </style>
    <p class="custom-text">AI Vision</p>
    """,
    unsafe_allow_html=True
)

def scene_understanding(image):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    prompt = "Generate descriptive textual output that interprets the content of the uploaded image, enabling user to understand the scene effectively."
    response = model.generate_content([image, prompt])
    return response.text

def object_detection(image):
    # Load pre-trained model from TensorFlow Hub (SSD model for object detection)
    model = hub.load('https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2')

    # Convert the image to RGB and resize it to meet model input requirements
    image = image.convert("RGB")
    image_np = np.array(image)
    
    # Resize image for model input (300, 300)
    image_np_resized = tf.image.resize(image_np, (300, 300))  # Resize image for model input
    
    # Ensure the image has the correct dtype (uint8) expected by the model
    image_np_resized = tf.cast(image_np_resized, dtype=tf.uint8)  # Cast to uint8

    # Add batch dimension
    input_tensor = tf.convert_to_tensor(image_np_resized)
    input_tensor = input_tensor[tf.newaxis, ...]  # Add batch dimension

    # Perform object detection
    detections = model(input_tensor)

    # Get the bounding boxes and labels
    boxes = detections['detection_boxes'][0].numpy()
    class_ids = detections['detection_classes'][0].numpy().astype(int)
    scores = detections['detection_scores'][0].numpy()

    # Draw the bounding boxes on the image
    annotated_image = image.copy()
    draw = ImageDraw.Draw(annotated_image)

    for i in range(len(boxes)):
        if scores[i] > 0.25:  # Filter out low-confidence detections
            ymin, xmin, ymax, xmax = boxes[i]
            width, height = image.size
            (left, right, top, bottom) = (xmin * width, xmax * width, ymin * height, ymax * height)

            # Draw bounding box
            draw.rectangle([left, top, right, bottom], outline="green", width=10)
            label = f"Object {class_ids[i]}: {scores[i]:.2f}"
            draw.text((left, top - 10), label, fill="red")

    # Display the annotated image in Streamlit
    st.image(annotated_image, caption="Detected Objects", use_container_width=True)

    return f"Detected {len(boxes)} object(s)"

def button_handling(image):
    # Initialize session state to track the active button
    if "clicked_button" not in st.session_state:
        st.session_state.clicked_button = None

    # Buttons for features
    button1_placeholder = st.empty()
    button2_placeholder = st.empty()

    btn_scene = button1_placeholder.button("Real-Time Scene Understanding")
    btn_objectDetection = button2_placeholder.button("Object and Obstacle Detection for Safe Navigation")

    # When a button is clicked, perform the action and hide other buttons
    if btn_scene:
        st.session_state.clicked_button = 1
        st.session_state.result = scene_understanding(image)
        st.session_state.result_type = "Scene Understanding"
    elif btn_objectDetection:
        st.session_state.clicked_button = 2
        st.session_state.result = object_detection(image)
        st.session_state.result_type = "Object Detection"

    # Show the result based on the action taken
    if 'result' in st.session_state:
        st.write(st.session_state.result)

def main():
    ai_title()

    image = collect_image()

    if image:
        st.image(image, caption="Uploaded Image", use_container_width=True)
        opened_image = Image.open(image)
        
        button_handling(opened_image)  # Call button handling once

if __name__ == "__main__":
    # Google API setup
    genai.configure(api_key="AIzaSyAwozLYn8tRSFY18TVTuV6uA0Q8fqdrCkI")
    main()  # Invoke main function
