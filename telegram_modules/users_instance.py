from singleton_decorator import singleton


@singleton
class UsersInstance:

    def __init__(self):
        self.instance = {}

    def set_value(self, user, key, value):
        user_values = self.instance.setdefault(user, {})
        user_values[key] = value

    def get_value(self, user, key):
        user_values = self.instance.setdefault(user, {})
        return user_values.get(key)

    def clear_instance(self, user):
        self.instance[user] = {}
