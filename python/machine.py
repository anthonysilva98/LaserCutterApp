import serial
import time

class Machine:
    def __init__(self, machine_type, comm_port, baud_rate):
        self.machine = None
        self.machine_type = machine_type  # "laser", "3d", "cnc", "custom".
        self.comm_port = comm_port
        self.baud_rate = baud_rate
        # self.custom_machines = []
        # self.comm_port = None
        self.x_limit = None
        self.y_limit = None
        self.z_limit = None

    def connect(self):
        if self.machine_type == "3d":
            self.machine = serial.Serial(self.comm_port, self.baud_rate)
            time.sleep(5)
            # Wait for response from machine.
        elif self.machine_type == "laser":
            pass
        elif self.machine_type == "cnc":
            pass
        # elif self.machine_type in self.custom_machines:
        #     pass
    
    def send_command(self, command):
        if self.machine:
            self.machine.write(bytes(F"{command}\r\n", "UTF-8"))


if __name__ == "__main__":
    """Test `Machine` class on CR-10 3D printer."""
    from gcode_ops import Gcoderizer
    printer = Machine("3d", "/dev/ttyUSB0", 115200)
    printer.x_limit = 300
    printer.y_limit = 275
    printer.z_limit = 400
    printer.connect()

    gcode = Gcoderizer()
    gcode.canvas_dim_x = printer.x_limit
    gcode.canvas_dim_y = printer.y_limit
    gcode.plotter_dim_x = printer.x_limit
    gcode.plotter_dim_y = printer.y_limit

    printer.send_command(gcode.home())
    printer.send_command(gcode.gen_line(0, 0, 100, 100))
    

