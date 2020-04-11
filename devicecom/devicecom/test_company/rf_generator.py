import sefra

class rf_generator_channel(sefra.epics.device):
    def __init__(self, parent, channel):
        super(rf_generator_channel, self).__init__("CH" + str(channel), parent=parent)
        self.channel = channel

        self.state = {}

    @sefra.epics.pv_set(type="int")
    def set_output(self, value):
        print("set_output ", self.channel, value)
        self.state["output"] = value

    @sefra.epics.pv_get(type="string")
    def get_output(self):
        value = self.state.get("output", 0)
        print("get_output ", self.channel, value)
        return value

    @sefra.epics.pv_set(type="float")
    def set_frequency(self, value):
        print("set_frequency ", self.channel, value)
        self.state["frequency"] = value

    @sefra.epics.pv_get(type="float") 
    def get_frequency(self):
        value = self.state.get("frequency", 0)
        print("get_frequency ", self.channel, value)
        return value


class rf_generator(sefra.epics.device):
    def __init__(self, name, server=False):
        print("Init Test device, ", name)
        super(rf_generator, self).__init__(name, server=server)

        self.channels = {}
        self.channels[1] = rf_generator_channel(self, 1)
        self.channels[2] = rf_generator_channel(self, 2)
        
    def channel(self, number):
        return self.channels.get(number, None)

    @sefra.epics.pv_get(type="string")
    def idn(self):
        return "test_device " + self.name



if __name__ == "__main__":

    some_config = {}
    ts = rf_generator("TEST:RF_DEVICE0", server=True)
    ts.start()
