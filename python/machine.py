import serial
import time
import pickle

class Machine:
    def __init__(self, machine_type):
        self.machine = None
        self.machine_type = machine_type  # "laser", "3d", "cnc", "custom".
        self.comm_port = comm_port
        self.baud_rate = baud_rate
        # self.custom_machines = []
        # self.comm_port = None
        self.x_limit = None
        self.y_limit = None
        self.z_limit = None

    def _write_custom(self, machine_settings):
        name = machine_settings["name"]
        path_to_custom = F"python/Machines/{name}.pickle"
        with open(path_to_custom, 'wb') as file:
            pickle.dump(machine_settings, file)
    
    def _load_custom(self):
        path_to_custom = F"python/Machines/{self.machine_type}.pickle"
        try:
            with open(path_to_custom, 'rb') as file:
                custom_machines = pickle.load(file)
            return custom_machines
        except:
            return False

    def connect(self):
        if self.machine_type == "3d":
            self.machine = serial.Serial(self.comm_port, self.baud_rate)
            time.sleep(5)
            # Wait for response from machine.
        elif self.machine_type == "laser":
            pass
        elif self.machine_type == "cnc":
            pass
        elif self._load_custom(self.machine_type):
            settings = self._load_custom(self.machine_type)
            self.machine = serial.Serial(settings["port"], settings["baud"])
   
    def send_command(self, command):
        if self.machine:
            self.machine.write(bytes(F"{command}\r\n", "UTF-8"))
