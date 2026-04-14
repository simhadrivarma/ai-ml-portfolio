import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import IPython.display as display

# 1. Load data from CSV
try:
    df = pd.read_csv("students.csv")
    print("✅ Data loaded successfully!\n")

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
    fig = plt.figure(figsize=(10, 6), facecolor='w')
    df.set_index("Name")[["Math", "Science", "English"]].plot(kind="bar", figsize=(10, 6), ax=plt.gca())
    plt.title("Subject-wise Marks Comparison", fontsize=14)
    plt.ylabel("Marks")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Display the plot as an image in the notebook output
    data = io.BytesIO()
    plt.savefig(data)
    image = F"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
    alt = "Subject-wise Marks Comparison Chart"
    display.display(display.Markdown(F"![{alt}]({image})"))
    plt.close(fig)

    print("\n🎨 Graph has been generated and displayed.")

except FileNotFoundError:
    print("❌ Error: students.csv not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
