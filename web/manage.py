#!/usr/bin/env python3

# when run from the command line
if __name__ == "__main__":
    # python imports
    import os
    import sys
    # django imports
    from django.core.management import execute_from_command_line

    # load the correct django settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "urbanRadish.settings.local")

    # perform the default action
    execute_from_command_line(sys.argv)


## end of file ##
