
import streamlit as st

st.set_page_config(
    page_title="Калькулятор",
    page_icon="🧮"
)

st.title("🧮 Менің калькуляторым")
st.write("Қарапайым есептеу бағдарламасы")

a = st.number_input("Бірінші санды енгізіңіз")
b = st.number_input("Екінші санды енгізіңіз")

operation = st.selectbox(
    "Амал таңдаңыз",
    ["Қосуу (+)", "Азайту (-)", "Көбейту (*)", "Бөлу (/)"]
)

if st.button("Есептеу"):

    result = None

    if operation == "Қосуу (+)":
        result = a + b

    elif operation == "Азайту (-)":
        result = a - b

    elif operation == "Көбейту (*)":
        result = a * b

    elif operation == "Бөлу (/)":
        if b != 0:
            result = a / b
        else:
            st.error("Нөлге бөлуге болмайды!")

    if result is not None:
        st.success(f"Нәтиже: {result}")
