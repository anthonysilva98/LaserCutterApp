class printer:
    def __init__(self):
        self.machine_type = None  # "laser", "3d", "cnc", "custom".
        self.custom_machines = []
        self.comm_port = None
        self.x_limit = None
        self.y_limit = None
        self.z_limit = None

    def connect(self, machine_type, comm_port):
        if machine_type == "3d":
            pass
        elif machine_type == "laser":
            pass
        elif machine_type == "cnc":
            pass
        elif machine_type in self.custom_machines:
            pass