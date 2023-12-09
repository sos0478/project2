import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

Q13_Text = f'13. {st.session_state["a13"]} \u00F7 {st.session_state["b13"]}의 {st.session_state["y13"]}.'
st.title(Q13_Text)
answer1 = st.number_input("답 : ", key="1")
st.session_state["N13"] = True

if "B46" not in st.session_state:
    st.session_state["B46"] = False
if "B47" not in st.session_state:
    st.session_state["B47"] = False
if "B48" not in st.session_state:
    st.session_state["B48"] = False
if "B49" not in st.session_state:
    st.session_state["B49"] = False
if "B50" not in st.session_state:
    st.session_state["B50"] = False
if "B51" not in st.session_state:
    st.session_state["B51"] = False


def make1():
    st.session_state["B46"] = True
def make2():
    st.session_state["B47"] = True
def make3():
    st.session_state["B48"] = True
def make4():
    st.session_state["B49"] = True
def make5():
    st.session_state["B50"] = True
def make6():
    st.session_state["B51"] = True


if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B46"]):
    if float(answer1) == float(st.session_state["x13"]):
        st.session_state["C13"] = st.session_state["C13"] + 1
        st.session_state["N13"] = False
        st.write("정답입니다.")
    else:
        st.session_state["Q13"] = st.session_state["Q13"] + 1


if st.session_state["Q13"] == 1:
    st.write("혹시 계산 실수가 있었나요? 몫이 아니라 나머지를 구해야 한다는 것을 생각하고 다시 답을 입력해주세요.")
    answer2 = st.number_input("답 : ", key="2")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B47"]):     
        if float(answer2) == float(st.session_state["x13"]):
            st.session_state["C13"] = st.session_state["C13"] + 1
            st.session_state["N13"] = False
            st.write("정답입니다.")
        else:
            st.session_state["Q13"] = st.session_state["Q13"] + 1
       

if st.session_state["Q13"] == 2.1:  
    st.write("나머지를 구하는 데 어려움이 있는 것 같군요.")
    st.write("이전처럼 소수의 나눗셈을 자연수로 바꾸면 몫은 유지되지만 나머지는 바뀌기 때문에 다른 방법으로 접근해봅시다.")
    st.write("우선 몫을 자연수 부분까지만 구한 후 답을 입력해봅시다.")
    Q13_easy_Text = f"13. {st.session_state['a13']} \u00F7 {st.session_state['b13']}의 몫을 자연수 부분까지 구해보시오."
    st.markdown(Q13_easy_Text)
    answer3 = st.number_input("답 : ", key="3")
    right_answer = st.session_state["y13_2"]
    if st.button("채점하기", key="c", on_click=make3, disabled=st.session_state["B48"]): 
        if int(answer3) == int(right_answer):
            st.write("정답입니다.")
            st.session_state["Q13"] = st.session_state["Q13"] + 0.4
        else:
            st.session_state["Q13"] = st.session_state["Q13"] + 1


if st.session_state["Q13"] == 2.5:
    st.write("그럼 이제 몫의 자연수 부분을 이용하여 나머지를 구해봅시다.")
    st.write("방금 입력한 몫의 자연수 부분인 ", int(right_answer), "를 나누는 수인 ", st.session_state['b13'], "에 곱해서 나누어지는 수인 ", st.session_state['a13'], "에서 빼주면 됩니다.")
    st.write(Q13_Text)
    answer4 = st.number_input("답 : ", key="4")
    if st.button("채점하기", key="d", on_click=make4, disabled=st.session_state["B49"]): 
        if float(answer4) == float(st.session_state["x13"]):
            st.session_state["N13"] = False
            st.write("정답입니다. 나머지는 이렇게 자연수 부분까지 몫을 구한 후 나누는 수에 곱해서 나누어지는 수에서 빼는 식으로 구할 수 있습니다.")
            st.write("하지만 더 쉬운 방법으로는 자연수 부분까지 몫을 구하는 과정을 세로셈으로 똑같이 한 후, 나누어지는 수의 소수점을 그대로 내려서 구한 나머지에 소수점을 찍어도 됩니다.")
            st.write("이 사실을 기억하면서 다음 문제로 넘어가도록 합시다.")
            st.session_state["Q13"] = st.session_state["Q13"] - 0.5
        else:
            st.session_state["N13"] = False
            st.write("오답입니다. 나머지를 구하는 방식을 이해하지 못하거나 계산 실수가 있었군요.")
            st.write("7을 2로 나누고 남은 나머지를 구할 때 7에서 몫인 3에 2를 곱한 후 빼주듯이")
            st.write(st.session_state['a13'], "에서 ", int(right_answer), "에 ", st.session_state['b13'], "를 곱하면 ", st.session_state['x13'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 놓쳤는지 확인하고 다음 문제로 넘어가도록 합시다.")


if st.session_state["Q13"] == 3.1:  
    st.write("소수의 나눗셈에서 몫을 자연수 부분을 나누는 방법에도 어려움이 있는 것 같군요. 몫의 자연수 부분까지만 구하는 것은 자연수의 나눗셈으로 바꾸어서 계산해도 괜찮습니다.")
    a13 = int(st.session_state["a13"]*10)
    b13 = int(st.session_state["b13"]*10)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 몫은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("주의할 점은 나누어지는 수는 이미 자연수라도 나누는 수를 자연수로 만들기 위해 같은 수를 꼭 곱해줘야 한다는 것입니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 10을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", st.session_state["a13"], "이 ", a13, "로 바뀌게 되고,")
    st.write(st.session_state["b13"], "이 ", b13, "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 후 몫을 자연수 부분까지 구한 후 답을 입력해봅시다.")
    Q13_easy_Text_2 = f"13. {a13} \u00F7 {b13}의 몫을 자연수 부분까지 구해보시오."
    st.markdown(Q13_easy_Text_2)
    answer5 = st.number_input("답 : ", key="5")
    if st.button("채점하기", key="e", on_click=make5, disabled=st.session_state["B50"]): 
        if int(answer5) == int(right_answer):
            st.write("정답입니다.")
            st.session_state["Q13"] = st.session_state["Q13"] + 0.4
        else:
            st.session_state["Q13"] = st.session_state["Q13"] + 0.9

if st.session_state["Q13"] == 3.5:
    st.write("그럼 이제 몫의 자연수 부분을 이용하여 나머지를 구해봅시다. 나머지를 구할 때는 몫의 자연수 부분을 구하느라 자연수로 바꾸었던 숫자를 다시 소수로 돌려놓고 생각해야 합니다.")
    st.write("방금 입력한 몫의 자연수 부분인 ", int(right_answer), "를 나누는 수인 ", st.session_state['b13'], "에 곱해서 나누어지는 수인 ", st.session_state['a13'], "에서 빼주면 됩니다.")
    st.write(Q13_Text)
    answer6 = st.number_input("답 : ", key="6")
    if st.button("채점하기", key="f", on_click=make6, disabled=st.session_state["B51"]): 
        if float(answer4) == float(st.session_state["x13"]):
            st.session_state["N13"] = False
            st.write("정답입니다. 나머지는 이렇게 자연수 부분까지 몫을 구한 후 나누는 수에 곱해서 나누어지는 수에서 빼는 식으로 구할 수 있습니다.")
            st.write("하지만 더 쉬운 방법으로는 자연수 부분까지 몫을 구하는 과정을 세로셈으로 똑같이 한 후, 나누어지는 수의 소수점을 그대로 내려서 구한 나머지에 소수점을 찍어도 됩니다.")
            st.write("이 사실을 기억하면서 다음 문제로 넘어가도록 합시다.")
            st.session_state["Q13"] = st.session_state["Q13"] - 0.5
        else:
            st.session_state["N13"] = False
            st.write("오답입니다. 나머지를 구하는 방식을 이해하지 못하거나 계산 실수가 있었군요.")
            st.write("7을 2로 나누고 남은 나머지를 구할 때 7에서 몫인 3에 2를 곱한 후 빼주듯이")
            st.write(st.session_state['a13'], "에서 ", int(right_answer), "에 ", st.session_state['b13'], "를 곱한 후 빼주면 ", st.session_state['x13'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 놓쳤는지 확인하고 다음 문제로 넘어가도록 합시다.")

if st.session_state["Q13"] == 4:
    st.session_state["N13"] = False
    st.write("오답입니다. 소수의 나눗셈과 나머지를 구하는 것에 모두 어려움이 있었군요.")
    st.write("그래도 나머지를 구하는 방법에 대해서는 다시 설명하겠습니다.")    
    st.write("위에서 풀지 못한 문제의 답을 이용해 나머지를 구하는 과정을 살펴봅시다.")
    st.write(f"{a13} \u00F7 {b13}의 몫을 자연수 부분까지 구하면 답은 {int(right_answer)}가 됩니다.")
    st.write("7을 2로 나누고 남은 나머지를 구할 때 7에서 몫인 3에 2를 곱한 후 빼주듯이")
    st.write(st.session_state['a13'], "에서 ", int(right_answer), "에 ", st.session_state['b13'], "를 곱한 후 빼주면 ", st.session_state['x13'], "이 된답니다.")
    st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 잘 몰랐는지 확인하고 다음 문제로 넘어가도록 합시다.")


st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N13"]):
    switch_page("Q14")
