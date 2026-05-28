# Computational Neuroscience Model: Brainwave Frequency Spread Tracking
# Analyzing gaps between Control Groups and Active Creative Processing

brainwave_data = {
    "subject_1": {"resting": 16.80, "creative_focus": 2.30},
    "subject_2": {"resting": 15.50, "creative_focus": 3.10},
    "subject_3": {"resting": 17.20, "creative_focus": 1.90}
}

print("📊 Initializing Neural Frequency Spread Logs...\n")

for subject, metrics in brainwave_data.items():
    # Calculating the arithmetic difference (spread) between states
    spread = metrics["resting"] - metrics["creative_focus"]
    
    print(f"🔬 {subject.upper()}:")
    print(f"   -> Resting Baseline: {metrics['resting']} Hz")
    print(f"   -> Creative State: {metrics['creative_focus']} Hz")
    print(f"   -> Delta Spread: {spread:.2f} Hz\n")
