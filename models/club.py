# -*-coding:utf-8 -*-

import os
import re
from datetime import datetime

from db import get_db

IMG_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "static", "img", "club")


class Club(object):
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
    def slogan(self):
        return self._slogan

    @slogan.setter
    def slogan(self, value):
        if value:
            self._slogan = value
        else:
            raise ValueError("You did not provide valid slogan")

    @property
    def intro(self):
        return self._intro

    @intro.setter
    def intro(self, value):
        if value:
            self._intro = value
        else:
            raise ValueError("You did not provide valid intro")

    @property
    def img_url(self):
        return self._img_url

    @img_url.setter
    def img_url(self, value):
        if value:
            # now = re.sub(r'[ :.]', '-', str(datetime.now()))
            path = os.path.join(IMG_DIR, str(self.name) + ".jpg")
            img_file = open(path, 'w')
            img_file.write(value)
            self._img_url = '/static.' + '/'.join(path.split('/')[-3:])
            img_file.close()
            # else:
            #     raise ValueError("You did not provide valid img")

    def __init__(self, name, slogan, intro, img, **kwargs):
        super(Club, self).__init__()
        self._name = None
        self._slogan = None
        self._intro = None
        self._all_act = []
        self._recent_act = []
        self._img_url = None
        self.name = name
        self.slogan = slogan
        self.intro = intro
        self.img_url = img

    def save(self):
        db = get_db()
        db["Clubs"].update(
                {
                    "name": self.name,
                },
                {
                    "name": self.name,
                    "slogan": self.slogan,
                    "intro": self.intro,
                    "img_url": self.img_url,
                    "all_act": self._all_act,
                    "recent_url": self._recent_act,
                },
                upsert=True
        )

    @classmethod
    def is_exist(cls, name):
        db = get_db()
        doc = db["Clubs"].find_one({"name": name})
        if doc:
            return True
        else:
            return False

    # @classmethod
    # def authenticate(cls, name, pwd):
    #     if cls.is_exist(name):
    #         db = get_db()
    #         doc = db["Users"].find_one({"name": name, "pwd": pwd})
    #         return doc
    #     else:
    #         return None

    @classmethod
    def get_all_clubs(cls):
        db = get_db()
        cursor = db["Clubs"].find({})
        return list(cursor)


if __name__ == "__main__":
    pass
