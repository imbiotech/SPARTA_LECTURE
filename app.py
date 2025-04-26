import streamlit as st
import openai
import os

# Set API key from environment variable
API_KEY = st.secrets["OPENAI_API_KEY"]
if API_KEY is None:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client with the API key
client = openai.OpenAI(api_key = API_KEY)

# 값 입력 받기
mbti_prompt = st.text_input("당신의 성격을 적어주세요.")

# OpenAI API를 사용하여 MBTI 결과를 생성합니다.
def get_mbti_response(prompt):

    # Spinner를 사용하여 로딩 중임을 표시합니다.
    with st.spinner("MBTI 결과를 생성하는 중입니다..."):
        try:
            response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "너는 MBTI 전문가야. 사용자가 입력한 성격 특징을 바탕으로 웹 검색을 수행하여 가장 적절한 MBTI 성격 유형을 찾아서 알려줘."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            )

            if response.choices and response.choices[0].message:
                return response.choices[0].message.content
            else:
                return "MBTI 정보를 찾을 수 없습니다."
        except Exception as e:
            st.error(f"오류 발생: {e}")
            return "MBTI 정보를 찾을 수 없습니다."
    

searching = st.button("내 MBTI를 알려주세요.", type="primary")

# Dalle-3 Model을 사용하여 입력받은 MBTI 와 유사한 이미지를 생성합니다.
def generate_image(prompt):
    # Spinner를 사용하여 로딩 중임을 표시합니다.
    with st.spinner("이미지를 생성하는 중입니다..."):
        try:
            # DALL-E API를 사용하여 이미지를 생성합니다.
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size="1024x1024",
            )
            if response.data and len(response.data) > 0:
                return response.data[0].url
            else:
                return None
        except Exception as e:
            st.error(f"오류 발생: {e}")
            return None
