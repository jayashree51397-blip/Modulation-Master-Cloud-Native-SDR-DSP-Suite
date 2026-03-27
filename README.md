📡 Modulation Master: Advanced SDR & Communication SuiteA Cloud-Native Signal Processing Platform for Electronics & Communication Engineering(Replace with your actual link)🚀 Project OverviewModulation Master is an interactive web-based simulation tool designed to bridge the gap between theoretical communication engineering and practical Software Defined Radio (SDR) implementation. Developed as part of the II Year ECE-B curriculum at Panimalar Engineering College, this suite provides real-time visualization and quantitative analysis of signal modulation and recovery.🛠️ Advanced Features (O-Grade Specifications)1. GNU Radio DSP Pipeline (Unit V)Digital Receiver Logic: Implements a 5th-order Butterworth Low Pass Filter to emulate GNU Radio flowgraphs.Signal Recovery: Real-time noise suppression of corrupted carrier waves using SciPy-based DSP blocks.2. Quantitative Metrics & AnalysisReal-time SNR Calculation: Dynamic measurement of Signal-to-Noise Ratio (dB) to assess channel quality.BER Estimation: Automated Bit Error Rate calculation by comparing transmitted vs. recovered bit sequences in BPSK.3. Comprehensive Modulation SuiteAnalog (Unit I & II): Standard AM, DSB-SC, and Frequency Modulation (FM) with live Spectrum Analysis.Digital (Unit IV): BPSK modulation with integrated Constellation Diagrams to visualize phase shifts ($180^\circ$) and noise-induced jitter.💻 Technical StackLanguage: Python 3.xDSP Engine: SciPy (Signal Processing), NumPyVisualization: Plotly (Interactive Oscilloscope & Spectrum Analyzer)Framework: Streamlit (Cloud-Native Deployment)📖 Syllabus AlignmentThis project directly maps to the Advanced Communication Lab requirements:Unit I & II: Amplitude and Frequency Modulation Power Relations.Unit IV: Digital Signaling and Phase Shift Keying (BPSK).Unit V: Noise Analysis, SNR Improvements, and Error Probabilities.🔧 Local SetupClone the repository:Bashgit clone https://github.com/your-username/modulation-master.git
Install dependencies:Bashpip install -r requirements.txt
Run the application:Bashstreamlit run app.py
🎓 Author & Acknowledgments
Lead Developer: Jayashree S (II Year ECE-B)
Institution: RMK Engineering College





<img width="1636" height="945" alt="Screenshot 2026-01-15 104934" src="https://github.com/user-attachments/assets/d29a5cb9-d986-48de-b233-f812fd7cee79" />
<img width="656" height="985" alt="Screenshot 2026-01-15 104650" src="https://github.com/user-attachments/assets/bb9c6562-dfbf-453d-a6bc-dc439cb1b6a3" />
<img width="1914" height="946" alt="Screenshot 2026-01-15 084007" src="https://github.com/user-attachments/assets/b6d5c444-d8b3-4027-a2f1-5d282b29d1bc" />
