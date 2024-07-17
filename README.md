Image Text Extraction Application
This project is an image text extraction application built using Streamlit and Keras OCR. The application allows users to upload images of logos and extracts any text present in the images. The extracted text is then displayed in a styled output box. This project demonstrates the integration of machine learning and web technologies to create a user-friendly tool for text extraction from images.

Features
Image Upload: Users can upload images in JPG, JPEG, or PNG formats.
Text Extraction: Uses Keras OCR to accurately recognize and extract text from uploaded images.
Interactive UI: Built with Streamlit to provide an intuitive and interactive user experience.
Custom Styling: Custom CSS for a modern, clean look with a dark theme.
Loading Spinner: Indicates processing time during text extraction to enhance user feedback.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/image-text-extraction-app.git
cd image-text-extraction-app
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Streamlit application:

bash
Copy code
streamlit run app.py
Open your web browser and navigate to the local URL provided by Streamlit.

Upload an image through the sidebar and click the "Extract Text" button to see the extracted text.
