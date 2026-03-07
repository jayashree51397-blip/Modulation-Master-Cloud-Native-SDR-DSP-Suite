📡 Modulation Master: Advanced Communication Lab Suite
A Cloud-Native Signal Processing & SDR Simulation Platform


https://adv-com-systemslab-xvjn8evekhf473peayfpds.streamlit.app/

🚀 Project Overview

Modulation Master is an interactive web application designed to bridge the gap between theoretical communication engineering and practical software-defined radio 
(SDR) implementation. Developed as part of the II Year ECE-B curriculum
at R.M.K. Engineering College, this suite allows for real-time visualization of analog and digital modulation schemes in both time and frequency 
domains.
🛠️ Key Features
1. Analog Modulation (Unit I & II)Standard AM, DSB-SC, and FM: Real-time generation of modulated waves with adjustable carrier and message frequencies.
2. Live Spectrum Analysis: Integrated Fast Fourier Transform (FFT) to visualize sidebands and power distribution.
3. Digital Modulation (Unit IV)BPSK Implementation: Visualization of phase reversals ($180^\circ$) at bit transitions..Constellation Mapping: Real-time plotting of signal points to analyze phase accuracy.
4. GNU Radio & DSP Integration (Advanced)SDR Receiver Logic: Implementation of low-pass filtering and noise suppression inspired by GNU Radio flowgraphs.Channel Noise Simulation: Adjustable Gaussian noise levels to test system reliability and SNR (Unit V).
   
   💻 Tech Stack
   Language: Python 3.x
   Web Framework: Streamlit (Cloud-Native Deployment)
    Signal Processing: NumPy, SciPy (Signal/FFT modules)
   Visualization: Plotly (Interactive Oscilloscope & Spectrum Analyzer)
   Version Control: GitHub with CI/CD integration

   📖 Syllabus Mapping
This project directly implements concepts from the Advanced Communication Lab:

Unit I: Amplitude Modulation and Power Relations.

Unit II: Frequency Modulation and Deviation.

Unit IV: Binary Phase Shift Keying (BPSK) and Digital Signaling.

Unit V: Channel Noise Analysis and System Performance.

🔧 Installation & Local Setup
To run this project locally, follow these steps:

Clone the repository:

Bash
git clone https://github.com/your-username/modulation-master.git
Install dependencies:

Bash
pip install -r requirements.txt
Run the app:

Bash
streamlit run app.py

🎓 Author & Credits
Developer: Jayashree S (II Year ECE-B)

Institution: R.M.K. Engineering College

Mentor: Mr. Harish Ganasampantham




<img width="1636" height="945" alt="Screenshot 2026-01-15 104934" src="https://github.com/user-attachments/assets/d29a5cb9-d986-48de-b233-f812fd7cee79" />
<img width="656" height="985" alt="Screenshot 2026-01-15 104650" src="https://github.com/user-attachments/assets/bb9c6562-dfbf-453d-a6bc-dc439cb1b6a3" />
<img width="1914" height="946" alt="Screenshot 2026-01-15 084007" src="https://github.com/user-attachments/assets/b6d5c444-d8b3-4027-a2f1-5d282b29d1bc" />
