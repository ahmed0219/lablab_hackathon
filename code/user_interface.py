import streamlit as st
from fn import generate_response

def chat_app():
    st.markdown("<header style='text-align: center; margin-bottom:30px; font-size: 0.8em;'>Powered by Neuralshield</header>", unsafe_allow_html=True)
    

    col1, col2, col3 = st.columns(3)

    # Apply centered-container style to the whole app
    st.markdown("<div style='display: flex; align-items: center; justify-content: center;'>", unsafe_allow_html=True)

    with col2:
        image_path = "../ASSETS/new.png"
        st.image(image_path, caption='')

    # Text below the image
    st.markdown("<p style='text-align: center; font-size:20px;'>How can I help you today?</p>", unsafe_allow_html=True)

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message['role'], avatar=message['avatar']):
            st.markdown(message['content'])

  
    if prompt := st.chat_input(""):
        # Add user message to chat history

        # Display user message in chat message container
        with st.chat_message("user",avatar="../ASSETS/a.png"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt,"avatar":"../ASSETS/a.png"})

        # Display assistant response in chat message container
        with st.chat_message("assistant", avatar="../ASSETS/log.png"):
            message_placeholder=st.empty()
            response = generate_response(prompt)
            message_placeholder.markdown(response['response'])
            st.session_state.messages.append({"role": "assistant", "content": response['response'],"avatar":"../ASSETS/log.png"})
            print(response['show'])

            # Scroll to the bottom
            st.markdown("<script>document.getElementById('root').scrollIntoView({behavior: 'smooth', block: 'end'});</script>", unsafe_allow_html=True)

    # Close the centered-container div
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    chat_app()
