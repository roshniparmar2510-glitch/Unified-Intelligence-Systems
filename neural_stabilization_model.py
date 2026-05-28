# Computational Neuroscience Model: Brainwave Telemetry Stabilization Matrix
# Evaluates neural frequency variance during deep creative states

def analyze_neural_stability(frequency_tracks):
    print("🧠 Initializing Neural Telemetry Data Scan...")
    
    for track_id, frequencies in frequency_tracks.items():
        # Calculate the mathematical spread (Max frequency - Min frequency)
        variance_spread = max(frequencies) - min(frequencies)
        
        print(f"\nScanning Profile: {track_id.upper()}")
        print(f" -> Frequency Range: {frequencies}")
        print(f" -> Calculated Signal Spread: {variance_spread:.2f} Hz")
        
        # Criteria: A spread under 5.00 Hz indicates stabilization
        if variance_spread <= 5.00:
            print(" -> STATUS: ✅ STABILIZATION CRITERIA MET (Deep Focus Confirmed)")
        else:
            print(" -> STATUS: 💤 ERRATIC SIGNAL DETECTED (Standard Baseline)")

# Simulated telemetry tracks from Dr. Vance's lab artists
artist_telemetry_matrix = {
    "subject_alpha_focus": [12.4, 13.1, 11.9, 14.2, 12.8],
    "subject_beta_baseline": [8.5, 19.2, 11.4, 24.1, 7.3]
}

analyze_neural_stability(artist_telemetry_matrix)
