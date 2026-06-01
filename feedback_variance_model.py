# Computational Neuroscience Model: Neural Network Feedback Optimization
# Concept: Tracking adaptive processing states across a multi-layered matrix

system_nodes = {"layer_alpha": 14.50, "layer_beta": 12.40, "layer_gamma": 15.30}
stabilization_threshold = 5.00

print("⚡ Initializing Adaptive Feedback Variance Optimization...\n")

for layer, variance in system_nodes.items():
    print(f"🔬 Analyzing {layer.upper()}...")
    print(f"   -> Raw Variance: {variance} Hz")
    
    # Calculate the optimization target distance
    distance_to_target = variance - stabilization_threshold
    print(f"   -> Distance to Target Base: {distance_to_target:.2f} Hz")
    
    if variance > stabilization_threshold:
        print("   ⚠️ STATUS: Optimization required. Calibrating system loops.\n")
    else:
        print("   ✅ STATUS: Stable state achieved.\n")
