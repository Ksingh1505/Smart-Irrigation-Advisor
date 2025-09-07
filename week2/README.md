# 🌱 Week 2 – Smart Irrigation Advisor Prototype

## 📌 Overview
In Week 2, we moved from dataset preparation (Week 1) to **developing a working prototype**.  
The prototype software uses a **rule-based algorithm** to predict whether irrigation is required, based on soil moisture, rainfall, and temperature.

---

## 🎯 Objectives
- Use the Week 1 dataset as input.  
- Apply a **rule-based decision system**:  
  - If `Soil Moisture < 30%` and `Rainfall < 5mm` → Irrigation Required = **Yes**  
  - Else → **No irrigation needed**  
- Implement in Python (pandas + matplotlib).  
- Save predictions into a new dataset.  
- Visualize irrigation requirements.  

---

## 📂 Files in this Folder
- [`Week2_Output_With_Predictions.csv`](./Week2_Output_With_Predictions.csv) – Dataset with predictions  
- [`week2_irrigation_advisor.py`](./week2_irrigation_advisor.py) – Python script for prototype  
- [`Week2_Report.pdf`](./Week2_Report.pdf) – Formal report (PDF)  
- [`Week2_Report.docx`](./Week2_Report.docx) – Formal report (Word)  

---

## 🖥️ How to Run the Code
1. Make sure you have Python installed with these libraries:
   ```bash
   pip install pandas matplotlib
