import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.fft import fft, fftfreq
from scipy.signal import butter, lfilter

# --- 1. THE GNU RADIO ENGINE (DSP FUNCTIONS) ---
def gnuradio_lpf_block(data, cutoff_freq, sampling_rate, order=5):
    """Mimics a GNU Radio Low Pass Filter Block"""
    nyquist = 0.5 * sampling_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, data)

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(page_title="Modulation Master", layout="wide")
st.title("📡 Jayashree's Advanced Communication Lab")
st.markdown("*A Cloud-Native SDR & Signal Processing Suite*")

# --- 3. SIDEBAR CONTROLS ---
st.sidebar.header("🕹️ Control Panel")
unit_choice = st.sidebar.radio("Select Syllabus Unit", 
    ["Analog (Unit I & II)", "Digital (Unit IV)", "GNU Radio DSP (Advanced)"])

st.sidebar.markdown("---")
fc = st.sidebar.slider("Carrier Frequency (Hz)", 20, 200, 100)
noise_level = st.sidebar.slider("Channel Noise (AWGN)", 0.0, 3.0, 0.1)

# Time Vector
t = np.linspace(0, 1, 1000)
fs = 1000 # Sampling Frequency
carrier = np.cos(2 * np.pi * fc * t)

# --- 4. SIGNAL GENERATION LOGIC ---
if unit_choice == "Analog (Unit I & II)":
    mod_type = st.sidebar.selectbox("Type", ["Standard AM", "DSB-SC", "FM"])
    fm = st.sidebar.slider("Message Frequency (Hz)", 1, 10, 5)
    message = np.cos(2 * np.pi * fm * t)
    
    if mod_type == "Standard AM":
        modulated = (1 + message) * carrier
    elif mod_type == "DSB-SC":
        modulated = message * carrier
    else: # FM
        modulated = np.cos(2 * np.pi * fc * t + 5 * np.cumsum(message)/fs)

elif unit_choice == "Digital (Unit IV)":
    st.sidebar.info("Sequence: [1, 0, 1, 1, 0]")
    # Generate BPSK Message
    message_bits = np.array([1, -1, 1, 1, -1])
    message = np.repeat(message_bits, 200) 
    modulated = message * carrier

else: # GNU RADIO DSP (ADVANCED)
    st.sidebar.info("GNU Radio Receiver Mode")
    # Using BPSK as the default test signal for DSP
    message_bits = np.array([1, -1, 1, 1, -1])
    message = np.repeat(message_bits, 200)
    modulated = message * carrier

# --- 5. CHANNEL SIMULATION (ADD NOISE) ---
noise = np.random.normal(0, noise_level, len(t))
noisy_signal = modulated + noise

# --- 6. O-GRADE METRICS (SNR & BER) ---
# Calculate SNR
sig_pwr = np.mean(np.square(modulated))
noise_pwr = np.mean(np.square(noise)) if noise_level > 0 else 1e-10
snr_db = 10 * np.log10(sig_pwr / noise_pwr)

st.sidebar.markdown("---")
st.sidebar.metric(label="Channel Quality (SNR)", value=f"{snr_db:.2f} dB", 
                  delta="Clear" if snr_db > 10 else "Noisy", delta_color="normal")

# --- 7. PLOTTING & DISPLAY ---
if unit_choice == "GNU Radio DSP (Advanced)":
    st.header("🛠️ GNU Radio Receiver Pipeline (Unit V)")
    st.info("Architecture: AWGN Channel → LPF Block → Decision Logic")
    
    # DSP Processing
    cutoff = st.slider("Filter Cutoff Frequency (Hz)", 5, 150, 40)
    recovered = gnuradio_lpf_block(noisy_signal, cutoff, fs)
    
    # BER Calculation
    # Simple zero-crossing detector to recover bits
    recovered_bits_raw = np.where(recovered > 0, 1, -1)
    # Sampling at the middle of each bit period
    samples = recovered_bits_raw[100::200] 
    ber = np.sum(message_bits != samples) / len(message_bits)
    
    st.sidebar.metric(label="Bit Error Rate (BER)", value=f"{ber:.4f}", 
                      delta="Lossy" if ber > 0 else "Perfect", delta_color="inverse")

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Time Domain: Noise vs Recovery")
        fig_rec = go.Figure()
        fig_rec.add_trace(go.Scatter(y=noisy_signal[:500], name="Noisy Input", line=dict(color='red', width=1)))
        fig_rec.add_trace(go.Scatter(y=recovered[:500], name="GNU Radio Output", line=dict(color='green', width=2.5)))
        st.plotly_chart(fig_rec, use_container_width=True)
        
    with col_b:
        st.subheader("Frequency Spectrum")
        yf_rec = fft(recovered)
        xf_rec = fftfreq(len(t), 1/fs)
        fig_spec = go.Figure()
        fig_spec.add_trace(go.Scatter(x=xf_rec[:fs//2], y=np.abs(yf_rec[:fs//2]), fill='tozeroy', name="Filtered"))
        st.plotly_chart(fig_spec, use_container_width=True)

else:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Time Domain (Oscilloscope)")
        fig_time = go.Figure()
        fig_time.add_trace(go.Scatter(x=t, y=noisy_signal, name="Received Signal"))
        st.plotly_chart(fig_time, use_container_width=True)

    with col2:
        if unit_choice == "Digital (Unit IV)":
            st.subheader("Constellation Diagram")
            # Create a simple I/Q plot
            fig_const = go.Figure()
            fig_const.add_trace(go.Scatter(x=message, y=[0]*len(t), mode='markers', marker=dict(size=8, color='orange')))
            fig_const.update_xaxes(range=[-2, 2], title="In-Phase")
            fig_const.update_yaxes(range=[-1, 1], title="Quadrature")
            st.plotly_chart(fig_const, use_container_width=True)
        else:
            st.subheader("Spectrum Analyzer")
            yf = fft(noisy_signal)
            xf = fftfreq(len(t), 1/fs)
            fig_freq = go.Figure()
            fig_freq.add_trace(go.Scatter(x=xf[:fs//2], y=np.abs(yf[:fs//2]), fill='tozeroy', line=dict(color='cyan')))
            st.plotly_chart(fig_freq, use_container_width=True)

st.markdown("---")
st.caption("Developed by Jayashree S | Mentor: Mr. Harish Ganasampantham | Team Astra")
