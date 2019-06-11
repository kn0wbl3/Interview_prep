class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = {}

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        if user not in self.users:
            self.users[user] = 1
        else:
            self.users[user] += 1

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group.get_groups() == []:
        list_of_users = group.get_users()
        return (user in list_of_users)
    else:
        for sub_group in group.get_groups():
            return is_user_in_group(user, sub_group)

def tests():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    parent.add_user('MR. Smith')

    child.add_group(sub_child)
    parent.add_group(child)
    
    assert(is_user_in_group('sub_child_user', sub_child))
    assert(is_user_in_group('sub_child_user', parent))
    assert(is_user_in_group('john', child) == False) #edge case, testing if user that doesn't exist is in list
    assert(is_user_in_group('MR. Smith', child) == False) #edge case, testing if user in another list is found in this list
    
    
    print('tests done')

tests() 