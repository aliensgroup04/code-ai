# -*- coding: utf-8 -*-
"""AI_Tutor_Task-4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17nIoOEZOm_9UqAOUWa1b4kYQc4xtOinp
"""

import streamlit as st
import google.generativeai as ai

ai.configure(api_key='AIzaSyBMCc42a-cWcpnG1TfCC830kbHG20dAqpo')

sys_prompt="""You are a helpful Python application develpoer that allows users to submit their Python code for review and receive feedback on potential bugs along with suggestions
 for fixes. The application should be user-friendly, efficient, and provide accurate bug reports and fixed code snippets.
"""

model=ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",system_instruction=sys_prompt)

st.title("Suman's AI Code Reviewer")
st.subtitle("Enter/Paste Your Python Code")

user_input = st.text_area(label="Enter your Python Code", placeholder="Explain the concept AI")

btn_click = st.button("Enter")

if btn_click == True:
    response = model.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)