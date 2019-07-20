from datetime import datetime
import os
import glob


def convert_str_to_datetime(date_str):
    date = datetime.strptime(date_str, "%d/%m/%Y").date()
    return date


class SampleDb:
    apps = ['routes']

    def delete_db(self):
        for app_name in self.apps:
            self._delete_migration_for_app(app_name)

    def _delete_migration_for_app(self, app_name):
        fileList = glob.glob(f'{app_name}/migrations/*.py', recursive=False)

        # Iterate over the list of filepaths & remove each file.
        for filePath in fileList:
            if not os.path.basename(filePath) == '__init__.py':
                try:
                    os.remove(filePath)
                except OSError:
                    print("Error while deleting file")

    def create_new(self):
        os.system('python manage.py migrate --fake core zero')
        pass


db = SampleDb()
db.delete_db()
