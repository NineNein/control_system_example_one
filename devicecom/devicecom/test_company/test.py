import rf_generator as rf 

import time 

dev = rf.rf_generator("TEST:DEVICE0")

print(dev.idn())


dev.channel(1).set_frequency(3E3)

print(dev.channel(1).get_frequency())
print(dev.channel(2).get_frequency())



dev.channel(1).set_output(0)
print(dev.channel(1).get_output())

dev.channel(1).set_output(1)
print(dev.channel(1).get_output())


# dev = rf.rf_generator("TEST:DEVICE1")

# print(dev.idn())


# dev.channel(1).set_frequency(3E3)

# print(dev.channel(1).get_frequency())
# print(dev.channel(2).get_frequency())



# dev.channel(1).set_output(0)
# print(dev.channel(1).get_output())
# time.sleep(2)
# dev.channel(1).set_output(1)
# print(dev.channel(1).get_output())