from multiprocessing import Process, Lock
from ftplib import FTP
import json


class Copier:
    def login(self, server, login, passwd):
        ftp = FTP(server)
        try:
            ftp.login(login, passwd)
        except:
            print("Login in {} with login = {} and pass = {} not successful".format(server, login, passwd))
            return None
        return ftp

    def read_json(self):
        try:
            with open(self.input_json, "r") as external:
                self.data = json.load(external)
        except FileNotFoundError:
            self.json_exist = False
            print("json does not exists")

    def __init__(self, input_json):
        self.input_json = input_json
        self.data = None
        self.json_exist = True
        self.read_json()

    def sub_load(self, server, file, path, lock):
        lock.acquire()
        try:
            server.cwd(path)
            try:
                with open(file, "rb") as f:
                    server.storbinary("STOR %s" % file, f)
            except:
                print("{} have not been upload".format(file))
        finally:
            lock.release()


    def load_file(self):
        if self.json_exist:
            data = self.data.popitem()
            server = self.login(data[0], data[1].get("user"), data[1].get("pass"))
            if server:
                procs = []
                files = data[1].get("files")
                path = data[1].get("path")
                lock = Lock()
                for i in range(len(files)):
                    proc = Process(target=self.sub_load, args=(server, files[i], path[i], lock))
                    procs.append(proc)
                    proc.start()
                for proc in procs:
                    proc.join()
            else:
                print("you are not logged in")
        else:
            print("You can not upload. Json does not exist.")


x = Copier("data.json")
x.load_file()




