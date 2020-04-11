import devicecom
import experiment.config

class experiment:
    def __init__(self, config):
        self.config = config

        self.RW = devicecom.test_company.rf_generator.rf_generator(self.config["devices"]["rotating_wall"]["name"])
        self.trap_voltage = devicecom.test_company2.voltage_source.voltage_source(self.config["devices"]["trap_voltage"]["name"])
        self.st = devicecom.experiment.penning_trap.penning_trap(self.config["devices"]["science_trap"]["name"])