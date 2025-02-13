# -*- coding: utf-8 -*-
"""Python_code_reviewer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rgWvQzx3Tvp_x-1AyncikZNg9S0k2xbL
"""

import streamlit as st
import google.generativeai as ai
ai.configure(api_key='AIzaSyBMCc42a-cWcpnG1TfCC830kbHG20dAqpo')
st.balloons()
st.snow()
sys_prompt="""You are a helpful Python application develpoer that allows users to submit their Python code for review and receive feedback on potential bugs along with suggestions
 for fixes. The application should be user-friendly, efficient, and provide accurate bug reports and fixed code snippets.In case if a student ask any question outside the python code scope,
                politely decline and tell them to ask the question from python code questions only."""
model=ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",system_instruction=sys_prompt)
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #000000; /* Black color */
            background-color: #f0f0f0; /* Light grey background */
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }
    </style>
    <div class="title">
        🌟 Suman's Python-Code Reviwer 🤖 📝
    </div>
""", unsafe_allow_html=True )
user_input = st.text_area(label="Enter your Python Code", placeholder="Write Python Code")
btn_click = st.button("Enter")
st.title("CODE REVIEW")
if btn_click == True:
    response = model.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)
