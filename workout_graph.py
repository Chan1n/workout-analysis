import os
import pandas as pd
import matplotlib.pyplot as plt

# สร้างโฟลเดอร์เก็บกราฟ
save_path = "graphs"

if not os.path.exists(save_path):
    os.makedirs(save_path)

# ดึงข้อมูลจาก Google Sheet
url = "https://docs.google.com/spreadsheets/d/1_27ZF2shVsMSYs9hzimi8_F2wkcjtjAICKzktvao6Fo/export?format=csv&gid=1267712629"
df = pd.read_csv(url)

# จัดการข้อมูล
df["Date"] = pd.to_datetime(df["Date"])
today = pd.Timestamp.today()

df = df[(df["Date"].dt.month == today.month) &
        (df["Date"].dt.year == today.year)]

df["Total Weight"] = (
    df["Set 1 Weights (lbs)"] +
    df["Set 2 Weights (lbs)"] +
    df["Set 3 Weights (lbs)"]
)

# สร้างกราฟ
plt.figure(figsize=(10,6))
plt.bar(df["Exercise"], df["Total Weight"], color="skyblue")

plt.title(f"Workout Volume ({today.strftime('%B %Y')})")
plt.xlabel("Exercise")
plt.ylabel("Total Weight (lbs)")
plt.xticks(rotation=45)

plt.tight_layout()

# ตั้งชื่อไฟล์
file_name = f"workout_{today.strftime('%B_%Y')}.png"
full_path = os.path.join(save_path, file_name)

plt.savefig(full_path)

print("Graph saved:", full_path)
