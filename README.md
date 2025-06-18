# 🧬 **Enhancing Proteomics Research through ML Algorithms and Blockchain Security**

## 📘 **Project Overview**

**Proteomics** is the study of protein structures and functions. It plays a critical role in medical and biological research. However, proteomics data is often **complex, high-volume, and sensitive**, making it difficult to process and secure using traditional methods.

This project introduces a secure, intelligent system that combines **Machine Learning (ML)** and **Blockchain technology** to:
- **Classify protein sequences**
- **Predict protein functions**
- **Ensure data security and traceability**
- **Provide a user-friendly web interface for researchers**

---

## 🎯 **Key Objectives**

- ✅ **Classify proteins** using ML algorithms (Neural Networks, SVM, etc.)
- ✅ **Secure data** using Ethereum Blockchain
- ✅ **Enable researchers** to upload, analyze, and verify predictions via a web interface
- ✅ **Support large-scale proteomics research** with accuracy, transparency, and speed

---

## 🛠️ **Technologies Used**

| **Layer** | **Tools & Technologies** |
|----------|---------------------------|
| **Frontend** | HTML, CSS, Bootstrap, Flask |
| **Backend** | Python, Flask, MySQL |
| **ML Models** | Neural Network, Random Forest, SVM, Logistic Regression, Decision Tree |
| **Blockchain** | Ethereum, Ganache, Truffle |
| **Feature Extraction** | TF-IDF Vectorizer |
| **Libraries** | Scikit-learn, TensorFlow, Pandas, NumPy |
| **Dataset** | Structural Protein Sequences (RCSB, 467,000+ records) |

---

## 🧠 **ML Models and Evaluation**

| **Model**             | **Accuracy** | **Precision** | **Recall** |
|-----------------------|--------------|---------------|------------|
| **Neural Network**    | ✅ **93.68%** | ✅ **93.98%**  | ✅ **93.68%** |
| Logistic Regression   | 93.10%       | 92.90%        | 93.10%     |
| Random Forest         | 29.04%       | 92.96%        | 29.04%     |
| Support Vector Machine (SVM) | 28.72% | 91.17% | 28.72% |
| Decision Tree         | 29.09%       | 92.96%        | 29.09%     |

✅ **Neural Networks** achieved the highest scores and were selected for final deployment.

---

## 🔐 **Blockchain Integration**

Implemented using:
- **Ganache** for local blockchain simulation
- **Truffle** for smart contract development
- **Ethereum** for immutable data storage

**Key Benefits:**
- 🔒 **Tamper-proof predictions**
- 🔍 **Hash-based verification**
- 📈 **Transparent audit logs**

---

## 🌐 **System Architecture**
[User Input] ➝ [Preprocessing (TF-IDF)] ➝ [ML Prediction] ➝ [Blockchain Logging] ➝ [Flask UI]


## 🖼️ **Screenshots**

### 🔐 **Login Interfaces**
### Admin login page
![image](https://github.com/user-attachments/assets/23773b59-3ab7-424f-b3a4-4ca95f5a76f8)
### User login page
![image](https://github.com/user-attachments/assets/73ab8e77-d220-4734-add3-b5aded205408)
### 📊 **Training & Testing**
### Training Interface for Classification Model
![image](https://github.com/user-attachments/assets/ead53183-bce9-41a7-88b8-9cd1c0a01e4d)
### Testing Interface for Model Evaluation
![image](https://github.com/user-attachments/assets/1f29c91c-35c9-4327-b56f-179d2f6bad9e)
### Results
### Performance metrics of classification models
![image](https://github.com/user-attachments/assets/02afbae2-69ff-4ecc-8653-53ce232177e1)
### Bargraph Representation of Performance
![image](https://github.com/user-attachments/assets/544e04c9-da9e-4c12-86b0-fd2bc278e5b6)
### Blockchain Page for Proteomics Data Analytics
![image](https://github.com/user-attachments/assets/2be3f361-090d-4cf0-ab6b-155ea1726709)

## 👩‍💻 **Features**

- 📥 Upload `.txt` protein sequence files  
- 🧠 Choose and train ML models  
- 📊 View performance metrics (Accuracy, Precision, Recall)  
- 🔐 Secure prediction results using blockchain  
- 👥 Role-based login: **Admin** and **User** interfaces

---

## 👨‍🔬 **Team Members**

- **Ms. J Siri** – *ML Model Developer*  
- **Ms. P Lakshmi Manjusha** – *Blockchain & Backend Developer*  
- **Ms. P Deepika** – *UI/UX & Integration Lead*

**Internal Guide:**  
**Mr. Navakanth Inala**  
Assistant Professor, Dept. of CSE, **MVSREC**

---

## 🚀 **Future Enhancements**

- 🌐 Deploy to **Ethereum testnet (Goerli/Mainnet)**
- 🧬 Add deep learning models (CNN/RNN)
- 📈 Include biological visualizations for researchers
- 🧠 Improve auto-labeling for protein datasets

---

## 📜 **License**

This project is licensed under the **MIT License**.
