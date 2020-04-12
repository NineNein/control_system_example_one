import devicecom

config = {
    "rotating wall" : {
        "host" : "Kronos",  #Will start on Computer named Kronos, or specfied Ip
        "autostart" : True,
        "autorestart" : False,
        "server_class" : devicecom.test_company.rf_generator.rf_generator,
        "server_args" : ( 
            "TEST:RW",
        )
    },

    "voltage source" : {
        "host" : "Kronos",  #Will start on Computer named Kronos, or specfied Ip
        "autostart" : True,
        "autorestart" : False,
        "server_class" : devicecom.test_company2.voltage_source.voltage_source,
        "server_args" : ( 
            "TEST:VOLTAGE",
            {
                "name" : "some config",
                "value" : 2,
            }
        )
    },

    "science trap" : {
        "host" : "Kronos",  #Will start on Computer named Kronos, or specfied Ip
        "autostart" : True,
        "autorestart" : False,
        "server_class" : devicecom.myexperiment.penning_trap.penning_trap,
        "server_args" : ( 
            "TEST:SCIENCE_TRAP",
            {
                "voltage_source" : "TEST:VOLTAGE",
                "UEC" : 1,
                "UCE" : 2,
                "RING" : 3,
                "LCE" : 4,
                "LEC" : 5,
                "TR" : 0.5
            }
        )
    }
}