import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd


Q10_Text = f'연습 10-1. {st.session_state["a10_p1"]} \u00F7 {st.session_state["b10_p1"]}의 몫을 어림하여 다음 중에서 고르시오.'
st.subheader(Q10_Text)
answer1 = st.radio("답 : ", [st.session_state["y10-1_p1"], st.session_state["y10-2_p1"], int(st.session_state["y10-3_p1"])], key="1")

if "B31_p1" not in st.session_state:
    st.session_state["B31_p1"] = False
if "B32_p1" not in st.session_state:
    st.session_state["B32_p1"] = False

def make1():
    st.session_state["B31_p1"] = True
def make2():
    st.session_state["B32_p1"] = True

st.write("이번 문제는 객관식이라 계산 실수 체크를 하지 않으니 주의해주세요.")
if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B31_p1"]):
    if answer1 == None:
        answer1 = 0
    if float(answer1) == float(st.session_state["x10_p1"]):
        st.write("정답입니다.")
    else:
        st.session_state["Q10_p1"] = st.session_state["Q10_p1"] + 2


if st.session_state["Q10_p1"] == 2:
    st.write("몫을 어림하여 주어진 답을 고르는 데 어려움이 있는 것 같네요.")
    st.write("이번에는 어림이기 때문에 주어진 소수를 계산하기 쉬운 자연수로 바꿔서 계산해보겠습니다.")
    st.write("그런데 나누는 숫자가 1보다 작은 숫자라서 계산하기 쉬운 자연수로 바꾸는게 의미가 없겠군요.")
    st.write("이럴 땐 우선 자연수의 나눗셈으로 바꿔봅시다.")
    st.write("그렇게 되면 ", st.session_state["a10_p1"], "이 ", int(st.session_state["a10_2_p1"]), "로 바뀌게 되고,")
    st.write(st.session_state["b10_p1"], "은 ", int(st.session_state["b10_2_p1"]), "로 바뀌게 됩니다.")
    st.write("그 후에 다시 이 숫자들을 계산하기 쉬운 자연수로 바꿔서 계산하면 됩니다.")
    st.write("그렇게 되면 ", int(st.session_state["a10_2_p1"]), "이 ", int(st.session_state["a10_3_p1"]), "로 바뀌게 되고,")
    st.write(int(st.session_state["b10_2_p1"]), "은 ", int(st.session_state["b10_3_p1"]), "로 바뀌게 됩니다.")    
    st.write("핵심은 정확히 계산하는 것이 아니라 대략적으로 제시된 답 중에 가까운 것만 찾으면 된다는 것입니다. 이 점에 주의하며 다음 문제를 다시 풀어봅시다.")
    Q10_easy_Text = f'연습 10-1. {int(st.session_state["a10_3_p1"])} \u00F7 {int(st.session_state["b10_3_p1"])}의 몫을 어림하여 다음 중에서 가장 가까운 값을 고르시오.'
    st.markdown(Q10_easy_Text)
    answer2 = st.radio("답 : ", [st.session_state["y10-1_p1"], st.session_state["y10-2_p1"], int(st.session_state["y10-3_p1"])], key="2")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B32_p1"]):     
        if answer2 == None:
            answer2 = 0
        if float(answer2) == float(st.session_state["x10_p1"]):
            st.write("정답입니다. 이렇게 비슷한 자연수로 바꿔서 대략적으로 가까운 답만 골라서 계산하면 된답니다.")
        else:
            st.session_state["Q10_p1"] = st.session_state["Q10_p1"] + 1
            st.write("오답입니다. 비슷한 자연수로 바꿔서 어림하는 방법을 아직 잘 이해하지 못했네요. 더 연습해봅시다.")
       
Q10_Text_p2 = f'연습 10-2. {st.session_state["a10_p2"]} \u00F7 {st.session_state["b10_p2"]}의 몫을 어림하여 다음 중에서 고르시오.'
st.subheader(Q10_Text_p2)
answer1_p2 = st.radio("답 : ", [st.session_state["y10-1_p2"], st.session_state["y10-2_p2"], int(st.session_state["y10-3_p2"])], key="1_p2")

if "B31_p2" not in st.session_state:
    st.session_state["B31_p2"] = False
if "B32_p2" not in st.session_state:
    st.session_state["B32_p2"] = False

def make1_p2():
    st.session_state["B31_p2"] = True
def make2_p2():
    st.session_state["B32_p2"] = True

st.write("이번 문제는 객관식이라 계산 실수 체크를 하지 않으니 주의해주세요.")
if st.button("채점하기", key="a_p2", on_click=make1_p2, disabled=st.session_state["B31_p2"]):
    if answer1_p2 == None:
        answer1_p2 = 0
    if float(answer1_p2) == float(st.session_state["x10_p2"]):
        st.write("정답입니다.")
    else:
        st.session_state["Q10_p2"] = st.session_state["Q10_p2"] + 2


if st.session_state["Q10_p2"] == 2:
    st.write("몫을 어림하여 주어진 답을 고르는 데 어려움이 있는 것 같네요.")
    st.write("이번에는 어림이기 때문에 주어진 소수를 계산하기 쉬운 자연수로 바꿔서 계산해보겠습니다.")
    st.write("그런데 나누는 숫자가 1보다 작은 숫자라서 계산하기 쉬운 자연수로 바꾸는게 의미가 없겠군요.")
    st.write("이럴 땐 우선 자연수의 나눗셈으로 바꿔봅시다.")
    st.write("그렇게 되면 ", st.session_state["a10_p2"], "이 ", int(st.session_state["a10_2_p2"]), "로 바뀌게 되고,")
    st.write(st.session_state["b10_p2"], "은 ", int(st.session_state["b10_2_p2"]), "로 바뀌게 됩니다.")
    st.write("그 후에 다시 이 숫자들을 계산하기 쉬운 자연수로 바꿔서 계산하면 됩니다.")
    st.write("그렇게 되면 ", int(st.session_state["a10_2_p2"]), "이 ", int(st.session_state["a10_3_p2"]), "로 바뀌게 되고,")
    st.write(int(st.session_state["b10_2_p2"]), "은 ", int(st.session_state["b10_3_p2"]), "로 바뀌게 됩니다.")    
    st.write("핵심은 정확히 계산하는 것이 아니라 대략적으로 제시된 답 중에 가까운 것만 찾으면 된다는 것입니다. 이 점에 주의하며 다음 문제를 다시 풀어봅시다.")
    Q10_easy_Text_p2 = f'연습 10-2. {int(st.session_state["a10_3_p2"])} \u00F7 {int(st.session_state["b10_3_p2"])}의 몫을 어림하여 다음 중에서 가장 가까운 값을 고르시오.'
    st.markdown(Q10_easy_Text_p2)
    answer2_p2 = st.radio("답 : ", [st.session_state["y10-1_p2"], st.session_state["y10-2_p2"], int(st.session_state["y10-3_p2"])], key="2_p2")
    if st.button("채점하기", key="b_p2", on_click=make2_p2, disabled=st.session_state["B32_p2"]):  
        if answer2_p2 == None:
            answer2_p2 = 0   
        if float(answer2_p2) == float(st.session_state["x10_p2"]):
            st.write("정답입니다. 이렇게 비슷한 자연수로 바꿔서 대략적으로 가까운 답만 골라서 계산하면 된답니다.")
        else:
            st.session_state["Q10_p2"] = st.session_state["Q10_p2"] + 1
            st.write("오답입니다. 비슷한 자연수로 바꿔서 어림하는 방법을 아직 잘 이해하지 못했네요. 더 연습해봅시다.")

practice = st.selectbox('연습하고 싶은 문제를 골라주세요.', st.session_state["R_Q_list"])
if st.button('연습 문제로 이동하기'):
    if practice == "1번":
        switch_page("Q1-P")
    elif practice == "2번":
        switch_page("Q2-P")
    elif practice == "3번":
        switch_page("Q3-P")
    elif practice == "4번":
        switch_page("Q4-P")
    elif practice == "5번":
        switch_page("Q5-P")
    elif practice == "6번":
        switch_page("Q6-P")
    elif practice == "7번":
        switch_page("Q7-P")
    elif practice == "8번":
        switch_page("Q8-P")
    elif practice == "9번":
        switch_page("Q9-P")
    elif practice == "10번":
        switch_page("Q10-P")
    elif practice == "11번":
        switch_page("Q11-P")
    elif practice == "12번":
        switch_page("Q12-P")
    elif practice == "13번":
        switch_page("Q13-P")
    elif practice == "14번":
        switch_page("Q14-P")

if st.button('분석 화면으로 돌아가기'):
    switch_page("Review")