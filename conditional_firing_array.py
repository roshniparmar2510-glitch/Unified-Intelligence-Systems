# Computational Neuroscience Model: Conditional Neural Threshold Firing
sensory_signals = [0.42, 0.68, 0.89, 0.55, 0.94, 0.31]
firing_threshold = 0.70  # The minimum action potential needed to fire

print("⚡ Initializing Neural Firing Array Analysis...\n")

for signal in sensory_signals:
    if signal >= firing_threshold:
        print(f"🔥 ACTION POTENTIAL REACHED: Signal {signal} crossed threshold. Neuron Fired!")
    else:
        print(f"💤 Signal {signal} insufficient. Neuron remains latent.")
