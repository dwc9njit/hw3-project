from .command_handler import Command

class MenuCommand(Command):
    def execute(self):
        print("Available commands: greet, goodbye, exit, menu")
