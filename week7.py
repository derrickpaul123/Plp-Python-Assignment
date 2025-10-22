import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for beautiful plots — because beauty honors the community!
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 🌿 Ubuntu Hospital Dataset: "We care because we are together."
data = {
    'Patient_ID': range(1, 101),
    'Age': np.random.randint(1, 90, size=100),
    'Gender': np.random.choice(['Male', 'Female'], size=100),
    'Condition': np.random.choice(['Flu', 'Diabetes', 'Hypertension', 'Asthma', 'Healthy'], size=100, p=[0.3, 0.2, 0.2, 0.2, 0.1]),
    'Treatment_Duration_Days': np.random.randint(1, 15, size=100),
    'Satisfaction_Score': np.random.randint(1, 11, size=100),  # 1-10 scale
    'Follow_Up_Needed': np.random.choice([True, False], size=100, p=[0.4, 0.6])
}

# Create DataFrame — our digital village square 🌳
df = pd.DataFrame(data)

print("🏥 Welcome to Ubuntu General Hospital!")
print("Where every patient’s data is honored and cared for.\n")
print(df.head(10))  # Show first 10 villagers (patients)