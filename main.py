import streamlit as st
import owo




def main():
    IMAGE_URL = "https://ahegao.b-cdn.net/wp-content/uploads/2021/04/Ijiranaide-Nagatoro-san-Episode-1-Nagatoro-Wipes-More-Senpai-Tears.jpg"
    key = st.secrets['API_KEY']

    st.header('Rikku.File Upload and Url Shortener')
    st.image(IMAGE_URL)

    st.subheader('Rikku.File Upload')
    uploaded_files = st.file_uploader("Upload a File", accept_multiple_files=True)

    btnUp = st.button('Upload')

    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        with open(f'{uploaded_file.name}', 'wb') as f: 
            f.write(bytes_data)
    
    if btnUp:           
        with st.spinner('Uploading...'):
            st.write(owo.upload_files(key, uploaded_file.name))
            st.success('File Uploaded.')
               

 
    
#####
    st.subheader('Rikku.URL Shortener')
    url = st.text_input('ex. https://...', '')
    btn = st.button('Shorten')
    req = 'https://'



    try:
        if req not in url:
            if btn:
                st.write(owo.shorten_urls(key, req + url))
        
        if url == '':
            if btn:
                st.write('Please input a URL')
            

    except ValueError:               
        st.write('Invalid URL, Please input "https://..."')
    
    

if __name__=='__main__':
  main()
     
