

class Resources():
    def __init__(self):
        self.output_ports = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.output_currs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.liquids      = [0, 0, 0, 0, 0]
        self.temperature  = [0, 0, 0]
        self.pressure     = [0, 0, 0]
        self.humidity     = [0, 0, 0]
        self.gas          = [0, 0, 0]
        self.total_curr   = 0.0
        self.relays       = 0
        self.ac_state     = True
        self.temp_on      = True
        self.ac_temp      = 22
        self.anti_freez   = False