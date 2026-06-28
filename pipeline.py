
import pandas as pd

# 1. Raw, messy system performance metrics
raw_perf_data = {
    "Emp_ID": [1001, 1002, 1003],
    "Commits": [145, 89, 210],
    "Active_Days": [22, 18, 25]
}
perf_df = pd.DataFrame(raw_perf_data)

# 2. Raw, messy employee system records
raw_directory_data = {
    "Emp_ID": [1001, 1002, 1003],
    "Engineer_Name": ["   Oseiwe ", "alice", "Bob "]
}
directory_df = pd.DataFrame(raw_directory_data)

# A. Clean up whitespace and casing
directory_df["Engineer_Name"] = directory_df["Engineer_Name"].str.strip().str.upper()

# B. Merge tables
portfolio_df = pd.merge(perf_df, directory_df, on="Emp_ID", how="inner")

# C. Calculate your new performance metric column
portfolio_df["Commits_Per_Day"] = portfolio_df["Commits"] / portfolio_df["Active_Days"]

# D. Save your finalized master dataframe safely to a CSV file!
portfolio_df.to_csv("cleaned_engineering_data.csv", index=False)

# Print the final dataframe to verify our columns are perfect
print(portfolio_df)

import matplotlib.pyplot as plt  # We import it and give it the short nickname 'plt'

# Step 1: Tell Python to draw a bar chart
# Format: plt.bar(X_axis_categories, Y_axis_numeric_values, color="your_choice")
plt.bar(portfolio_df["Engineer_Name"], portfolio_df["Commits_Per_Day"], color="skyblue")

# Step 2: Add metadata so a manager can read it
plt.title("Developer Productivity Index") # Adds a main title at the top
plt.xlabel("Engineer Name")               # Labels the bottom horizontal axis
plt.ylabel("Commits per Day")             # Labels the vertical axis

# Step 3: Save the canvas as a physical picture file on your computer
plt.savefig("developer_productivity.png", bbox_inches="tight")

# Step 4: Clear the canvas to free up memory
plt.close()