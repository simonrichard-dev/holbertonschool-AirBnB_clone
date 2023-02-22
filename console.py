#!/usr/bin/python3
""" base class """
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """class HBNB for Command Interpreter
    """
    prompt = '(shotgun !!!) '
    list_class = ['BaseModel']

    list_function = ['create']

    # def precmd(self, arg):
    #    """parses command input"""
    #    if '.' in arg and '(' in arg and ')' in arg:
    #        my_class = arg.split('.')
    #        my_func = my_class[1].split('(')
    #        param=my_func[1].split(')')
    #        if my_class[0] in HBNBCommand.list_class and \
    #           my_func[0] in HBNBCommand.list_function:
    #            arg = my_func[0] + ' ' + my_class[0] + ' ' + param[0]
    #    return arg

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
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")

        elif len(arg) == 1:
            print('** instance id missing **')

        else:
            try:
                obj_to_show = storage.all()[arg[0] + '.' + arg[1]]
            except:
                print('** no instance found **')
            else:
                print(obj_to_show)

    def do_destroy(self, arg):
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")

        elif len(arg) == 1:
            print('** instance id missing **')

        else:
            try:
                obj_to_del = storage.all()
                string = "{}.{}".format(arg[0], arg[1])
                del obj_to_del[string]
                storage.save()

                print('yes')
            except:
                print('** no instance found **')

    def do_all(self, arg):
        arg = arg.split()
        objects = storage.all()

        if len(arg) == 0:
            print([str(obj) for obj in objects.values()])
        elif arg[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == arg[0]])

    def do_update(self, arg):
        arg = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.list_class:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print('** instance id missing **')
        elif len(arg) >= 2:
            try:
                storage.all()[arg[0] + '.' + arg[1]]
            except:
                print('** no instance found **')
                return
            if len(arg) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")
        else:
            setattr(instance, arg[2], arg[3])
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
