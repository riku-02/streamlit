import streamlit as st
from pytube import YouTube
import datetime
from moviepy.editor import *
import os

filePath = ''

url = st.text_input(label='URL: ')

convert = st.button('Convert')

if convert:
    yti = YouTube(url)
    st.subheader(yti.title)
    st.image(yti.thumbnail_url, width=200)
    sec = yti.length
    res = datetime.timedelta(seconds=sec)
    st.text(f'Duration: {res} ')

    with st.spinner('Converting...'):
        yt = YouTube(url)

        yt.streams.filter(only_audio=True)
        stream = yt.streams.get_by_itag(140)

        freshDownload = stream.download(filePath)

        basePath, extension = os.path.splitext(freshDownload)

        video = AudioFileClip(os.path.join(basePath + ".mp4"))
        video.write_audiofile(os.path.join(basePath + ".mp3"))

        with open(os.path.join(basePath + ".mp3"), 'rb') as f:
            st.success('Success!')
            st.download_button('Download', f, file_name=yt.title + '.mp3')
