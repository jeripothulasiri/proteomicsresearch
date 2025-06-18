🧬 Enhancing Proteomics Research through ML Algorithms and Blockchain Security
📘 Project Overview
Proteomics, the study of protein structures and functions, is a crucial domain in bioinformatics and medical research. However, proteomics data is massive, complex, and sensitive, making it difficult to manage, analyze, and secure using traditional systems.

This project addresses these challenges by integrating Machine Learning (ML) algorithms for protein classification and prediction with Blockchain for tamper-proof data security. A user-friendly Flask web interface allows researchers to upload data, run analyses, and view secure results — all in one platform.

🎯 Key Objectives
✅ Develop a machine learning-based prediction system for protein classification

✅ Secure all predictions using Ethereum blockchain (Truffle + Ganache)

✅ Design a user-friendly Flask-based web interface for researchers

✅ Ensure scalability, transparency, and reproducibility in proteomics research

🛠️ Technologies Used
Layer	Tools
Frontend	HTML, CSS, Bootstrap, Flask
Backend	Python, Flask, MySQL
ML Models	Neural Networks, Random Forest, SVM, Logistic Regression, Decision Tree
Blockchain	Ganache, Truffle, Ethereum Smart Contracts
Libraries	Scikit-learn, TensorFlow, Pandas, NumPy
Dataset	Structural Protein Sequences from RCSB (~467,000+ sequences)
Feature Extraction	TF-IDF Vectorizer

🧠 ML Models and Evaluation
Model	Accuracy (Best)	Precision	Recall
Neural Network	✅ 93.68%	✅ 93.98%	✅ 93.68%
Logistic Regression	93.10%	92.90%	93.10%
Random Forest	29.04%	92.96%	29.04%
SVM	28.72%	91.17%	28.72%
Decision Tree	29.09%	92.96%	29.09%

✅ Neural Networks outperformed other models in both Testset 1 and Testset 2.

🔐 Blockchain Integration
All ML-generated results are stored on a local Ethereum blockchain using:

Ganache for simulation

Truffle for smart contract management

SHA-based hashing to ensure integrity

This ensures:

Immutable records of predictions

Transparent data verification

Prevention of tampering and unauthorized access

🌐 System Architecture
css
Copy
Edit
[User Input] → [Preprocessing (TF-IDF)] → [ML Prediction] → [Blockchain Logging] → [Flask Web Interface]
(Replace with your own image)

🖼️ Screenshots
🔐 Admin & User Login


📊 Model Training & Prediction Results


🔒 Blockchain Hash Verification

(Replace above with your own local screenshots for authenticity)

👩‍💻 Features
Upload protein sequence data (e.g., .txt, .fasta)

Select & train ML model (RF, SVM, NN, etc.)

View performance (Accuracy, Precision, Recall)

Securely log predictions to blockchain

Role-based login system (Admin & User)

👨‍🔬 Team Members
Ms. J Siri – ML Model Developer

Ms. P Lakshmi Manjusha – Blockchain & Backend Developer

Ms. P Deepika – UI/UX & Integration Lead

Internal Guide:
Mr. Navakanth Inala
Assistant Professor, Dept. of CSE, MVSREC

📈 Future Enhancements
Deploy to live Ethereum testnet (Goerli/Testnet)

Integrate deep learning (CNN/RNN/Transformer)

Add visualization tools for biological interpretation

Expand dataset with real-time protein analysis

📜 License
This project is licensed under the MIT License.
