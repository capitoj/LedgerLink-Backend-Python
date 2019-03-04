#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainsite.settings.base")

    from django.core.management import execute_from_command_line

    try:
        args = sys.argv[:]
        has_loadfixtures_flag = True if '--loadfixtures' in args else False

        if has_loadfixtures_flag:
            args.remove('--loadfixtures')

        execute_from_command_line(args)

        if 'migrate' in args and args[1] == 'migrate' and has_loadfixtures_flag:
            from django.core.management import call_command
            from django.conf import settings

            FIXTURES_TO_LOAD_AFTER_MIGRATION = getattr(settings, "FIXTURES_TO_LOAD_AFTER_MIGRATION")

            if FIXTURES_TO_LOAD_AFTER_MIGRATION is not None:
                for fixture_file in settings.FIXTURES_TO_LOAD_AFTER_MIGRATION:
                    try:
                        call_command('loaddata', fixture_file)
                        print('  Processed file: {}'.format(fixture_file))
                    except Exception as e:
                        print(e)
                        print("  Unable to process file: {}".format(fixture_file))


    except:
        raise