import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd


Q9_Text = f'9. {st.session_state["a9"]} \u00F7 {st.session_state["b9"]}의 몫을 어림하여 다음 중에서 고르시오.'
st.subheader(Q9_Text)
answer1 = st.radio("답 : ", [st.session_state["y9-1"], st.session_state["y9-2"], int(st.session_state["y9-3"])], key="1")

if "N9" not in st.session_state:
    st.session_state["N9"] = True

if "B29" not in st.session_state:
    st.session_state["B29"] = False
if "B30" not in st.session_state:
    st.session_state["B30"] = False

def make1():
    st.session_state["B29"] = True
def make2():
    st.session_state["B30"] = True

st.write("이번 문제는 객관식이라 계산 실수 체크를 하지 않으니 주의해주세요.")
if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B29"]):
    if answer1 == None:
        answer1 = 0
    if float(answer1) == float(st.session_state["x9"]):
        st.session_state["C9"] = st.session_state["C9"] + 1
        st.session_state["N9"] = False
        st.write("정답입니다.")
    else:
        st.session_state["Q9"] = st.session_state["Q9"] + 2


if st.session_state["Q9"] == 2:
    st.write("몫을 어림하여 주어진 답을 고르는 데 어려움이 있는 것 같네요.")
    st.write("이번에는 어림이기 때문에 주어진 소수를 계산하기 쉬운 자연수로 바꿔서 계산해보겠습니다.")
    st.write("그렇게 되면 ", st.session_state["a9"], "이 ", int(st.session_state["a9_2"]), "로 바뀌게 되고,")
    st.write(st.session_state["b9"], "은 ", int(st.session_state["b9_2"]), "로 바뀌게 됩니다.")
    st.write("핵심은 정확히 계산하는 것이 아니라 대략적으로 제시된 답 중에 가까운 것만 찾으면 된다는 것입니다. 이 점에 주의하며 다음 문제를 다시 풀어봅시다.")
    Q9_easy_Text = f'9. {int(st.session_state["a9_2"])} \u00F7 {int(st.session_state["b9_2"])}의 몫을 어림하여 다음 중에서 가장 가까운 값을 고르시오.'
    st.markdown(Q9_easy_Text)
    answer2 = st.radio("답 : ", [st.session_state["y9-1"], st.session_state["y9-2"], int(st.session_state["y9-3"])], key="2")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B30"]):     
        if answer2 == None:
            answer2 = 0
        if float(answer2) == float(st.session_state["x9"]):
            st.session_state["N9"] = False
            st.write("정답입니다. 이렇게 계산하기 쉬운 자연수로 바꿔서 대략적으로 가까운 답만 골라서 계산하면 된답니다.")
        else:
            st.session_state["Q9"] = st.session_state["Q9"] + 1
            st.session_state["N9"] = False
            st.write("오답입니다. 계산하기 쉬운 자연수로 바꿔서 어림하는 방법을 아직 잘 이해하지 못했네요. 일단 다음 문제로 넘어갑시다.")
       
st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N9"]):
    switch_page("Q10")
