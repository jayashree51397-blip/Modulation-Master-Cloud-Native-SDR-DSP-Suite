mport streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.fft import fft, fftfreq

st.set_page_config(page_title="Modulation Master", layout="wide")
st.title("📡 Jayashree's Adv Communication Lab")

# --- SIDEBAR ---
st.sidebar.header("Control Panel")
unit_choice = st.sidebar.radio("Select Syllabus Unit", ["Analog (Unit I & II)", "Digital (Unit IV)"])

# --- SHARED PARAMETERS ---
fc = st.sidebar.slider("Carrier Frequency (Hz)", 20, 200, 100)
noise_level = st.sidebar.slider("Channel Noise", 0.0, 2.0, 0.1)

t = np.linspace(0, 1, 1000)
carrier = np.cos(2 * np.pi * fc * t)

if unit_choice == "Analog (Unit I & II)":
    mod_type = st.sidebar.selectbox("Type", ["Standard AM", "DSB-SC", "FM"])
    fm = st.sidebar.slider("Message Frequency", 1, 10, 5)
    message = np.cos(2 * np.pi * fm * t)
    
    if mod_type == "Standard AM":
        modulated = (1 + message) * carrier
    elif mod_type == "DSB-SC":
        modulated = message * carrier
    else:
        modulated = np.cos(2 * np.pi * fc * t + 5 * np.cumsum(message)/100)

else: # DIGITAL MODULATION (UNIT IV)
    st.sidebar.info("Binary Data: [1, 0, 1, 1, 0]")
    # Create a square wave message (Bits)
    message = np.repeat([1, -1, 1, 1, -1], 200) 
    # BPSK Formula: s(t) = b(t) * cos(2*pi*fc*t)
    modulated = message * carrier

# Add Noise
modulated += np.random.normal(0, noise_level, len(t))

# --- PLOTTING ---
col1, col2 = st.columns(2)
with col1:
    st.subheader("Time Domain (Oscilloscope)")
    fig_time = go.Figure()
    fig_time.add_trace(go.Scatter(x=t, y=modulated, name="Signal"))
    st.plotly_chart(fig_time, use_container_width=True)

with col2:
    st.subheader("Constellation Diagram (Unit IV Only)" if unit_choice == "Digital (Unit IV)" else "Spectrum Analyzer")
    if unit_choice == "Digital (Unit IV)":
        # Show Phase shifts
        fig_const = go.Figure()
        fig_const.add_trace(go.Scatter(x=message, y=[0]*len(t), mode='markers', name="Phase"))
        fig_const.update_xaxes(range=[-2, 2])
        st.plotly_chart(fig_const, use_container_width=True)
    else:
        yf = fft(modulated)
        xf = fftfreq(len(t), 1/1000)
        fig_freq = go.Figure()
        fig_freq.add_trace(go.Scatter(x=xf[:500], y=np.abs(yf[:500]), fill='tozeroy'))
        st.plotly_chart(fig_freq, use_container_width=True)
