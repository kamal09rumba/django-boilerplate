from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Renames a Django Project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The New Django Project Name')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # bit of logic to rename the project

        file_to_rename = ['demo/settings/base.py', 'demo/wsgi.py', 'manage.py']
        folder_to_rename = ['demo']

        for f in file_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()
            filedata = filedata.replace('demo', new_project_name)
            # print(filedata)
            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)
        self.stdout.write(self.style.SUCCESS('Project has been rename to %s' % new_project_name))
