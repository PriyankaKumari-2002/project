import json
import numpy as np
import av
import requests
import traceback
from streamlit_lottie import st_lottie
#streamlit for deploying the model locally 
import streamlit as st
from PIL import Image
from retinaface.pulse_retina import PulseMonitor
from annotated_text import annotated_text
from streamlit_webrtc import ClientSettings, VideoTransformerBase, WebRtcMode, webrtc_streamer


def main():
    st.set_page_config(page_title="microPULSEage", page_icon="microPULSEage.png",initial_sidebar_state="collapsed")
     #st.image("./assets/favicon.png")
    #st.image("\Engage Facerec Pulse Monitor\Pulse-master\\assets\\favicon.png")
    #st.image("\Engage Facerec Pulse Monitor\microPULSEage.png")
    #st.title("   microPULSEage  ")
    st.markdown("<h3 style='text-align:center; color: darkblue;'><b>Heart Rate Monitor System using face recognition</b></h3>", unsafe_allow_html=True)
    #opening the image

    image = Image.open('microPULSEage.png')
    #st.image(image, width=400, use_column_width=900)
    col1, col2, col3 = st.columns(3)

    with col1:
     st.write(' ')

    with col2:
     st.image(image, width=230, use_column_width=900)

    with col3:
     st.write(' ')
    st.markdown("<h5 style='text-align: center; color: black;'> >> Extraction of heart rate optically using flash of camera and face recognition!!</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'> >> Generation of web based electrocardiogram for graphical visualization(ECG)!!</h5>", unsafe_allow_html=True)
    #annotated_text(("In addition , generation of web based", "#8ef"))
    #st.markdown("<img src="https://www.tutorialspoint.com/html/images/test.png" alt="Simply Easy Learning" width="200" height="80">",unsafe_allow_html=True )
    #st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtJK4ZP4-IPT1B9AHb2v-leh6fa5vULTQd0w&usqp=CAU")
    st.markdown("<style> .reportview-container .main footer {visibility: hidden;} #MainMenu {visibility: hidden;}     </style>", unsafe_allow_html=True)
    get_pulsemonitor_frames()
    
    #annotated_text(("This feature will help to diagnose critical diseases...Some of them are:"))
    st.markdown("<h5 style='text-align: center; color: black;'> *** This feature will help to diagnose critical diseases ***...Some of them are:</h5>", unsafe_allow_html=True)
    annotated_text((" >> Coronary artery disease ", "#FFFF00"))
    st.markdown("<h6 <br> </h6>", unsafe_allow_html=True)
    annotated_text((" >> Heart Attack ", "#00FF00"))
    st.markdown("<h6 <br> </h6>", unsafe_allow_html=True)
    annotated_text((" >> Ventricular Tachycardia ", "#FFDF00"))
    st.markdown("<h6 <br> </h6>", unsafe_allow_html=True)
    annotated_text((" >> Cardiomyopathy (Where the heart walls becomes thickened or enlarged) ", "#FFA500"))
    st.markdown("<h6 <br> </h6>", unsafe_allow_html=True)
    annotated_text((" >> Atrial Fibrillation/Asthma --(People with asthma could be at 1.5 times higher risk of developing atrial fibrillation) ", "#728C00"))
    st.markdown("<h6 <br> </h6>", unsafe_allow_html=True)
    annotated_text((" >> COPD (Chronic Obstructive Pulmonary Disease) ", "#A52A2A"))
    st.markdown("<h6 <br> </h6>", unsafe_allow_html=True)
    annotated_text((" >> Arrhythmias ", "#F70D1A"))
    st.markdown("<h6 <br> </h6>", unsafe_allow_html=True)
    annotated_text((" >> Pneumonia --(it can push heart into abnormal fast rhythms) ", "#808000"))
    
    st.markdown("<h5 style='text-align: center; color: black;'> <br> <br> <b> <h4>Hope this helped :))</h4> </b> Check Pulse Rate Regularly using microPULSEage at your own comfort and cost free to detect heart diseases at early stage!!</h4>", unsafe_allow_html=True)
#st.markdown("<h5 style='text-align: center; color: black;'> Hope you liked it :)) <br> Check your Pulse Rate Regularly using microPULSEage at your own comfort and cost free!!</h5>", unsafe_allow_html=True)


def app_loopback():
    """ Simple video loopback """
    webrtc_streamer(
        key="loopback",
        mode=WebRtcMode.SENDRECV,
        client_settings=WEBRTC_CLIENT_SETTINGS,
        video_processor_factory=None,  # NoOp
    )


def get_pulsemonitor_frames():

    class NNVideoTransformer(VideoTransformerBase):

        def __init__(self) -> None:
            self.processor = PulseMonitor()

        def transform(self, frame: av.VideoFrame) -> np.ndarray:
            try:
                image = frame.to_ndarray(format="bgr24")
                annotated_image, current_bpm = self.processor.process_frame(image)
                return annotated_image
            except Exception as e:
                print("Caught Exception")
                traceback.print_exc()
                return image
    
    webrtc_ctx = webrtc_streamer(key="loopback", mode=WebRtcMode.SENDRECV, client_settings=WEBRTC_CLIENT_SETTINGS,
     video_processor_factory=NNVideoTransformer, async_processing=True,)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_W5Sk67.json")




WEBRTC_CLIENT_SETTINGS = ClientSettings(
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)


if __name__ == "__main__":
    main()