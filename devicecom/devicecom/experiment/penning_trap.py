import sefra
import devicecom


class penning_trap(sefra.epics.device):
    def __init__(self, name, config = {}, server=False):
        print("Init Test device, ", name)
        super(penning_trap, self).__init__(name, server=server)
        self.config = config

        self.vs = devicecom.test_company.voltage_source.voltage_source(self.config["voltage_source"])


    def set_depth(self, value):
        pass

    def set_tr(self, value):
        pass

    def set_uec(self, value):
        pass

    def set_lec(self, value):
        pass

    def get_voltages(self):
        pass

    @sefra.epics.pv_get(type="string")
    def idn(self):
        return "voltage_source " + self.name