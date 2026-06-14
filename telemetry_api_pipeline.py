# API Pipeline: Pushing Parser Metrics to Frontend Map
import json

# 1. Your existing Phase 2 telemetry parser output matrix
processed_matrix = [241.34, 57.12, -12.89]

def dynamic_map_api_payload(coordinates):
    """
    Packages the clean decimal matrix into a universal JSON packet 
    so the mobile interface can read it instantly.
    """
    payload = {
        "status": "ACTIVE_TRACKING",
        "latitude": coordinates[0],
        "longitude": coordinates[1],
        "altitude": coordinates[2],
        "system_fail_safe": "RESILIENT_OFFLINE_CACHE"
    }
    return json.dumps(payload)

# 2. Generate the live data packet
live_packet = dynamic_map_api_payload(processed_matrix)
print("📡 API Outbound Packet Transmitted:")
print(live_packet)
