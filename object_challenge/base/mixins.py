from object_challenge import app, pymongo
from object_challenge.base import UserObj


class AuthMixin:
    DEFAULT_AUTH_ERRORS = {
        'bearer': "Invalid authorization `bearer`",
        'token': "Invalid user `token`"
    }

    def _fetch_user(self, token):
        """

        :param token:
        :return:
        """
        user_data = pymongo.db.users.find_one({'auth_token': token}, {'_id': 0})
        if user_data:
            return UserObj(**user_data)

    def is_authenticated(self, request):
        """

        :param request:
        :return:
        """
        user = None
        error = None

        auth_header = request.headers.get('Authorization')
        if auth_header:
            bearer, token = auth_header.split(' ')
            if bearer == app.config['BEARER']:
                if token:
                    user = self._fetch_user(token)
                    if not user:
                        error = self.DEFAULT_AUTH_ERRORS['token']
                else:
                    error = self.DEFAULT_AUTH_ERRORS['token']
            else:
                error = self.DEFAULT_AUTH_ERRORS['bearer']

        return user, error
