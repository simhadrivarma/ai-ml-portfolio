import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data from CSV 
try:
    df = pd.read_csv("students.csv")
    print("✅ Data loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: students.csv not found.")

# 2. Advanced Analysis
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = (df["Total"] / 3).round(2)

# 3. Insights (The 'Smart' part)
topper = df.loc[df["Total"].idxmax()]
lowest = df.loc[df["Total"].idxmin()]

print("📊 --- STUDENT REPORT CARD ---")
print(df)
print("\n🏆 TOPPER OF THE CLASS:")
print(f"Name: {topper['Name']} | Total: {topper['Total']} | Avg: {topper['Average']}%")

print("\n📉 NEEDS IMPROVEMENT:")
print(f"Name: {lowest['Name']} | Total: {lowest['Total']}")

# 4. Professional Visualization
df.set_index("Name")[["Math", "Science", "English"]].plot(kind="bar", figsize=(10, 6))
plt.title("Subject-wise Marks Comparison", fontsize=14)
plt.ylabel("Marks")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the graph as an image
plt.savefig("marks_chart.png")
print("\n🎨 Graph has been generated and saved as 'marks_chart.png'")
plt.show()
