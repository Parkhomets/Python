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

    def load_file(self):
        #примерно тут будет начинаться параллельная область
        if self.json_exist:
            try:
                simple_part = self.data.popitem()
            except KeyError:
                return
            server = simple_part[0]
            data = simple_part[1]
            server = self.login(server, data.get("user"), data.get("pass"))
            if server:
                path = data.get("path")
                files = data.get("files")
                for i in range(len(files)):
                    ftype = files[i].split(".")[len(files[i].split(".")) - 1]
                    server.cwd(path[i])
                    try:
                        with open(files[i], "rb") as f:
                            server.storbinary("STOR %s" % files[i], f)
                    except:
                        print("{} have not been download".format(files[i]))
        else:
            print("You can not download. Json does not exist.")


