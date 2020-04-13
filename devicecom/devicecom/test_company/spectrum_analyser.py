import sefra
import threading
import random
import time

class spectrum_analyser_channel(sefra.epics.device):
    def __init__(self, parent, channel):
        super(spectrum_analyser_channel, self).__init__("CH" + str(channel), parent=parent)
        self.channel = channel

        self.state = {}
        self.stream_run = False
        self.tid = 0


    @sefra.epics.pv_get(type="float", count=100)
    def get_spectrum(self):
        print("get_spectrum")
        ret = [random.randint(1,40) for i in range(50)]
        return ret

    @sefra.epics.pv_set(type="float")
    def set_center(self, value):
        print("set_center ", self.channel, value)
        self.state["center"] = value

    @sefra.epics.pv_get(type="float") 
    def get_center(self):
        value = self.state.get("center", 0)
        print("get_center ", self.channel, value)
        return value

    @sefra.epics.pv_set(type="float")
    def set_span(self, value):
        print("set_span ", self.channel, value)
        self.state["span"] = value

    @sefra.epics.pv_get(type="float") 
    def get_span(self):
        value = self.state.get("span", 0)
        print("get_span ", self.channel, value)
        return value

    @sefra.epics.pv_set(type="int")
    def set_stream(self, value):
        print("set_stream ", self.channel, value)
        if value == 0: #Stop Stream
            self.stream_run = False
        else: #Start Stream
            self.stream_run = True
            self.tid = threading.Thread(target=self.run_stream)
            self.tid.start()


    #One can use pv_get for function without arguments
    @sefra.epics.pv_get(type="int") 
    def stream_on(self):
        self.set_stream(1)
        return 1

    @sefra.epics.pv_get(type="int") 
    def stream_off(self):
        self.set_stream(0)
        return 0

    def run_stream(self):
        while self.stream_run:
            time.sleep(0.5)
            ret = [random.randint(1,40) for i in range(50)]
            self.get_spectrum.set(ret)
            

class spectrum_analyser(sefra.epics.device):
    def __init__(self, name, server=False):
        print("Init Test device, ", name)
        super(spectrum_analyser, self).__init__(name, server=server)

        self.channels = {}
        self.channels[1] = spectrum_analyser_channel(self, 1)
        self.channels[2] = spectrum_analyser_channel(self, 2)
        
    def channel(self, number):
        return self.channels.get(number, None)

    @sefra.epics.pv_get(type="string")
    def idn(self):
        return "test_device " + self.name



