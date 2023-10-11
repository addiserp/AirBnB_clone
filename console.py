#!/usr/bin/python3
"""
    Main Console program
    a program called console.py that contains the entry
    point of the command interpreter:
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Quit/exit the program"""
        return True

    def do_quit(self, arg):
        """Quit/exit the program"""
        return True

    def emptyline(self):
        """Ignore/skip empty inputs"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
