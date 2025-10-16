import requests
import argparse
import yaml
import logging

from lot import Lot
from sensor import Sensor

# 1. send data at interval
# 2. randomize data

def configure():
    parser = argparse.ArgumentParser(
        description="An emulator that produces dummy parkme sensor data")
    parser.add_argument(
        "--config",
        type=pathlib.Path,
        required=True,
        help="Path of YAML config for the emulator")
    parser.add_argument("--log-level",
                    default="DEBUG",
                    help="Set the logging level. Options: DEBUG, INFO, WARNING, ERROR, CRITICAL")

    args = parser.parse_args()
    log_level = getattr(logging, args.log_level.upper(), 1)
    if not isinstance(log_level, int):
        raise RuntimeError("log level must me integer")

    logging.basicConfig(level=Config.log_level,
                    format='%(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

    yaml_options = None
    with open(str(args.config), 'r') as file:
        yaml_options = yaml.safe_load(file)

    return yaml_options

def main():
    config = configure()
    defined_lots = {}
    for lot_config in config.get("lots", []):
        defined_logs[lot_config.get("id")] = Lot(lot_config)


if __name__ == "__main__":
    main()
