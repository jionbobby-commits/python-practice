import streamlit as st

st.title("银灰长发少女 · 静谧的午后")
st.subheader("2026-10-22 12:54 内容来源于网络请勿转载")
st.header("银发少女的午后时光")
st.image("./file/01.jpg")
st.write("简短描述：")
st.write("银灰色长发、清透的绿色眼眸与深色格纹短裙，在柔和的窗边光影中交织出一幅细腻而静谧的日系动漫插画。")

st.logo("./file/logo.png")

mail = st.text_input("您的邮箱为？")

sex = st.radio("您的性别为？",["男","女","其他"])