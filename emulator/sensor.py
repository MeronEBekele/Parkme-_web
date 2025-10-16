
sensors:
  - id: "emulated_01"
    lat: 37.774929
    lon: -122.419416
    interval_ms: 1000
    lot_id: "lot_a"

from utils import Location

class Sensor:
    def __init__(self, sensor_config, defined_lots):
        self.id = sensor_config.get("id")
        self.location = Location(sensor_config.get("lat", None), sensor_config.get("lon", None))
        self.desc = description
