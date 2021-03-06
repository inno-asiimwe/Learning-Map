"""
Usage:
    (Map) add_skill <skill_name>      
    (Map) (-i | --interactive)
    (Map) (-h | --help)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

"""

import sys
import cmd
from docopt import docopt, DocoptExit
from classes.learning_map import LearningMap


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


lp = LearningMap()


class LearningMap(cmd.Cmd):
    intro = 'Welcome to THE Learning Map APP!\n'
    prompt = ' (type help for a list of commands.)\n'

    file = None

    @docopt_cmd
    def do_add_skill(self, arg):
        """Usage: add_skill <skill_name>"""
        skill_name = arg['<skill_name>']
        lp.add_skill(skill_name)

    @docopt_cmd
    def do_learnt_skill(self, arg):
        """Usage: learnt_skill <skill_name>"""
        skill_name = arg['<skill_name>']
        lp.learnt_skill(skill_name)

    @docopt_cmd
    def do_learning_progress(self, arg):
        """Usage: learning_progress"""
        lp.learning_progress()

    @docopt_cmd
    def do_skills_learnt(self, arg):
        """Usage: skills_learnt"""
        lp.skills_list()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('******Good Bye!******')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    LearningMap().cmdloop()
print(opt)
