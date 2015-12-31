# -*-coding:utf-8 -*-

import os
import re
from datetime import datetime
from consts import *

from db import get_db

IMG_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "static", "img", "club")
CLUBS = [
    {

    },
]

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
    def chinese_name(self):
        return self._chinese_name

    @chinese_name.setter
    def chinese_name(self, value):
        if value:
            self._chinese_name = value
        else:
            raise ValueError("You did not provide valid chinese_name")

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

    def __init__(self, name, chinese_name, slogan, intro, img, cid=None, **kwargs):
        super(Club, self).__init__()
        self._cid = None
        self._name = None
        self._chinese_name = None
        self._slogan = None
        self._intro = None
        self._all_act = []
        self._recent_act = []
        self._img_url = None
        self.name = name
        self.chinese_name = chinese_name
        self.slogan = slogan
        self.intro = intro
        self.img_url = img
        if cid:
            self

    def save(self):
        db = get_db()
        if self.cid:
            db["Clubs"].update(
                    {
                        "_id": self.cid,
                    },
                    {
                        "name": self.name,
                        "chinese_name": self.chinese_name,
                        "slogan": self.slogan,
                        "intro": self.intro,
                        "img_url": self.img_url,
                        "all_act": self._all_act,
                        "recent_url": self._recent_act,
                    },
                    upsert=True
            )

    # @classmethod
    # def is_exist(cls, name):
    #     db = get_db()
    #     doc = db["Clubs"].find_one({"name": name})
    #     if doc:
    #         return True
    #     else:
    #         return False

    # @classmethod
    # def authenticate(cls, name, pwd):
    #     if cls.is_name_exist(name):
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

    @classmethod
    def reset(cls):
        db = get_db()
        cursor = db["Clubs"].find({})
        if cursor.count() == 0:
            db["Clubs"].insert(
                    {
                        "name": "guangbotai",
                        "chinese_name": "广播台",
                        "slogan": "赶紧参加维纳斯歌手大赛吧",
                        "intro": "大家好我叫广播台",
                        "img_url": SERVER_ROOT_URL + "/static/img/club/default_logo.png",
                        "all_act": [],
                        "recent_act": [],
                    }
            )

if __name__ == "__main__":
    pass
