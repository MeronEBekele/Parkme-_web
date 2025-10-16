from utils import Location

class Lot:
    def __init__(self, lot_config):
        self.id = lot_config.get("id")
        self.location = Location(lot_config.get("lat", None, lot_config.get("lon", None))
        self.desc = description
