import streamlit as st
st.set_page_config(
 page_title="Студент үлгерімі",
 page_icon=""
)
st.title("Студенттің орташа бағасын есептеу")
st.write("Үш пән бойынша бағаларыңызды енгізіңіз.")
name = st.text_input("Студенттің аты-жөні")
math_grade = st.number_input(
 "Математика бағасы", min_value=0, max_value=100, value=0
)
python_grade = st.number_input(
 "Python бағасы", min_value=0, max_value=100, value=0
)
web_grade = st.number_input(
 "Web бағдарламалау бағасы", min_value=0, max_value=100, value=0
)
if st.button("Орташа балды есептеу"):
    if name.strip() == "":
        st.warning("Аты-жөніңізді енгізіңіз.")
    else:
        average = (math_grade + python_grade + web_grade) / 3
        st.subheader(f"Нәтиже: {name}")
        st.metric("Орташа балл", f"{average:.2f}")
    if average >= 85:
        st.success("Өте жақсы нәтиже!")
    elif average >= 70:
        st.info("Жақсы нәтиже!")
    elif average >= 50:
        st.warning("Қанағаттанарлық нәтиже.")
    else:
        st.error("Үлгерімді жақсарту қажет.")