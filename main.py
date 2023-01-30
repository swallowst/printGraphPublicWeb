import streamlit as st
import webbrowser
import streamlit.components.v1 as components
def redirect(_url):
    link = ''
    st.markdown(link, unsafe_allow_html=True)
st.title("PrintGraph紹介サイト")
st.subheader("コードがわかるグラフ作成ツール")
start=st.button('START')
st.caption('アプリケーションを開始します．')
col = st.columns(6)
proposal = col[0].button('企画書')
col[0].caption('アプリ開発の目的，構想，詳細などの情報がまとめられています．')
method = col[2].button('紹介動画')
col[2].caption('アプリの使い方についての説明動画です．')
git = col[4].button('Github')
col[4].caption('アプリのプログラムです．')
manual = col[5].button("マニュアル")
col[5].caption("使い方のマニュアルです．")

if start:
    webbrowser.open("https://dancing-clafoutis-499aab.netlify.app/")
if proposal:
    webbrowser.open('https://drive.google.com/file/d/119abdlHGUJ9PqECeyT7Aitc5JGY-qy-5/view?usp=sharing')
if method:
    webbrowser.open("https://youtu.be/_4r3IcXitPw")
if git:
    webbrowser.open('https://github.com/azuma-naoki/PriGraph')
if manual:
    webbrowser.open("https://drive.google.com/file/d/1B5Z_DaZXv7rHu_aVev9Db8xOAVSRgXYC/view?usp=sharing")


components.html(
    """    
    <iframe width="560" height="315" src="https://www.youtube.com/embed/_4r3IcXitPw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>    
    """
    ,height=560,width=615
)
st.subheader('メンバー')
st.write('東直樹')
st.write('土岐田力輝')
st.write('佐子柊人')