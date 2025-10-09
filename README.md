# Parkme Data Management

## Overview

This contains code for the management and display of data across the Parkme custom hardware parking monitor and two main display endpoints:
1. **User Client:** custom web client for viewing parking accessablilty
2. **Admin Client:** grafan web client for viewing parking usage data over time, as well as monitoring parking habits


## Admin Data

Illegal parking alerts

lot popularity

per hour per lot spot occupancy

per day per lot avg nof cars at a given time. (whole year)

current occupancy

map of most used locations


## Client Data

Current occupancy

Open spot locations

## Data Structure

lot tables

Lot
{
  "lot_id": uuid4,
  "name"
  "nof_spots"
  "location"
  "desc"
}

ParkMe Sensor
{
  "location": gps
  "report_ms": int
}

Report
{
  "lot_id": uuid4, -> tag
  "space_id": uuid4 -> tag
  "parkme_id": uuid4 -> tag
  "ts": time
  "is_full": bool
  "is_illegal": bool
}

Space
{
  "lot_id": uuid4,
  "space_id": uuid4
  "location": gps
}

