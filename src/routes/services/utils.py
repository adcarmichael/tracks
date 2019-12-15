from datetime import datetime
import os
import glob
import routes.services.conf as conf


def convert_str_to_datetime(date_str):
    date = datetime.strptime(date_str, "%d/%m/%Y").date()
    return date


def get_name_from_value_for_enum(enum, value):
    if not isinstance(value, (list,)):
        value = [value]
    name = []
    for val in value:
        name.append(enum(val).name)
    return name

def ensure_data_is_type_list(data):
    if not isinstance(data, (list,)):
            data = [data]
    return data

def get_grade_name_from_value(value):
    return get_name_from_value_for_enum(conf.Grade, value)


def get_grade_sub_name_from_value(value):
    return get_name_from_value_for_enum(conf.GradeSub, value)


class SampleDb:
    apps = ['routes']

    def __init__(self):
        pass

    def delete_db(self):
        for app_name in self.apps:
            self._delete_migration_for_app(app_name)
        if os.path.isfile('db.sqlite3'):
            try:
                os.remove('db.sqlite3')
                print('Deleted db')
            except:
                print('Failed to delete file')

    def _delete_migration_for_app(self, app_name):
        fileList = glob.glob(f'{app_name}/migrations/*.py', recursive=False)

        # Iterate over the list of filepaths & remove each file.
        for filePath in fileList:
            if not os.path.basename(filePath) == '__init__.py':
                try:
                    os.remove(filePath)
                except OSError:
                    print("Error while deleting file")

    def new_migrations(self):
        os.system('python manage.py makemigrations')
        os.system('python manage.py migrate --fake core zero')
        pass

    def add_gym(self):
        pass
