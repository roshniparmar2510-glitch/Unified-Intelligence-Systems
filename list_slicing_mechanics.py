# Programming Foundation: Data Array Slicing Mechanics

# A list of scientific parameters for data tracking
scientific_metrics = ["Velocity", "Mass", "Force", "Density", "Volume"]

print("🔬 Initializing Scientific Data Array...\n")
print(f"📊 Full Matrix: {scientific_metrics}")

# In Python slicing, list[start:stop] includes the start index but EXCLUDES the stop index!
# We want to extract "Mass", "Force", and "Density" (Indices 1, 2, and 3)
extracted_subset = scientific_metrics[1:4]

print(f"✂️ Sliced Segment (Indices 1 to 3): {extracted_subset}")
print(f"\n✅ CAPABILITY LOGGED: Subset holds {len(extracted_subset)} metrics.")
