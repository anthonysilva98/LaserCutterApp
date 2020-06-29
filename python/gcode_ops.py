from machine import Machine


class Gcoderizer:
    """
    The `Gcoderizer` class handles the creation and formation of g-code commands.
    G-code is generated to be machine specific in terms of type and size.

    Attributes:
        canvas_dim_(x/y) - Dimensions of canvas, using canvas units (px).
        plotter_dim(x/y) - Dimensions of plotter, using plotter units (m, mm, in).
    """
    def __init__(self):
        self.canvas_dim_x = 1
        self.canvas_dim_y = 1
        self.plotter_dim_x = 1
        self.plotter_dim_y = 1
        self.scale_x = self.plotter_dim_x / self.canvas_dim_x 
        self.scale_y = self.plotter_dim_y / self.canvas_dim_y
    
    def load(self, name):
        settings = Machine(name)._load_custom()
        self.plotter_dim_x = settings["x_lim"]
        self.plotter_dim_y = settings["y_lim"]

    def _in_canvas_bounds(x_points, y_points):
        """
        Ensure that machine will not be given instructions to move beyond it's bounds.
        If x-y-points are within bounds, proper scaling will ensure that the
        plotter position is always within it's limits.
        Parameters:
            x_points, y_points - X-y-points to compare to canvas boundaries.
        
        Returns:
            True - If x-y-points are within the bounds of the canvas.
            False - If x-y-points are out of the canvas' bounds.
        """
        try:
            assert min(x_points) >= 0
            assert min(y_points) >= 0
            assert max(x_points) <= self.canvas_dim_x
            assert max(y_points) <= self.canvas_dim_y
        except:
            return False

        return True


    def gen_line(self, start_x, start_y, end_x, end_y):
        """
        Generate a Gcode command to move from `start_pt` to `end_pt`.
        Parameters:
            start_px: Starting position of a line, in canvas frame.
            end_px: Ending position of a line, in canvas frame.
        Returns:
            Gcode commands recreating the line in the plotter's frame.
        """

        if not self._in_canvas_bounds([start_x, end_x], [start_y, end_y]):
            print("Illegal canvas boundary supplied as parameter.\n")
            quit()

        plotter_start_x = round(start_x * self.scale_x, 1)
        plotter_start_y = round(start_y * self.scale_y, 1)
        plotter_end_x = round(end_x * self.scale_x, 1)
        plotter_end_y = round(end_y * self.scale_y, 1)

        gcode_command = F"G0 Z10\n"
        gcode_command += F"G0 X{plotter_start_x} Y{plotter_start_y}\n"
        gcode_command += F"G0 Z2\n"
        gcode_command += F"G1 X{plotter_end_x} Y{plotter_end_y}\n"
        gcode_command += F"G0 Z10\n"

        return gcode_command

    def home(self):
        return "G28"

    def stop(self):
        return "M18"