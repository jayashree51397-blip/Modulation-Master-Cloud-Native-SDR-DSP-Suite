import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.fft import fft, fftfreq
from scipy.signal import butter, lfilter

# --- GNU RADIO ENGINE ---
def gnuradio_lpf_block(data, cutoff_freq, sampling_rate, order=5):
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, data)

st.set_page_config(page_title="Modulation Master", layout="wide")
st.title("📡 Jayashree's Adv Communication Lab")

# --- SIDEBAR ---
st.sidebar.header("Control Panel")
unit_choice = st.sidebar.radio("Select Syllabus Unit", 
    ["Analog (Unit I & II)", "Digital (Unit IV)", "GNU Radio DSP (Advanced)"])

# --- SHARED PARAMETERS ---
fc = st.sidebar.slider("Carrier Frequency (Hz)", 20, 200, 100)
noise_level = st.sidebar.slider("Channel Noise", 0.0, 2.0, 0.1)

t = np.linspace(0, 1, 1000)
carrier = np.cos(2 * np.pi * fc * t)

# --- LOGIC SEPARATION ---
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

elif unit_choice == "Digital (Unit IV)":
    st.sidebar.info("Binary Data: [1, 0, 1, 1, 0]")
    message = np.repeat([1, -1, 1, 1, -1], 200) 
    modulated = message * carrier

else: # GNU RADIO DSP (ADVANCED)
    st.sidebar.info("GNU Radio Mode Active")
    # Using a default BPSK signal for the DSP demo
    message = np.repeat([1, -1, 1, 1, -1], 200)
    modulated = message * carrier

# Add Noise to whatever signal was generated
modulated += np.random.normal(0, noise_level, len(t))
# --- SNR CALCULATION (O-GRADE METRIC) ---
signal_power = np.mean(np.square(modulated - np.random.normal(0, noise_level, len(t)))) # Approximation
noise_power = np.mean(np.square(np.random.normal(0, noise_level, len(t))))

# Avoid division by zero
if noise_level > 0:
    snr_db = 10 * np.log10(signal_power / noise_power)
else:
    snr_db = 100 # Infinity for zero noise

# Display the metric at the top of the dashboard
st.sidebar.markdown("---")
st.sidebar.metric(label="Channel Quality (SNR)", value=f"{snr_db:.2f} dB", 
                  delta="Good" if snr_db > 10 else "Poor", delta_color="normal")

# --- PLOTTING ---
if unit_choice == "GNU Radio DSP (Advanced)":
    st.header("🛠️ GNU Radio Receiver Pipeline")
    st.info("Simulated Flowgraph: Noisy Input → LPF Block → Recovered Signal")
    
    cutoff = st.slider("Filter Cutoff Frequency (Hz)", 5, 80, 30)
    recovered = gnuradio_lpf_block(modulated, cutoff, 1000)

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Time Domain: Before vs After")
        fig_rec = go.Figure()
        fig_rec.add_trace(go.Scatter(y=modulated[:300], name="Noisy Channel", line=dict(color='red', width=1)))
        fig_rec.add_trace(go.Scatter(y=recovered[:300], name="GNU Radio Output", line=dict(color='green', width=2)))
        st.plotly_chart(fig_rec, use_container_width=True)
        
    with col_b:
        st.subheader("Receiver Spectrum")
        yf_rec = fft(recovered)
        xf_rec = fftfreq(len(t), 1/1000)
        fig_spec = go.Figure()
        fig_spec.add_trace(go.Scatter(x=xf_rec[:500], y=np.abs(yf_rec[:500]), fill='tozeroy', name="Filtered Spectrum"))
        st.plotly_chart(fig_spec, use_container_width=True)

else:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Time Domain (Oscilloscope)")
        fig_time = go.Figure()
        fig_time.add_trace(go.Scatter(x=t, y=modulated, name="Signal"))
        st.plotly_chart(fig_time, use_container_width=True)

    with col2:
        if unit_choice == "Digital (Unit IV)":
            st.subheader("Constellation Diagram")
            fig_const = go.Figure()
            fig_const.add_trace(go.Scatter(x=message, y=[0]*len(t), mode='markers', name="Phase"))
            fig_const.update_xaxes(range=[-2, 2])
            st.plotly_chart(fig_const, use_container_width=True)
        else:
            st.subheader("Spectrum Analyzer")
            yf = fft(modulated)
            xf = fftfreq(len(t), 1/1000)
            fig_freq = go.Figure()
            fig_freq.add_trace(go.Scatter(x=xf[:500], y=np.abs(yf[:500]), fill='tozeroy'))
            st.plotly_chart(fig_freq, use_container_width=True)
