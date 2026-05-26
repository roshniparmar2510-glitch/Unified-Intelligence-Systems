# Mapping unawakened brain layers using a Python Dictionary Matrix
neural_network_matrix = {
    "layer_1_focus": {"neurons": 12, "activation_threshold": 0.75, "status": "active"},
    "layer_2_memory": {"neurons": 24, "activation_threshold": 0.88, "status": "latent"},
    "layer_3_telemetry": {"neurons": 48, "activation_threshold": 0.95, "status": "unawakened"}
}

print("Scanning Latent Cognitive Network Matrix...\n")

# Looping through the dictionary keys and values seamlessly
for layer, attributes in neural_network_matrix.items():
    print(f"🧠 System: {layer.upper()}")
    print(f"   -> Capacity: {attributes['neurons']} nodes")
    print(f"   -> State: {attributes['status'].upper()}\n")
