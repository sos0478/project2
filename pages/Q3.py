import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

Q3_Text = f'3. {st.session_state["a3"]} \u00F7 {st.session_state["b3"]} ='
st.title(Q3_Text)
answer1 = st.number_input("답 : ", key="1")
st.session_state["N3"] = True

if "B8" not in st.session_state:
    st.session_state["B8"] = False
if "B9" not in st.session_state:
    st.session_state["B9"] = False
if "B10" not in st.session_state:
    st.session_state["B10"] = False

def make1():
    st.session_state["B8"] = True
def make2():
    st.session_state["B9"] = True
def make3():
    st.session_state["B10"] = True

if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B8"]):
    if float(answer1) == float(st.session_state["x3"]):
        st.session_state["C3"] = st.session_state["C3"] + 1
        st.session_state["N3"] = False
        st.write("정답입니다.")
    else:
        st.session_state["Q3"] = st.session_state["Q3"] + 1


if st.session_state["Q3"] == 1:
    st.write("혹시 계산 실수가 있었나요? 천천히 계산해보고 다시 답을 입력해주세요.")
    answer2 = st.number_input("답 : ", key="2")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B9"]):     
        if float(answer2) == float(st.session_state["x3"]):
            st.session_state["C3"] = st.session_state["C3"] + 1
            st.session_state["N3"] = False
            st.write("정답입니다.")
        else:
            st.session_state["Q3"] = st.session_state["Q3"] + 1
       

if st.session_state["Q3"] == 2:  
    st.write("소수의 나눗셈을 이해하는 데 어려움이 있는 것 같군요. 그렇다면 자연수의 나눗셈으로 바꿔봅시다.")
    a3 = int(st.session_state["a3"]*100)
    b3 = int(st.session_state["b3"]*100)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 답은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 100을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", st.session_state["a3"], "이 ", a3, "로 바뀌게 되고,")
    st.write(st.session_state["b3"], "이 ", b3, "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 식을 풀어봅시다.")
    Q3_easy_Text = f"3. {a3} \u00F7 {b3} ="
    st.markdown(Q3_easy_Text)
    answer3 = st.number_input("답 : ", key="3")
    if st.button("채점하기", key="c", on_click=make3, disabled=st.session_state["B10"]): 
        if float(answer3) == float(st.session_state["x3"]):
            st.session_state["N3"] = False
            st.write("정답입니다. 처음 문제를 방금 푼 자연수의 나눗셈으로 바꾸듯이 소수의 나눗셈은 소수점을 이동하여 자연수의 나눗셈으로 만들어 풀면 됩니다.")
        else:
            st.session_state["Q3"] = st.session_state["Q3"] + 1


if st.session_state["Q3"] == 3:
    st.session_state["N3"] = False
    st.write("오답입니다. 자연수의 나눗셈에도 어려움이 있거나 계산 실수가 있는 것 같네요. 일단 다음 문제를 이어서 풀어봅시다.")

st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N3"]):
    switch_page("Q4")