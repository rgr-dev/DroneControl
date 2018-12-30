import paho.mqtt.client as mqtt
import time


class MQTTSubscriber:

    CODE_MESSAGES = {0: "Connection successful",
                     1: "Connection refused - incorrect protocol version",
                     2: "Connection refused - invalid client identifier",
                     3: "Connection refused - server unavailable",
                     4: "Connection refused - bad username or password",
                     5: "Connection refused - not authorised",
                     6: "Unknow Error Code (6-255)"}

    def __init__(self, logger, topic="roger/test", host="iot.eclipse.org", port=1883, keep_alive=60):
        self.log = logger
        self.topic = topic
        self.host = host
        self.port = port
        self.keep_alive = keep_alive
        self.connected = False
        self.client = mqtt.Client()

    # The callback for when the client receives a CONNACK response from the server.
    def _on_connect(self, client, userdata, flags, rc):
        print("Connected with result code %s. ", str(rc))
        self.log.debug("Connected with result code %s", str(rc))
        self.log.info(self.process_returncode(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(self.topic)
        self.connected = True

    def _on_disconnect(self, client, userdata, rc):
        client.unsubscribe()
        print("Disconnected from the broker.")
        self.log.debug("Disconnected from the broker.")
        self.connected = False


    # The callback for when a PUBLISH message is received from the server.
    def _on_message(self, client, userdata, msg):
        self.log.debug("Message: %s, Topic: %s", msg.payload.decode(), msg.topic)
        self.log.info("Incoming Message: %s", msg.payload.decode())
        print(msg.topic + " " + str(msg.payload))

    def run(self):
        self.log.info("Init MQTT Broker connection...")
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect

        self.log.info("Connecting with [b]Topic:[/b]\"[color=#0000cc]%s[/color]\" "
                      "[b]host:[/b][color=#0000cc] %s[/color] "
                      "[b]port:[/b][color=#0000cc]%s[/color]",
                      self.topic, self.host, self.port)
        self.client.connect(self.host, self.port, self.keep_alive)

    def disconnect(self):
        self.log.info("Disconnecting from MQTT Broker channel...")
        self.client.loop_stop()
        self.client.disconnect()
        self.log.info("MQTT connection finished.")

    def fast_connection(self):
        """
        Init a connection directly whithout init callbacks

        NOTE: Callbacks most be Setted
        """
        self.log.info("Connecting...")
        time.sleep(1)
        self.client.connect(self.host, self.port, self.keep_alive)
        self.log.info("Now Connected,")
        self.client.loop_start()

    def start_listener(self):
        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        # self.client.loop_forever()
        self.client.loop_start()

    def stop_listener(self):
        self.client.loop_stop()

    def is_connected(self):
        return self.connected

    def process_returncode(self, code):
        if code == 0:
            return self.CODE_MESSAGES[0]
        elif code == 1:
            return self.CODE_MESSAGES[1]
        elif code == 2:
            return self.CODE_MESSAGES[2]
        elif code == 3:
            return self.CODE_MESSAGES[3]
        elif code == 4:
            return self.CODE_MESSAGES[4]
        elif code == 5:
            return self.CODE_MESSAGES[5]
        elif code >= 6:
            return self.CODE_MESSAGES[6]
