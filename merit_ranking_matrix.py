# Technical Base Expansion: Automated Merit Ranking Matrix
# Concept: Filtering and processing high-aptitude student data profiles

student_records = {
    "applicant_01": {"score": 94, "status": "Pending"},
    "applicant_02": {"score": 78, "status": "Pending"},
    "applicant_03": {"score": 91, "status": "Pending"},
    "applicant_04": {"score": 85, "status": "Pending"}
}

merit_threshold = 90

print("🏆 Initializing Scholarship Merit Verification Matrix...\n")

for student, profile in student_records.items():
    print(f"🔬 Evaluating {student.upper()} | Raw Aptitude Score: {profile['score']}%")
    
    # Conditional logic array to update structural parameters
    if profile["score"] >= merit_threshold:
        profile["status"] = "MERIT LIST CONFIRMED"
        print(f"   -> Result: {profile['status']} (Passes Filter)\n")
    else:
        profile["status"] = "Standard Tier"
        print(f"   -> Result: {profile['status']} (Awaiting Review)\n")

print("🏁 DATA STREAM CALIBRATED: Filtering loops completed successfully.")
