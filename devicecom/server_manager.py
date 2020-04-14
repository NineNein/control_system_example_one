from devicecom.config import config
import socket
import multiprocess
import time


class server_manager:
    def __init__(self, config):
        self.config = config
        self.pids = {}

    def run(self, cfg):
        pinstance = cfg["server_class"](*cfg["server_args"], server=True)
        pinstance.start()
        print("Finished")

    def start(self):
        host_name = socket.gethostname()
        ip_addr = socket.gethostbyname(host_name) 

        for name, cfg in self.config.items():
            print("Init ", name)

            if cfg["host"] not in [host_name, ip_addr]:
                continue

            p = multiprocess.Process(target=self.run, args=(cfg,))
            p.start()
            print(p.pid)

            self.pids[name] = p

    def update_config(self):
        #While running update config...more complicated to implement
        pass

    def keep_running(self):
        while True:
            time.sleep(0.5)
            for name, p in self.pids.items():
                if p.is_alive():
                    continue

                print("Restart ", name)
                cfg = self.config[name]
                p = multiprocess.Process(target=self.run, args=(cfg,))
                p.start()
                print(p.pid)
                self.pids[name] = p

            

if __name__ == "__main__":

    sm = server_manager(config)
    sm.start()

    sm.keep_running()

