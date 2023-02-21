#!/usr/bin/python3
""" base class """
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """class HBNB for Command Interpreter
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """execute End of File line
        """
        return True
    
    def do_quit(self, line):
        """Quit commant to exit the program
        """
        return True

    def emptyline(self):
        """Do not repeat previous action"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()