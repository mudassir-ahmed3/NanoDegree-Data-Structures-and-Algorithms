class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent.add_user("Muzammil")
child.add_user("Mudassir")
sub_child.add_user("Mubashir")

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    if user in group.users:
        return True

    for item in group.groups:
        if (is_user_in_group(user, item)):
            return True

    return False


print(is_user_in_group("Mubashir", parent))
print(is_user_in_group("Tanzeel", parent))
print(is_user_in_group("", parent))