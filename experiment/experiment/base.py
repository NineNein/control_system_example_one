import devicecom
import experiment.config

import os
os.environ["PATH"] += os.pathsep + r"C:\Software\Anaconda3\Lib\site-packages\epics\clibs\win64"

class experiment:
    def __init__(self, config):
        self.config = config

        self.RW = devicecom.test_company.rf_generator.rf_generator(self.config["devices"]["rotating_wall"]["name"])
        self.trap_voltage = devicecom.test_company2.voltage_source.voltage_source(self.config["devices"]["trap_voltage"]["name"])
        self.st = devicecom.myexperiment.penning_trap.penning_trap(self.config["devices"]["science_trap"]["name"])
        self.spec = devicecom.test_company.spectrum_analyser.spectrum_analyser(self.config["devices"]["spectrum_analyser"]["name"])