# Phase 2 Engineering: Space Telemetry Network Parser
# Concept: Extracting numeric data arrays from raw system text blocks

# Simulated raw telemetry feed from an orbital network tracking line
raw_telemetry_stream = "OBJECT=MARS;COORDS=241.34,57.12,-12.89;STATUS=ACTIVE"

print("📡 Initializing Phase 2 Network Stream Parser...\n")
print(f"📥 Raw Incoming Data: {raw_telemetry_stream}\n")

# 1. Splitting the raw stream by semicolons to isolate blocks
data_segments = raw_telemetry_stream.split(";")

# 2. Extracting the coordinate block (Index position 1)
raw_coords = data_segments[1] # Yields "COORDS=241.34,57.12,-12.89"
clean_coords = raw_coords.split("=")[1] # Yields "241.34,57.12,-12.89"

# 3. Converting the plain text coordinates into mathematical decimals (floats)
coordinate_list = [float(x) for x in clean_coords.split(",")]

print(f"🛰️ Target Object Identifer: {data_segments[0].split('=')[1]}")
print(f"📊 Processed Decimal Matrix: {coordinate_list}")
print(f"📈 Extracted X-Axis Vector:  {coordinate_list[0]}")
print(f"🏁 System Status Flag:      {data_segments[2].split('=')[1]}")
