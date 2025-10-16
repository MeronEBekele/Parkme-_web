
from influxdb_client import InfluxDBClient, WriteApi
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxConfig:
    self.host : str = ""
    self.port : str = ""
    self.org : str = ""
    self.token : str = ""
    self.client : InfluxDBClient = None

    def is_valid(self) -> bool:
        return self.host and self.port and self.org and self.token

class InfluxHandler:
    def __init__(self):
        self.config = InfluxConfig()

    def __repr_():
        return f"PORT: {self.port}, HOST: {self.host}, ORG: {self.org}, TOKEN: {self.token}"

    def from_env(self):
        self.config.host = os.getenv("DOCKER_INFLUXDB_INIT_HOST")
        self.config.port = os.getenv("DOCKER_INFLUXDB_INIT_PORT")
        self.config.org = os.getenv("DOCKER_INFLUXDB_INIT_ORG")
        self.config.token = os.getenv("DOCKER_INFLUXDB_INIT_ADMIN_TOKEN")

        if not self.config.is_valid():
            raise RuntimeError(f"Invalid config passed to influxDB {self.config}")

        self.config.client = InfluxDBClient(
            f"http://{influxdb_host}:{influxdb_port}",
            org=influxdb_org,
            token=influxdb_token
        )

    def send_message(self, record : dict):
        with self.config.client.write_api(write_options=SYNCHRONOUS) as write_api:
            try:
                utc_timestamp = datetime.utcnow()
                formatted_timestamp = utc_timestamp.strftime("%Y-%m-%dT%H:%M:%SZ")
                self.influx_push(write_api, bucket='rtusystem', record_time_key="time", record=record)
                logging.debug(f"[{self.config.container_id}]: {message_text}")
            except Exception as e:
                logging.error(f"send_message failed with error: {e}")

    def influx_push(self, write_api: WriteApi, *args, **kwargs) -> None:
        while True:
            try:
                write_api.write(*args, **kwargs)
                break
            except ConnectionError as e:
                logging.warning(f"Error pushing data: {e}. Retrying...")
                time.sleep(1)
