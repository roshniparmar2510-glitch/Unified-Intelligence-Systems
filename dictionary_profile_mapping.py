# Programming Foundation: Tracking Data Profiles via Dictionaries

# Creating a dictionary to map university profile information
college_profile = {
    "target_university": "MIT",
    "required_math_score": 800,
    "financial_aid_status": "Need-Blind Full Ride"
}

print("📋 Initializing University Profile Data Extraction...\n")

# Extracting data using the exact text keys
university_name = college_profile["target_university"]
financial_policy = college_profile["financial_aid_status"]

print(f"🏛️ Destination Goal: {university_name}")
print(f"💰 Financial Strategy: {financial_policy}")

# Printing the total number of keys stored in this profile dictionary
total_keys = len(college_profile)
print(f"\n📊 Total active parameters stored in this data array: {total_keys}")
