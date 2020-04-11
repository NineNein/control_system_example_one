import sefra

class voltage_source_channel(sefra.epics.device):
    def __init__(self, parent, channel):
        super(voltage_source_channel, self).__init__("CH" + str(channel), parent=parent)
        self.channel = channel
        self.state = {}

    @sefra.epics.pv_set(type="float")
    def set_voltage(self, value):
        print("set_voltage ", self.channel, value)
        self.state["voltage"] = value

    @sefra.epics.pv_get(type="float") 
    def get_voltage(self):
        value = self.state.get("voltage", 0)
        print("voltage ", self.channel, value)
        return value


class voltage_source(sefra.epics.device):
    def __init__(self, name, config = {}, server=False):
        print("Init Test device, ", name)
        super(voltage_source, self).__init__(name, server=server)

        self.config = config

        self.channels = {}
        for i in range(10):
            self.channels[i] = voltage_source_channel(self, i)
        
        
    def channel(self, number):
        return self.channels.get(number, None)

    @sefra.epics.pv_get(type="string")
    def idn(self):
        return "voltage_source " + self.name



if __name__ == "__main__":

    some_config = {}
    ts = rf_generator("TEST:VOLTAGE_DEVICE0", config = some_config, server=True)
    ts.start()
