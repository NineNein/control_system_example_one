import sefra
import devicecom


class penning_trap(sefra.epics.device):
    def __init__(self, name, config = {}, server=False):
        print("Init Test device, ", name)
        super(penning_trap, self).__init__(name, server=server)
        self.config = config

        self.vs = devicecom.test_company.voltage_source.voltage_source(self.config["voltage_source"])

        self.UEC = vs.channel(self.config["UEC"])
        self.UCE = vs.channel(self.config["UCE"])
        self.RING = vs.channel(self.config["RING"])
        self.LCE = vs.channel(self.config["LCE"])
        self.LEC = vs.channel(self.config["LEC"])

        self.tr = self.config["TR"]


    @sefra.epics.pv_set(type="float")
    def set_depth(self, value):
        #In real life it makes sense to determine the order RING, CE or other wiese around
        #by looking on the prev order.

        self.RING.set_voltage(value)
        self.UCE.set_voltage(value*self.tr)
        self.LCE.set_voltage(value*self.tr)

    @sefra.epics.pv_set(type="float")
    def set_tr(self, value):
        self.tr = value
        last_ring = self.RING.set_voltage.get()
        self.set_depth(last_ring)

    @sefra.epics.pv_set(type="float")
    def set_uec(self, value):
        self.UEC.set_voltage(value)

    @sefra.epics.pv_set(type="float")
    def set_lec(self, value):
        self.LEC.set_voltage(value)

    @sefra.epics.pv_set(type="float")
    def set_both_endcaps(self, value):
        self.UEC.set_voltage(value)
        self.LEC.set_voltage(value)

    @sefra.epics.pv_get(type="string")
    def get_voltages(self):
        return "voltages"

    @sefra.epics.pv_get(type="string")
    def idn(self):
        return "penning_trap" + self.name