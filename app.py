import streamlit as st
import openai
import pandas as pd
from langchain_community.chat_models import ChatOpenAI
 

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"
def get_gpt3_response(prompt, file_content=None,model="gpt-3.5-turbo"):
    if file_content:
        # If a file is uploaded, decode its content to a string
        file_content = file_content.decode("utf-8")
        prompt += "\nFile Content:\n" + file_content
 
 
    message=[{"role":"user","content":prompt}]
    response=openai.ChatCompletion.create(
        model=model,
        messages=message,
        temperature=0
    )
    return response.choices[0].message['content']
 
# Streamlit app
def main():
   
   
 
    st.set_page_config(page_title='MuleSoft Integration Assistant with ChatGPT')
   
    st.title("Welcome to the MuleSoft Integration Assistant!")
   
    col1, col2, col3 = st.columns(3)
 
    with col1:
        st.write("This application provides assistance and guidance for MuleSoft integration development using ChatGPT. Describe any issues or error messages you're facing , we will provide potential solutions and debugging tips")
   
    with col2:
        st.write("Seek recommendations for designing robust and scalable integrations. Describe your use cases and requirements for personalized guidance.Share snippets of your integration code for review , feedback, optimization suggestions, and tips on adhering to MuleSoft and integration best practices ")
   
 
    with col3:
        st.write("Inquire about the appropriate design patterns for your integration scenarios , security best practices , data transformation scenarios and MuleSoft components, connectors, or features. ")
 
   
    # Upload file section
    st.header("Upload File")
    uploaded_file = st.file_uploader("Choose a file", type=["json", "csv", "xml", "txt"])
 
    # Input prompt section
    st.header("Input Prompt")
    prompt = st.text_area("Enter your prompt")
 
    # Check if the file is uploaded and get its content
    file_content = None
    if uploaded_file is not None:
        file_content = uploaded_file.read()
 
    # Button to submit prompt and get GPT-3 response
    if st.button("Submit Prompt"):
        if not prompt and not file_content:
            st.warning("Please enter a prompt or upload a file.")
        else:
            # Get GPT-3 response
            response = get_gpt3_response(prompt, file_content)
            # response = generate_response(prompt, file_content)
 
            st.subheader("MuleSoft Integration Assistant Response:")
            st.write(response)
 
if __name__ == "__main__":
    main()
