import streamlit as st

# 값 입력 받기
animal_name = st.text_input("Animal Name")

searching = st.button("Search", type="primary")

# 입력 받은 동물 이미지 찾기
if searching:
    if animal_name == "":
        st.warning("Please enter an animal name.")
    else:
        # 동물 이름을 소문자로 변환
        animal_name = animal_name.lower()
        # 동물 이미지 링크 생성
        animal_image_link = f"https://spartacodingclub.study/random/?{animal_name}"
        # 찾은 동물 이미지를 출력하기
        st.image(animal_image_link)


