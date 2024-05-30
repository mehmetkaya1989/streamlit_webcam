import cv2
import streamlit as st
import numpy as np
import tempfile

cap = cv2.VideoCapture(0)

st.title("Opem cv Deneme")

frame_placeholder = st.empty()
stop_button = st.button("Stop")

st.title("Video Yakalama")

while cap.isOpened() and not stop_button:
    ret, frame = cap.read()
    if not ret:
        st.write("the video capture has ended.")
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame, 1)

    frame_placeholder.image(frame,channels="RGB")

    if cv2.waitKey(1) % 0xFF == ord ("q") or stop_button:
        break

cap.release()


