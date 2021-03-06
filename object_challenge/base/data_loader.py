import os

import ujson

from object_challenge import app
from object_challenge.bucket.mongo_models import User as UserDocument

__all__ = ('DataLoaderMixin',)


class DataLoaderMixin:

    @staticmethod
    def load_data(filename):
        path = os.path.join(app.config['PROJECT_ROOT'], 'object_challenge', 'fixtures', filename)
        col_name = filename[:-5]

        with open(path) as file:
            for row in file.readlines():
                UserDocument._get_db()[col_name].insert_one(ujson.loads(row))
