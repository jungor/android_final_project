# -*-coding:utf-8 -*-

import os
import re
from datetime import datetime

from db import get_db

IMG_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "static", "img")


class User(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value
        else:
            raise ValueError("You did not provide valid name")

    @property
    def pwd(self):
        return self._pwd

    @pwd.setter
    def pwd(self, value):
        if value:
            self._pwd = value
        else:
            raise ValueError("You did not provide valid pwd")

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if value:
            self._sex = value
        else:
            raise ValueError("You did not provide valid sex")

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        if value:
            self._major = value
        else:
            raise ValueError("You did not provide valid major")

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if value:
            self._grade = value
        else:
            raise ValueError("You did not provide valid grade")

    @property
    def avatar_url(self):
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        if value:
            now = re.sub(r'[ :.]', '-', str(datetime.now()))
            path = os.path.join(IMG_DIR, str(self.name) + "_avatar" + now + ".jpg")
            avatar_file = open(path, 'w')
            avatar_file.write(value)
            self._avatar_url = '/' + '/'.join(path.split('/')[-3:])
            avatar_file.close()
            # else:
            #     raise ValueError("You did not provide valid avatar")

    def __init__(self, name=None, pwd=None, sex=None, major=None, grade=None, avatar=None, **kwargs):
        super(User, self).__init__()
        self._name = None
        self._pwd = None
        self._sex = None
        self._major = None
        self._grade = None
        self._avatar_url = None
        self._new_psw = None
        self._avatar_file = "default_avatar.jpg"
        self.name = name
        self.pwd = pwd
        self.sex = sex
        self.major = major
        self.grade = grade
        self.avatar_url = avatar

    def save(self):
        db = get_db()
        db["Users"].update(
                {
                    "name": self.name,
                },
                {
                    "name": self.name,
                    "pwd": self.pwd,
                    "sex": self.sex,
                    "major": self.major,
                    "grade": self.grade,
                    "avatar_url": self.avatar_url,
                },
                upsert=True
        )

    @classmethod
    def is_exist(cls, name):
        db = get_db()
        doc = db["Users"].find_one({"name": name})
        if doc:
            return True
        else:
            return False

    @classmethod
    def authenticate(cls, name, pwd):
        if cls.is_exist(name):
            db = get_db()
            doc = db["Users"].find_one({"name": name, "pwd": pwd})
            return doc
        else:
            return None

    @classmethod
    def get_user(cls, name, pwd):
        doc = cls.authenticate(name, pwd)
        if doc:
            print doc
            u = cls(**doc)
            u._avatar_url = doc["avatar_url"]
            return u
        else:
            return None


if __name__ == "__main__":
    pass
