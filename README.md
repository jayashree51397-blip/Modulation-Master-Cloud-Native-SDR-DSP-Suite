📡 Advanced SDR & Communication SuiteA Cloud-Native Signal Processing Platform for Electronics & Communication Engineering



https://adv-com-systemslab-xvjn8evekhf473peayfpds.streamlit.app/


🚀 Project Overview


Modulation Master is an interactive web-based simulation tool designed to bridge the gap between theoretical communication engineering and practical Software Defined Radio (SDR) implementation. Developed as part of the II Year ECE-B curriculum at RMK Engineering College, this suite provides real-time visualization and quantitative analysis of signal modulation and recovery.

🛠️ Advanced Features 

1. GNU Radio DSP Pipeline (Unit V)Digital Receiver Logic: Implements a 5th-order Butterworth Low Pass Filter to emulate GNU Radio flowgraphs.Signal Recovery: Real-time noise suppression of corrupted carrier waves using SciPy-based DSP blocks.
2. Quantitative Metrics & AnalysisReal-time SNR Calculation: Dynamic measurement of Signal-to-Noise Ratio (dB) to assess channel quality.BER Estimation: Automated Bit Error Rate calculation by comparing transmitted vs. recovered bit sequences in BPSK.
3. Comprehensive Modulation SuiteAnalog (Unit I & II): Standard AM, DSB-SC, and Frequency Modulation (FM) with live Spectrum Analysis.Digital (Unit IV): BPSK modulation with integrated Constellation Diagrams to visualize phase shifts ($180^\circ$) and noise-induced jitter.
  
💻 Technical StackLanguage: 

Python 3.8
DSP Engine: SciPy (Signal Processing), NumPyVisualization: Plotly (Interactive Oscilloscope & Spectrum Analyzer)Framework: Streamlit (Cloud-Native Deployment)


📖 Syllabus Alignment

This project directly maps to the Advanced Communication Lab requirements:
Unit I & II: Amplitude and Frequency Modulation Power Relations.
Unit IV: Digital Signaling and Phase Shift Keying (BPSK).
Unit V: Noise Analysis, SNR Improvements, and Error Probabilities.


🔧 Local Setup

Clone the repository:

Bash
git clone https://github.com/your-username/modulation-master.git
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py


🎓 Author & Acknowledgments
Lead Developer: Jayashree S (II Year ECE-B)
Institution: RMK Engineering College





<img width="1636" height="945" alt="Screenshot 2026-01-15 104934" src="https://github.com/user-attachments/assets/d29a5cb9-d986-48de-b233-f812fd7cee79" />

<img width="656" height="985" alt="Screenshot 2026-01-15 104650" src="https://github.com/user-attachments/assets/bb9c6562-dfbf-453d-a6bc-dc439cb1b6a3" />

<img width="1914" height="946" alt="Screenshot 2026-01-15 084007" src="https://github.com/user-attachments/assets/b6d5c444-d8b3-4027-a2f1-5d282b29d1bc" />

<img width="1916" height="1079" alt="Screenshot 2026-03-27 213924" src="https://github.com/user-attachments/assets/b0afe716-e1d7-48a3-ac2c-a0af30782be6" />

<img width="1916" height="1079" alt="Screenshot 2026-03-27 213924" src="https://github.com/user-attachments/assets/346257ef-e542-486d-895d-9620929f4241" />

<img width="1919" height="1141" alt="Screenshot 2026-03-27 213939" src="https://github.com/user-attachments/assets/6d0e304d-270d-4b94-b98d-d4aeac8418c4" />

<img width="1919" height="1133" alt="Screenshot 2026-03-27 213950" src="https://github.com/user-attachments/assets/c5a9c105-c8e0-4cfb-acd1-24aa24d8707e" />

<img width="1918" height="1137" alt="Screenshot 2026-03-27 214635" src="https://github.com/user-attachments/assets/b784d87d-073a-47f9-a255-79f622a981a2" />



