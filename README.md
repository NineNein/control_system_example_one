# Control_system_example_one
Example how one could build a control system for small to medium sized experiments.
This is not the best Control System Pattern in the world but it is a tribute.


## Ideas/Reasons for this Pattern
Pros:
- Simple Integration of an GUI, and display of the state of the experiment e.g. Amplitude of some RF Generator
- Build in support for more Computers, which handles different devices

Cons:
- More Complex than one simple experiment class running on one computer
- Most proably slower than a simple implementation, but anyhow time critical think should not be done on non realtime systems?


I considere writing Epics server for all the devices exausting, but with the sefra class it gets managable.



# Installation

- Install Sefra Package, see sefra package
- Fork/Copy Project
- Install **devicecom** and **experiment** package in develop modus:
In you favorite console change path to where the setup.py is located then use:
```
python setup.py develop
```

- Edit the config next to server_manager, change Host to the hostname or ip of your current Computer.
- start server_manager.py
- Start CMD Control

# The Pattern

There are two packages, the deviceom package and the experiment package.

The Devicecom package should include all class which are nessary for comunicating with the instruments. It
also includes the server_manager and the the config which defines where to start which server.

The Experiment package includes the experiment class. This class should model the experiment. The package also
includes a config which links all used devices to their PV names.

The simples way to control the experiment would be to use your fav. python console e.g. ipython and initalize the experiment class. For an example, see section CMD Control.

The package abstract the use of Epics, but it is still nessary to understand how epics works.




# CMD Control
Command Line Control

Use your fav. Python Console e.g. IPython
```from init_experiment import *```

# When abastraction server makes sense?
- When epics compatible types can be used
- When Information should be global available


# TODOs: 
- Add Plotserver for easy plotting
- Make ServerManager more functional, e.g. also a Epics server, Start Stop servers, monitor options, logging of error messages...

