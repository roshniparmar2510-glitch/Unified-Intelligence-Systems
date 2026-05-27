# Computational Neuroscience Model: Spatial Coordinate Boundary Tracking
# Based on the Circle Equation: (x - h)^2 + (y - k)^2 = r^2

center_h, center_k = 5, -2  # Center coordinates of the cognitive boundary
radius = 7  # Radius boundary limit
radius_squared = radius ** 2

# Test coordinates representing incoming sensory data packets (X, Y)
test_coordinates = [(6, -1), (12, 5), (4, -3), (10, 10)]

print("🌐 Initializing Spatial Coordinate Boundary Analysis...\n")

for x, y in test_coordinates:
    # Calculating spatial distance metric: (x - h)^2 + (y - k)^2
    distance_metric = (x - center_h)**2 + (y - center_k)**2
    
    if distance_metric <= radius_squared:
        print(f"✅ WITHIN BOUNDARY: Coordinate ({x}, {y}) is inside the processing zone.")
    else:
        print(f"❌ OUTSIDE BOUNDARY: Coordinate ({x}, {y}) exceeds spatial radius limits.")
