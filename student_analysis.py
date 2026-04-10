import pandas as pd
import matplotlib.pyplot as plt

# More realistic student dataset
data = {
    "Name": ["Rahul", "Anita", "Kiran", "Sneha", "Arjun"],
    "Math": [78, 92, 85, 60, 88],
    "Science": [82, 89, 80, 65, 90],
    "English": [75, 95, 78, 70, 85]
}

df = pd.DataFrame(data)

# Calculate total and average marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Find topper
topper = df.loc[df["Total"].idxmax()]

print("📊 Student Data:\n")
print(df)

print("\n🏆 Topper:")
print(topper["Name"], "with total marks:", topper["Total"])

# Plot marks comparison
df.set_index("Name")[["Math", "Science", "English"]].plot(kind="bar")
plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
