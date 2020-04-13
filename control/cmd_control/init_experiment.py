import experiment
import time


exp = experiment.experiment(experiment.config)



def onChanges(pvname=None, value=None, char_value=None, **kw):
    print('PV Changed! ', pvname, char_value, time.ctime())


def test():
    exp.st.set_depth(-33)
    exp.st.set_tr(0.15)

    exp.spec.channel(1).get_spectrum.add_callback(onChanges)


    exp.spec.channel(1).stream_on()


    while True:
        time.sleep(1)
