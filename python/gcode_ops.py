class gcoderizer:
    def __init__(self):
        self.canvas_dim_x = 0
        self.canvas_dim_y = 0
        self.plotter_dim_x = 0
        self.plotter_dim_y = 0
        self.scale_x = self.plotter_dim_x / self.canvas_dim_x 
        self.scale_y = self.plotter_dim_y / self.canvas_dim_y 

    def gen_gcode(self, start_x, start_y, end_x, end_y):
        """
        Generate a Gcode command to move from `start_pt` to `end_pt`.
        Parameters:
            start_px: Starting position of a line, in canvas frame.
            end_px: Ending position of a line, in canvas frame.
        Returns:
            Gcode commands recreating the line in the plotter's frame.
        """

        plotter_start_x = start_x * self.scale_x
        plotter_start_y = start_y * self.scale_y
        plotter_end_x = end_x * self.scale_x
        plotter_end_y = end_y * self.scale_y

        gcode_command = F"G0 X{plotter_start_x} Y{plotter_start_y}\n"
        ## gcode_command += some command to activate/drop the plotter carriage.
        gcode_command += F"G1 X{plotter_end_x} Y{plotter_end_y}"
        ## gcode_command += some command to deactivate/lift the plotter carriage.

        return gcode_command
