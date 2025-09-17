import streamlit as st
import time

# 초기 변수 설정
if 'running' not in st.session_state:
    st.session_state.running = False
    st.session_state.time_left = 0
    st.session_state.cnt = 0
    st.session_state.timer_over = False

# 타이머 시작 함수
def start_timer():
    st.session_state.time_left = 5  # 타이머 5초 설정
    st.session_state.cnt = 0  # 클릭 횟수 초기화
    st.session_state.running = True  # 타이머 동작 시작
    st.session_state.timer_over = False  # 타이머 종료 상태 초기화

# 클릭 함수
def click():
    if st.session_state.running and st.session_state.time_left > 0:
        st.session_state.cnt += 1

# 타이머 업데이트 함수
def update_timer():
    if st.session_state.running and st.session_state.time_left > 0:
        st.session_state.time_left -= 1
        time.sleep(1)  # 1초 대기
    elif st.session_state.time_left == 0:
        st.session_state.running = False
        st.session_state.timer_over = True  # 타이머 종료

# 앱 실행
st.title("주어진 시간 동안 최대한 많이 클릭하세요!")

if st.session_state.running:
    timer_placeholder = st.empty()  # 타이머 값을 표시할 공간
    while st.session_state.time_left > 0:
        timer_placeholder.text(f"Time left: {st.session_state.time_left} seconds")
        update_timer()

    st.text(f"현재 횟수: {st.session_state.cnt}")

elif st.session_state.timer_over:
    st.text(f"최종 횟수: {st.session_state.cnt}")
    if st.button('Reset'):
        st.session_state.time_left = 0
        st.session_state.cnt = 0
        st.session_state.running = False
        st.session_state.timer_over = False
else:
    if st.button('Start Timer'):
        start_timer()

# 클릭 버튼
if st.session_state.running and st.session_state.time_left > 0:
    if st.button("Click Me!"):
        click()

