import streamlit as st
import keras_ocr

#defining a pipeline for the model
pipeline = keras_ocr.pipeline.Pipeline()

#Main function to extract image
def extract_text(image):
    images = [image]
    name =""

    prediction_groups = pipeline.recognize(images)
    for i in prediction_groups[0]:
        name+=i[0]+" "
    return name

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #000a1f; /* Even Darker Navy Blue */
        color: white;
    }
    .stButton>button {
        background-color: #FF851B; /* Orange */
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .stTextInput>div>div>input {
        background-color: #e6e6e6;
    }
    .header {
        background-color: #FF851B; /* Orange */
        padding: 10px;
        text-align: center;
        color: white;
        font-size: 24px;
    }
    .output-box {
        background-color: #FF851B; /* Orange */
        padding: 20px;
        border-radius: 5px;
        color: white;
        font-size: 18px;
        text-align: center;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #000a1f; /* Even Darker Navy Blue */
        text-align: center;
        padding: 10px;
        color: #FF851B; /* Orange */
    }
    .image-container {
        text-align: center;
    }
    .image-container img {
        max-width: 100%; /* Set maximum width to 100% of its container */
        height: auto; /* Maintain aspect ratio */
        display: block;
        margin: auto;
    }
    .content {
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<div class="header"><b>Extract Text from Image<b></div>', unsafe_allow_html=True)

# Sidebar: Image Upload
uploaded_image = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Main content area for image display and output
st.markdown('<div class="content">', unsafe_allow_html=True)

if uploaded_image is not None:
    # Read the image
    image = keras_ocr.tools.read(uploaded_image)

    # Display the uploaded image with a smaller width
    st.markdown('<div class="image-container">', unsafe_allow_html=True)

    st.image(image, width=300)
    st.markdown('</div>', unsafe_allow_html=True)

    # Placeholder for text output
    placeholder = st.empty()

    # Simulating some processing
    with st.spinner('Extracting text...'):
        text = extract_text(image)  # Simulating a delay for processing

    # Example text output
    text_output = extract_text(image)

    # Display text output in an orange box
    placeholder.markdown(f'<div class="output-box">{text_output}</div>', unsafe_allow_html=True)
else:
    st.text("Please upload an image to see the output.")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        -made by deepmbhatt using Streamlit🌌
    </div>
    """,
    unsafe_allow_html=True
)
