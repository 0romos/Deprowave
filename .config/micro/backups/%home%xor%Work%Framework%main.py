import os
import inspect
from importlib.machinery import SourceFileLoader
from modules.help import HelpCommand
from data.clear import ClearScreen
from data.banner import Display
from core.modular import Module


class ExploitLoader:
    def __init__(self):
        self.exploits = []

    def load_exploits(self):
        exploits_directory = "exploits"
        for filename in os.listdir(exploits_directory):
            if filename.endswith(".py") and filename != "__init__.py":
                exploit_module = SourceFileLoader(filename[:-3], os.path.join(exploits_directory, filename)).load_module()
                for name, obj in inspect.getmembers(exploit_module):
                    if inspect.isclass(obj) and issubclass(obj, Module) and obj is not Module:
                        exploit_instance = obj()
                        self.exploits.append(exploit_instance)


def main(loader, help_command):
    try:
        while True:
            user_input = input("Framework > ").strip()
            if user_input == "help":
                help_command.execute(loader.exploits)
            elif user_input == "exit":
                print("Exiting...")
                break
            else:
                exploit_instance = next((exploit for exploit in loader.exploits if exploit.name == user_input), None)
                if exploit_instance:
                    print()
                    exploit_instance.execute()
                    print()
                else:
                    print(f"Command '{user_input}' does not exist.")
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    ClearScreen.clear()
    Display.banner()
    loader = ExploitLoader()
    loader.load_exploits()
    help_command = HelpCommand()
    main(loader, help_command)
