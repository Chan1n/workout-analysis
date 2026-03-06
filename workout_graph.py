import pandas as pd
import matplotlib.pyplot as plt

url = "https://docs.google.com/spreadsheets/d/1_27ZF2shVsMSYs9hzimi8_F2wkcjtjAICKzktvao6Fo/export?format=csv&gid=1267712629"

df = pd.read_csv(url)

df["Date"] = pd.to_datetime(df["Date"])

df["Total Weight"] = (
    df["Set 1 Weights (lbs)"] +
    df["Set 2 Weights (lbs)"] +
    df["Set 3 Weights (lbs)"]
)

plt.figure()

plt.bar(df["Exercise"], df["Total Weight"])

plt.title("Workout Volume")
plt.xlabel("Exercise")
plt.ylabel("Total Weight")

plt.savefig("workout_graph.png")

plt.show()
