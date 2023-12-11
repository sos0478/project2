import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

a2_up = str(st.session_state["a2_up"])
b2_up = str(st.session_state["b2_up"])
Q2_UP_Text = st.session_state["Q2_UP"].replace('a', a2_up)
Q2_UP_Text = Q2_UP_Text.replace('b', b2_up)

st.header("고난도 문제 1번")
st.subheader(Q2_UP_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")

if "N2_UP" not in st.session_state:
    st.session_state["N2_UP"] = True

if "B7" not in st.session_state:
    st.session_state["B7"] = False

def make1():
    st.session_state["B7"] = True

st.write("고난도 문제는 채점 기회가 1번 뿐이니 신중하게 눌러주세요.")
if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B7"]):
    if float(answer1) == float(st.session_state["x2_up"]):
        st.session_state["C1"] = st.session_state["C1"] + 1
        st.session_state["C2"] = st.session_state["C2"] + 1
        st.session_state["N2_UP"] = False
        st.write("정답입니다.")
    else:
        st.write("아쉽지만 오답입니다.")
        st.write("문제를 바탕으로 세운 식을 확인해보면 ", st.session_state["a2_up"], "\u00F7", st.session_state["b2_up"], "이 됩니다.")
        st.write("세운 식이 맞다면 계산 실수를 한 것이니 신중하게 풀도록 하고, 세운 식이 잘못되었다면 문제에서 위의 식을 어떻게 끌어냈는지 확인하고 다음 문제로 넘어가봅시다.")
        st.session_state["N2_UP"] = False


st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N2_UP"]):
    switch_page("Q3")