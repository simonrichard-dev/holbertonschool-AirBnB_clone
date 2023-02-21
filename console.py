#!/usr/bin/python3
""" base class """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class HBNB for Command Interpreter
    """
    prompt = '(hbnb) '
    list_class = ['BaseModel']

    list_function = ['create']

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            my_class = arg.split('.')
            my_func = my_class[1].split('(')
            param=my_func[1].split(')')
            if my_class[0] in HBNBCommand.list_class and \
               my_func[0] in HBNBCommand.list_function:
                arg = my_func[0] + ' ' + my_class[0] + ' ' + param[0]
        return arg

    def do_EOF(self, arg):
        """execute End of File line
        """
        return True
    
    def do_quit(self, arg):
        """Quit commant to exit the program
        """
        return True

    def emptyline(self):
        """Do not repeat previous action"""
        pass

    def do_create(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
    
    def do_show(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif arg not in id:
            print('** instance id missing **')
        elif new_instance not in id:
            print('** no instance found **')
        else:
            print(new_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()