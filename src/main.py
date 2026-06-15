import time
import random
import json
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - [IoT Module] - %(levelname)s - %(message)s'
)

def get_sensor_data():
    """Simulates reading data from physical sensors connected to the edge gateway."""
    temperature = round(random.uniform(15.0, 35.0), 2)
    humidity = round(random.uniform(30.0, 80.0), 2)
    
    return {
        "device_id": "edge-gateway-alpha-01",
        "temperature_c": temperature,
        "humidity_percent": humidity,
        "sensor_status": "OK"
    }

def main():
    logging.info("Starting IoT Edge Sensor Module...")
    logging.info("Initializing connection to local MQTT broker...")
    
    time.sleep(2) 
    logging.info("Connected successfully. Ready to transmit data.")

    try:
        while True:
            data = get_sensor_data()
            payload = json.dumps(data)
            
            logging.info(f"Publishing Telemetry -> {payload}")
            
            time.sleep(5) 
            
    except KeyboardInterrupt:
        logging.info("Module shutdown requested.")
    except Exception as e:
        logging.error(f"Module encountered a critical error: {e}")

if __name__ == "__main__":
    main()
