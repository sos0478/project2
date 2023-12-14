import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

Q12_Text = f'12. {st.session_state["a12"]} \u00F7 {st.session_state["b12"]}의 {st.session_state["y12"]}하시오.'
st.subheader(Q12_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")

if "right_answer4" not in st.session_state:
    st.session_state["right_answer4"] = 0
if "a12__" not in st.session_state:
    st.session_state["a12__"] = 0
if "b12__" not in st.session_state:
    st.session_state["b12__"] = 0



if "N12" not in st.session_state:
    st.session_state["N12"] = True
if "N12-UP" not in st.session_state:
    st.session_state["N12-UP"] = True

if "B39" not in st.session_state:
    st.session_state["B39"] = False
if "B40" not in st.session_state:
    st.session_state["B40"] = False
if "B41" not in st.session_state:
    st.session_state["B41"] = False
if "B42" not in st.session_state:
    st.session_state["B42"] = False
if "B43" not in st.session_state:
    st.session_state["B43"] = False
if "B44" not in st.session_state:
    st.session_state["B44"] = False


def make1():
    st.session_state["B39"] = True
def make2():
    st.session_state["B40"] = True
def make3():
    st.session_state["B41"] = True
def make4():
    st.session_state["B42"] = True
def make5():
    st.session_state["B43"] = True
def make6():
    st.session_state["B44"] = True

if "round_q2" not in st.session_state:
    st.session_state["round_q2"] = 0

if st.session_state['y12_2'] == "소수 첫째 자리":
    st.session_state["round_q2"] = 1
elif st.session_state['y12_2'] == "소수 둘째 자리":
    st.session_state["round_q2"] = 2


if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B39"]):
    if answer1 == None:
        answer1 = 0
    if float(answer1) == float(st.session_state["x12"]):
        st.session_state["C12"] = st.session_state["C12"] + 1
        st.session_state["N12"] = False
        st.write("정답입니다.")
    else:
        st.session_state["Q12"] = st.session_state["Q12"] + 1


if st.session_state["Q12"] == 1:
    st.write("혹시 계산 실수가 있었나요? 반올림을 해야 한다는 것을 생각하고 다시 답을 입력해주세요.")
    answer2 = st.number_input("답 : ", key="2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B40"]):
        if answer2 == None:
            answer2 = 0     
        if float(answer2) == float(st.session_state["x12"]):
            st.session_state["C12"] = st.session_state["C12"] + 1
            st.session_state["N12"] = False
            st.write("정답입니다.")
        else:
            st.session_state["Q12"] = st.session_state["Q12"] + 1.1
       

if st.session_state["Q12"] == 2.1:  
    st.write("몫을 반올림하여 구하는 데 어려움이 있는 것 같군요.")
    st.write("우선 몫을", st.session_state['y12_2'], "까지 구한 후 답을 입력해봅시다.")
    Q12_easy_Text = f"12. {st.session_state['a12']} \u00F7 {st.session_state['b12']}의 몫을 {st.session_state['y12_2']}까지 구해보시오."
    st.markdown(Q12_easy_Text)
    answer3 = st.number_input("답 : ", key="3", value=None, placeholder="답을 입력하세요.", format="%f")
    st.session_state['right_answer4'] = float(st.session_state['a12']/st.session_state['b12'])
    st.session_state['right_answer4'] = f"{st.session_state['right_answer4']:.{st.session_state['round_q2']}f}"
    if st.button("채점하기", key="c", on_click=make3, disabled=st.session_state["B41"]): 
        if answer3 == None:
            answer3 = 0
        if float(answer3) == float(st.session_state['right_answer4']):
            st.write("정답입니다.")
            st.session_state["Q12"] = st.session_state["Q12"] + 0.4
        else:
            st.session_state["Q12"] = st.session_state["Q12"] + 1


if st.session_state["Q12"] == 2.5:
    st.write("그럼 이제 구한 값을 반올림해보겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("방금 입력한 ", st.session_state['right_answer4'], "를 ", st.session_state['y12_2'], "에서 반올림한 값을 입력해봅시다.")
    answer4 = st.number_input("답 : ", key="4", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="d", on_click=make4, disabled=st.session_state["B42"]): 
        if answer4 == None:
            answer4 = 0
        if float(answer4) == float(st.session_state["x12"]):
            st.session_state["N12"] = False
            st.write("정답입니다. 소수의 나눗셈에서 몫을 구하고 반올림을 할 수 있는데 2번이나 답을 틀린 것을 보니 반올림을 잘못 이해했거나 실수를 많이 한 것 같네요. 다음부터는 집중하여 문제를 풀도록 합시다.")
            st.session_state["Q12"] = st.session_state["Q12"] - 0.5
        else:
            st.session_state["N12"] = False
            st.write("오답입니다. 몫은 구할 수 있지만 반올림에 어려움이 있었군요.")
            st.write(st.session_state['right_answer4'], "를 ", st.session_state['y12_2'], "에서 반올림하면 ", st.session_state['x12'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 실수를 했는지 확인하고 다음 문제로 넘어가도록 합시다.")


if st.session_state["Q12"] == 3.1:  
    st.write("소수의 나눗셈 자체에 어려움이 있는 것 같군요. 그렇다면 자연수로 바꿔서 나눗셈을 진행해봅시다.")
    st.session_state['a12__'] = int(st.session_state["a12"]*100)
    st.session_state['b12__'] = int(st.session_state["b12"]*100)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 몫은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("주의할 점은 나누어지는 수는 이미 자연수라도 나누는 수를 자연수로 만들기 위해 같은 수를 꼭 곱해줘야 한다는 것입니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 100을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", st.session_state["a12"], "이 ", st.session_state['a12__'], "로 바뀌게 되고,")
    st.write(st.session_state["b12"], "이 ", st.session_state['b12__'], "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 후 몫을", st.session_state['y12_2'], "까지 구한 후 답을 입력해봅시다.")
    Q12_easy_Text_2 = f"12. {st.session_state['a12__']} \u00F7 {st.session_state['b12__']}의 {st.session_state['y12']}하시오."
    st.markdown(Q12_easy_Text_2)
    answer5 = st.number_input("답 : ", key="5", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="e", on_click=make5, disabled=st.session_state["B43"]): 
        if answer5 == None:
            answer5 = 0
        if float(answer5) == float(st.session_state['right_answer4']):
            st.write("정답입니다.")
            st.session_state["Q12"] = st.session_state["Q12"] + 0.4
        else:
            st.session_state["Q12"] = st.session_state["Q12"] + 0.9

if st.session_state["Q12"] == 3.5:
    st.write("그럼 이제 구한 값을 반올림해보겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("방금 입력한 ", st.session_state['right_answer4'], "를 ", st.session_state['y12_2'], "에서 반올림한 값을 입력해봅시다.")
    answer6 = st.number_input("답 : ", key="6", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="f", on_click=make6, disabled=st.session_state["B44"]): 
        if answer6 == None:
            answer6 = 0
        if float(answer6) == float(st.session_state["x12"]):
            st.session_state["N12"] = False
            st.write("정답입니다. 소수의 나눗셈에는 어려움이 있었지만 반올림에는 문제가 없었군요. 다음에는 자연수로 바꿔서 신중하게 계산해봅시다.")
            st.session_state["Q12"] = st.session_state["Q12"] - 0.5
        else:
            st.session_state["N12"] = False
            st.write("오답입니다. 소수의 나눗셈과 반올림에 모두 어려움이 있었군요.")
            st.write("그래도 반올림에 대해서는 다시 설명하겠습니다.")
            st.write(st.session_state['right_answer4'], "를 ", st.session_state['y12_2'], "에서 반올림하면 ", st.session_state['x12'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 실수를 했는지 확인하고 다음 문제로 넘어가도록 합시다.")

if st.session_state["Q12"] == 4:
    st.session_state["N12"] = False
    st.write("오답입니다. 소수의 나눗셈과 반올림에 모두 어려움이 있었군요.")
    st.write("그래도 반올림에 대해서는 다시 설명하겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("위에서 풀지 못한 문제의 답을 이용해 반올림 과정을 살펴봅시다.")
    st.write(f"{st.session_state['a12__']} \u00F7 {st.session_state['b12__']}의 {st.session_state['y12']}하면 답은 {st.session_state['right_answer4']}가 됩니다.")
    st.write("이때 ", st.session_state['right_answer4'], "를 ", st.session_state['y12_2'], "에서 반올림하면 ", st.session_state['x12'], "이 된답니다.")
    st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 잘 몰랐는지 확인하고 다음 문제로 넘어가도록 합시다.")


st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N12"]):
    switch_page("Q12")

if st.session_state["C11"] == 1 and st.session_state["C12"] == 1:
    st.session_state["N12-UP"] = False
    st.session_state["N12"] = True

st.write("11번 문제와 12번 문제를 성공적으로 풀었다면 고난도 문제에 도전할 수 있습니다.")
if st.button("고난도 문제 풀어보기", disabled=st.session_state["N12-UP"]):
    switch_page("Q12-UP")
