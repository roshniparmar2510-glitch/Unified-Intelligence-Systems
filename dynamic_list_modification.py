# Programming Foundation: Dynamic Modification of Data Arrays

# Initializing your core portfolio tracks
portfolio_tracks = ["SAT Math", "Python Coding", "Substack Essays"]

print("🚀 Initializing Active Portfolio Track Manifest...\n")
print(f"📊 Original List: {portfolio_tracks}")

# 1. Appending a new asset to the end of the data list
portfolio_tracks.append("Letters of Rec")
print(f"➕ After Append:   {portfolio_tracks}")

# 2. Modifying an existing item (Overwriting Index 0)
portfolio_tracks[0] = "SAT 800 Target"
print(f"🔄 After Update:   {portfolio_tracks}")

# Printing final list configuration
print(f"\n✅ SYSTEM ACTIVE: {len(portfolio_tracks)} tracking paths fully live.")
