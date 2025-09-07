# 🌱 Smart Irrigation Advisor for Sustainable Agriculture

## 📌 Project Overview
Agriculture consumes nearly **70% of global freshwater resources**, yet much of it is wasted due to **over-irrigation or under-irrigation**.  
This project develops a **Smart Irrigation Advisor** software that uses soil moisture, rainfall, and temperature data to recommend **optimal irrigation schedules**, helping farmers:

- 💧 Save water  
- 🌾 Improve crop yield  
- 🌍 Promote sustainable agriculture  

---

## 📅 Project Timeline

- **Week 1 (30%)** – Dataset preparation + system design ✅  
- **Week 2 (30%)** – Prototype development (Python-based irrigation advisor)  
- **Week 3 (40%)** – Final implementation, testing, and project report  

---

## 📊 Dataset (Week 1)

The dataset simulates real farm data for **20 days**, including soil moisture, rainfall, temperature, crop type, and irrigation requirement.

**Columns:**
- `Date` – Day of observation  
- `Soil_Moisture (%)` – Percentage of water in soil (<30% = dry)  
- `Rainfall (mm)` – Daily rainfall in millimeters  
- `Temperature (°C)` – Average daily temperature  
- `Crop_Type` – Wheat, Rice, or Maize  
- `Irrigation_Required` – Yes/No (based on sustainability rules)  

📂 Files included:  
- [`data/Smart_Irrigation_Week1_Dataset.csv`](./data/Smart_Irrigation_Week1_Dataset.csv)   
- Week 1 Report (in `docs/` folder)  

**Sample Data:**

| Date       | Soil_Moisture (%) | Rainfall (mm) | Temperature (°C) | Crop_Type | Irrigation_Required |
|------------|------------------|---------------|------------------|-----------|----------------------|
| 2025-09-01 | 25               | 0             | 32               | Wheat     | Yes                  |
| 2025-09-02 | 40               | 5             | 30               | Wheat     | No                   |
| 2025-09-03 | 18               | 0             | 34               | Rice      | Yes                  |
| 2025-09-04 | 60               | 12            | 28               | Rice      | No                   |
| 2025-09-05 | 22               | 0             | 33               | Wheat     | Yes                  |

---

## 🏗️ System Design

### Architecture
1. **Input Layer:** Soil Moisture, Rainfall, Temperature, Crop Type  
2. **Processing Layer:** Rule-based decision algorithm  
   - If `Soil Moisture < 30%` AND `Rainfall < 5 mm` → Irrigation Required = Yes  
   - Else → Irrigation Required = No  
3. **Output Layer:** Irrigation recommendation (Yes/No)  

### Flowchart
```mermaid
flowchart TD
    A[Start] --> B[Collect Input Data: Soil, Rainfall, Temp, Crop]
    B --> C{Soil Moisture < 30%?}
    C -- No --> D[No Irrigation Required]
    C -- Yes --> E{Rainfall > 10mm?}
    E -- Yes --> D
    E -- No --> F[Irrigation Required]
