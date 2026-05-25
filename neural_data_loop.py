# Computational Neuroscience Neural Data Loop
sensory_inputs = [0.5, 0.9, 1.2, 0.4, 1.8]

print("Processing incoming neural data streams...")

for data in sensory_inputs:
    if data > 1.0:
        print(f"⚠️ High Activity Detected: {data}")
    else:
        print(f"Normal Signal: {data}")
