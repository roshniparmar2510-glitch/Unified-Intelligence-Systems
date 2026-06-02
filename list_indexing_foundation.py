# Programming Foundation: Tracking Data Matrices via List Indexing

# Creating a list of target application milestones
portfolio_milestones = ["SAT Prep", "Python Scripts", "Common App Essay", "LOR Request"]

print("📦 Initializing Portfolio Milestone Inventory...\n")

# In Python, counting always starts at 0!
first_task = portfolio_milestones[0]
third_task = portfolio_milestones[2]

print(f"📌 The absolute first item in our index (Position 0) is: {first_task}")
print(f"📌 The third item in our index (Position 2) is: {third_task}")

# Printing the full list length
total_tasks = len(portfolio_milestones)
print(f"\n📊 Total active milestones stored in this data array: {total_tasks}")
