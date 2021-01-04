# OP - object programming (usr.py)
#
# this file is placed in the public domain

"users (usr)"

# imports

import opl

# exceptions

class ENOUSER(Exception):
    "no matching user found."

# classes

class User(opl.Object):

    "user"

    def __init__(self):
        super().__init__()
        self.user = ""
        self.perms = []

class Users(opl.Object):

    "users"

    userhosts = opl.Object()

    def allowed(self, origin, perm):
        "origin has needed permission"
        perm = perm.upper()
        origin = opl.get(self.userhosts, origin, origin)
        user = self.get_user(origin)
        if user:
            if perm in user.perms:
                return True
        return False

    def delete(self, origin, perm):
        "permission"
        for user in self.get_users(origin):
            try:
                user.perms.remove(perm)
                opl.save(user)
                return True
            except ValueError:
                pass

    def get_users(self, origin=""):
        "all users, optionaly matching origin"
        s = {"user": origin}
        return opl.dbs.find("opl.usr.User", s)

    def get_user(self, origin):
        "specific user with matching origin"
        u = list(self.get_users(origin))
        if u:
            return u[-1][-1]

    def meet(self, origin, perms=None):
        "user"
        user = self.get_user(origin)
        if user:
            return user
        user = User()
        user.user = origin
        user.perms = ["USER", ]
        opl.save(user)
        return user

    def oper(self, origin):
        "grant oper permission"
        user = self.get_user(origin)
        if user:
            return user
        user = User()
        user.user = origin
        user.perms = ["OPER", "USER"]
        opl.save(user)
        return user

    def perm(self, origin, permission):
        "add permission"
        user = self.get_user(origin)
        if not user:
            raise ENOUSER(origin)
        if permission.upper() not in user.perms:
            user.perms.append(permission.upper())
            opl.save(user)
        return user
