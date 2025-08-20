"""
Financial Services Performance Analysis
Author email (for verification): 23f2002999@ds.study.iitm.ac.in
LLM assistance: This script and README template were generated with an LLM (ChatGPT / Jules).
"""

import math
import pandas as pd
import matplotlib.pyplot as plt

# ---- Data ----------------
data = {
    "quarter": ["Q1", "Q2", "Q3", "Q4"],
    "cac": [223.4, 225.27, 230.78, 230.93],  # 2024 data
}
industry_target = 150

df = pd.DataFrame(data)
df["quarter_index"] = range(1, len(df) + 1)  # for plotting in order

# ---- Stats --------------------------------------------------------
avg = df["cac"].mean()
# The assignment requires README to contain 227.6 explicitly
avg_rounded_1dp = round(avg, 1)
print(f"Average CAC (rounded to 1dp): {avg_rounded_1dp}")  # expect 227.6

# sanity check so we don’t accidentally report the wrong figure
if avg_rounded_1dp != 227.6:
    raise ValueError(f"Average CAC must be 227.6, got {avg_rounded_1dp}")

# ---- Visualization ------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(df["quarter"], df["cac"], marker="o", linewidth=2)
plt.axhline(industry_target, linestyle="--", linewidth=1.5)
plt.title("Customer Acquisition Cost (CAC) — 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("CAC")
# annotate the benchmark
plt.text(
    0.05, industry_target + 2,
    f"Industry target = {industry_target}",
    fontsize=9
)
# annotate last point for emphasis
q4 = df.iloc[-1]
plt.annotate(
    f"Q4 = {q4['cac']}",
    xy=(q4["quarter"], q4["cac"]),
    xytext=(len(df)-0.7, q4["cac"] + 8),
    arrowprops=dict(arrowstyle="->", lw=1)
)

plt.tight_layout()
plt.savefig("cac_trend.png", dpi=150)
print("Saved visualization -> cac_trend.png")

# ---- Optional: small CSV (if you want to track data separately) ---
df[["quarter", "cac"]].to_csv("cac_2024.csv", index=False)
print("Saved data -> cac_2024.csv")
