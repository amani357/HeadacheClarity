import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('headache_data.csv')

# Scatter plot of sleep hours vs headache intensity
plt.figure(figsize=(10, 6))
plt.scatter(data['sleep_hours'], data['headache_intensity'], alpha=0.5)
plt.title('Sleep Hours vs Headache Intensity')
plt.xlabel('Sleep Hours')
plt.ylabel('Headache Intensity')
plt.grid(True)
plt.tight_layout()
plt.savefig("Sleep/sleep_vs_headache.png")

# Insight extraction
low_sleep_days = data[data["sleep_hours"] < 6]
if len(low_sleep_days) > 0 and low_sleep_days["headache_intensity"].mean() > data["headache_intensity"].mean():
    print("Insight: headaches tend to be more intense after nights with less than 6 hours’ sleep.")
else:
    print("No clear relationship between low sleep and headache intensity in this sample.")