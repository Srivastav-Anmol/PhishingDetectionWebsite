import streamlit as st
import requests

# Define FastAPI server URL
API_URL = "http://localhost:8000/predict"

# Streamlit UI layout
col1, col2, col3 = st.columns(3)

# Display the image in the center column
with col2:
    st.image(
        "https://www.ntu.ac.uk/__data/assets/image/0032/2233859/phishing.jpg",
        width=320
    )

# Title and subtitle in the center
st.markdown(
    "<h1 style='text-align: center; color: #14559E'>FalseX</h1>", unsafe_allow_html=True
)
st.markdown(
    "<h3 style='text-align: center; color: #494848;'>Malicious URL Detection</h3>", unsafe_allow_html=True
)

# URL input field
url_input = st.text_input("Enter URL:", "")

# Classification button
if st.button("Classify"):
    if url_input:
        try:
            # Make POST request to FastAPI server
            response = requests.post(API_URL, json={"url": url_input})
            data = response.json()
            
            # Unpack the prediction values from the API response
            score, InTop1Million, isOlderThan3Months = data.get("prediction")
            
            # Format the output as desired
            st.write(f"The URL '{url_input}' is:")
            st.write(f"Score: {score}")
            st.write(f"In Top 1 Million Website: {InTop1Million}")
            st.write(f"Is older than Three Months: {isOlderThan3Months}")

            # Determine the conclusion based on the score
            if score >=170 and InTop1Million==True and isOlderThan3Months ==True:
                st.write("Conclusion: ✅ It is not a Malicious Website.")
            else:
                st.write("Conclusion: ⛔️ It is a Malicious Website.")

        except Exception as e:
            st.write(f"Error: {e}")
    else:
        st.write("Please enter a URL.")
