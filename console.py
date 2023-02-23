#!/usr/bin/python3
""" base class """
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNB for Command Interpreter
    """
    prompt = '(shotgun !!!) '
    list_class = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                  'Place', 'Review']

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
        else:
            try:
                obj = storage.all()[arg[0] + '.' + arg[1]]
            except:
                print('** no instance found **')
                return
            if len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            else:
                setattr(obj, arg[2], arg[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
