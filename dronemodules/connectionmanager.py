import socket
import time
import _pickle as cPickle

from dronemodules.mqqsubscriber import MQTTSubscriber

class DroneConnectionDriver:

    def __init__(self, logger, sock_host, sock_port=50000):
        self.logger = logger
        self.sock_host = sock_host
        self.sock_port = int(sock_port)

    def init_comm_config_process(self):
        try:
            self.logger.info("Initializing Drone communication...")
            # Paso 1 Connectar con el drone
            self._establish_drone_connection()
            # Paso 2 Pedir datos de conexion y credenciales MQTT
            # Paso 3 Connectarse al broker MQTT y subscribirse al topico correspondiente
            self._MQTT_connection()
            while not self.__mqtt_subs.is_connected():
                time.sleep(1)
            self.logger.info("All Communication config finished successfully.")
        except ConnectionRefusedError:
            self.logger.error("Cannection Refused. Maybe the drone is power off?")

    def _establish_drone_connection(self):
        self.logger.info("Connecting with drone...")
        self.__socket_client = SocketClientManager(self.logger, self.sock_host, self.sock_port)
        self.logger.info("Connection successful.")

    def _MQTT_connection(self):
        self.logger.info("Getting configurations from Drone..")
        data = self._get_MQTT_config()
        config = cPickle.loads(data)
        self.logger.info("Configuration Obtained")
        # MQTT subscriber ready!
        self.__mqtt_subs = MQTTSubscriber(self.logger, config['Topic'], config['Host'], config['Port'])
        self.__mqtt_subs.run()
        self.__mqtt_subs.start_listener()

    def _get_MQTT_config(self):
        return self.send_rec_message('$CM-01')

    def send_rec_message(self, msg):
        return self.__socket_client.send_rec_message(msg)

    def stop_drone_connection(self):
        self.logger.info("Stopping communications with the Drone..")
        self.__socket_client.close_connection()
        self.__mqtt_subs.disconnect()



class SocketClientManager:

    def __init__(self, logger, host, port):
        self.host = host
        self.port = port
        self.logger = logger
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.open_connection()

    def open_connection(self):
        self.sock.connect((self.host, self.port))

    def close_connection(self):
        self.sock.close()
        self.logger.info("Socket connection closed.")

    def send_message(self, message):
        self.logger.debug("Sending message: %s", message)
        self.sock.sendall(message.encode())

    def send_rec_message(self, msg):
        self.logger.debug("Sending message: %s", msg)
        self.sock.sendall(msg.encode())
        data = self.sock.recv(1024)
        self.logger.debug("Received message: %s", cPickle.loads(data))
        return data

    def send_rec_decoded_message(self, msg):
        return self.send_rec_message(msg).decode()