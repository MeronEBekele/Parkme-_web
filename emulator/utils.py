
class Location:
    def __init__(self, lat, lon):
        if isinstance(lat, None) or isinstance(lon, None):
            raise RuntimeError("Latitude or Longitude is none!")

        self.latitude = lat
        self.longitude = lon

    def distance_from(self, other : Location):
        # Haversine formula
        EARTH_RADIUS_M = 6371000.0
        phi1, phi2 = math.radians(self.latitude), math.radians(other.latitude)
        dphi = math.radians(other.latitude - self.latitude)
        dlambda = math.radians(other.longitude - self.longitude)
        a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return EARTH_RADIUS_M * c
