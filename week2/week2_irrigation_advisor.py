import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (adjust path if needed)
df = pd.read_csv("../week1/Smart_Irrigation_Week1_Dataset.csv")

# Rule-based irrigation function
def irrigation_required(soil, rain):
    if soil < 30 and rain < 5:
        return "Yes"
    else:
        return "No"

# Apply rule
df["Predicted_Irrigation"] = df.apply(
    lambda row: irrigation_required(row["Soil_Moisture (%)"], row["Rainfall (mm)"]), axis=1
)

# Compare with dataset labels (Week 1 ground truth)
if "Irrigation_Required" in df.columns:
    accuracy = (df["Predicted_Irrigation"] == df["Irrigation_Required"]).mean() * 100
    print(f"Model Accuracy: {accuracy:.2f}%")

# Save results
df.to_csv("../week2/Week2_Output_With_Predictions.csv", index=False)
print("✅ Predictions saved to week2/Week2_Output_With_Predictions.csv")

# Visualization: Soil Moisture vs Temperature with irrigation requirement
plt.figure(figsize=(10, 6))
plt.scatter(df["Soil_Moisture (%)"], df["Temperature (°C)"],
            c=df["Predicted_Irrigation"].map({"Yes": "red", "No": "green"}),
            label="Prediction")
plt.xlabel("Soil Moisture (%)")
plt.ylabel("Temperature (°C)")
plt.title("Irrigation Requirement (Yes=Red, No=Green)")
plt.grid(True)
plt.show()
