# Parkme Data Management

## Overview

This contains code for the management and display of data across the Parkme custom hardware parking monitor and two main display endpoints:
1. **User Client:** custom web client for viewing parking accessablilty
2. **Admin Client:** grafan web client for viewing parking usage data over time, as well as monitoring parking habits


## Admin Data

1. Lot popularity
2. per hour per lot spot occupancy
3. per day per lot avg nof cars at a given time. (whole year)
4. current occupancy
5. map of most used locations


## Client Data

1. Current occupancy
2. Open spot locations

## Data Structure

### Lot
```json
{
  "lot_id": uuid4,
  "nof_spots": int,
  "location": gps,
  "desc": str
}
```

### ParkMe Module
```json
{
  "lot_id": uuid4,
  "location": gps,
  "report_ms": int
}
```

### Report
```json
{
  "lot_id": uuid4,
  "space_id": uuid4,
  "parkme_id": uuid4,
  "is_full": bool
}
```

### Space
```json
{
  "lot_id": uuid4,
  "space_id": uuid4,
  "location": gps
}
```

