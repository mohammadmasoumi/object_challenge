import mongoengine as mo


class User(mo.Document):
    user_id = mo.IntField(null=False, unique=True)
    name = mo.StringField(null=False)
    auth_token = mo.StringField(null=False, unique=True)

    def __str__(self):
        return f'{self.user_id}-{self.name}-{self.auth_token}'

    meta = {
        'index_background': True,
        'collection': 'users',
        'indexes': [
            'user_id',
            'auth_token'
        ],
        'db_alias': 'challenge'
    }
