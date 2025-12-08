import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('headache_data.csv')

# Scatter plot of stress levels vs headache intensity
plt.figure(figsize=(10, 6))
plt.scatter(data['stress_level'], data['headache_intensity'], alpha=0.5)
plt.title('Stress Level vs Headache Intensity')
plt.xlabel('Stress Level')
plt.ylabel('Headache Intensity')
plt.grid(True)
plt.tight_layout()
plt.savefig("Stress/stress_vs_headache.png")

# Insight extraction
high_stress_days = data[data["stress_level"] >= 7]

if len(high_stress_days) > 0 and high_stress_days["headache_intensity"].mean() > data["headache_intensity"].mean():
    print("Insight: Headaches tend to be more intense on high-stress days (stress level ≥ 7).")
else:
    print("No clear relationship between stress level and headache intensity in this sample.")
