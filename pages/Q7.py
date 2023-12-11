import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

Q7_Text = f'7. {int(st.session_state["a7"])} \u00F7 {st.session_state["b7"]} ='
st.title(Q7_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")

if "N7" not in st.session_state:
    st.session_state["N7"] = True

if "B22" not in st.session_state:
    st.session_state["B22"] = False
if "B23" not in st.session_state:
    st.session_state["B23"] = False
if "B24" not in st.session_state:
    st.session_state["B24"] = False

def make1():
    st.session_state["B22"] = True
def make2():
    st.session_state["B23"] = True
def make3():
    st.session_state["B24"] = True

if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B22"]):
    if float(answer1) == float(st.session_state["x7"]):
        st.session_state["C7"] = st.session_state["C7"] + 1
        st.session_state["N7"] = False
        st.write("정답입니다.")
    else:
        st.session_state["Q7"] = st.session_state["Q7"] + 1


if st.session_state["Q7"] == 1:
    st.write("혹시 계산 실수가 있었나요? 천천히 계산해보고 다시 답을 입력해주세요.")
    answer2 = st.number_input("답 : ", key="2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B23"]):     
        if float(answer2) == float(st.session_state["x7"]):
            st.session_state["C7"] = st.session_state["C7"] + 1
            st.session_state["N7"] = False
            st.write("정답입니다.")
        else:
            st.session_state["Q7"] = st.session_state["Q7"] + 1
       

if st.session_state["Q7"] == 2:  
    st.write("자연수를 소수로 나누는 나눗셈을 이해하는 데 어려움이 있는 것 같군요. 그렇다면 자연수끼리의 나눗셈으로 바꿔봅시다.")
    a7 = int(st.session_state["a7"]*10)
    b7 = int(st.session_state["b7"]*10)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 답은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("주의할 점은 나누어지는 수는 이미 자연수라도 나누는 수를 자연수로 만들기 위해 같은 수를 꼭 곱해줘야 한다는 것입니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 10을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", int(st.session_state["a7"]), "이 ", a7, "로 바뀌게 되고,")
    st.write(st.session_state["b7"], "이 ", b7, "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 식을 풀어봅시다.")
    Q7_easy_Text = f"7. {a7} \u00F7 {b7} ="
    st.markdown(Q7_easy_Text)
    answer3 = st.number_input("답 : ", key="3", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="c", on_click=make3, disabled=st.session_state["B24"]): 
        if float(answer3) == float(st.session_state["x7"]):
            st.session_state["N7"] = False
            st.write("정답입니다. 처음 문제를 방금 푼 자연수끼리의 나눗셈으로 바꾸듯이 자연수를 소수로 나누는 나눗셈은 자연수와 소수를 모두 소수점 이동하여 자연수끼리의 나눗셈으로 만들어 풀면 됩니다.")
        else:
            st.session_state["Q7"] = st.session_state["Q7"] + 1


if st.session_state["Q7"] == 3:
    st.session_state["N7"] = False
    st.write("오답입니다. 자연수끼리의 나눗셈에도 어려움이 있거나 계산 실수가 있는 것 같네요. 일단 다음 문제를 이어서 풀어봅시다.")

st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N7"]):
    switch_page("Q8")