# -*-coding:utf-8 -*-

import os
import re
from datetime import datetime

from bson.objectid import ObjectId

from consts import *

from db import get_db

IMG_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "static", "img", "activity")


class Activity(object):
    @classmethod
    def get_all_acts_by_club(cls, cname):
        db = get_db()
        cursor = db["Activities"].find({"organizer": cname})
        return list(cursor)

    @classmethod
    def reset(cls):
        db = get_db()
        cursor = db["Activities"].find({})
        if cursor.count() == 0:
            db["Activities"].insert(
                    {
                        "title": "校园跑",
                        "read_nums": "0",
                        "start_date": "2015-11-11 19:00",
                        "end_date": "2015-11-11 22:00",
                        "sponsor": "红牛",
                        "organizer": "一起跑",
                        "img_url": SERVER_ROOT_URL + "/static/img/activity/0.jpg",
                        "detail_url": SERVER_ROOT_URL + "/static/img/activity/0",
                        "type": "0",
                    }
            )
            db["Activities"].insert(
                    {
                        "title": "三下乡",
                        "read_nums": "0",
                        "start_date": "2015-11-11 19:00",
                        "end_date": "2015-11-11 22:00",
                        "sponsor": "红牛",
                        "organizer": "软件学院团委",
                        "img_url": SERVER_ROOT_URL + "/static/img/activity/1.jpg",
                        "detail_url": SERVER_ROOT_URL + "/static/img/activity/1",
                        "type": "1",
                    }
            )
            db["Activities"].insert(
                    {
                        "title": "认识毒药",
                        "read_nums": "0",
                        "start_date": "2015-11-11 19:00",
                        "end_date": "2015-11-11 22:00",
                        "sponsor": "红牛",
                        "organizer": "软件学院学生会",
                        "img_url": SERVER_ROOT_URL + "/static/img/activity/2.jpg",
                        "detail_url": SERVER_ROOT_URL + "/static/img/activity/2",
                        "type": "2",
                    }
            )
            db["Activities"].insert(
                    {
                        "title": "食在广州",
                        "read_nums": "0",
                        "start_date": "2015-11-11 19:00",
                        "end_date": "2015-11-11 22:00",
                        "sponsor": "红牛",
                        "organizer": "旅游协会",
                        "img_url": SERVER_ROOT_URL + "/static/img/activity/3.jpg",
                        "detail_url": SERVER_ROOT_URL + "/static/img/activity/3",
                        "type": "3",
                    }
            )
            db["Activities"].insert(
                    {
                        "title": "教室电影",
                        "read_nums": "0",
                        "start_date": "2015-11-11 19:00",
                        "end_date": "2015-11-11 22:00",
                        "sponsor": "红牛",
                        "organizer": "科幻协会",
                        "img_url": SERVER_ROOT_URL + "/static/img/activity/4.jpg",
                        "detail_url": SERVER_ROOT_URL + "/static/img/activity/4",
                        "type": "0",
                    }
            )
            db["Activities"].insert(
                    {
                        "title": "3D打印前景",
                        "read_nums": "0",
                        "start_date": "2015-11-11 19:00",
                        "end_date": "2015-11-11 22:00",
                        "sponsor": "红牛",
                        "organizer": "IBM俱乐部",
                        "img_url": SERVER_ROOT_URL + "/static/img/activity/5.jpg",
                        "detail_url": SERVER_ROOT_URL + "/static/img/activity/5",
                        "type": "1",
                    }
            )
            db["Activities"].insert(
                    {
                        "title": "净化心灵",
                        "read_nums": "0",
                        "start_date": "2015-11-11 19:00",
                        "end_date": "2015-11-11 22:00",
                        "sponsor": "红牛",
                        "organizer": "心理学社",
                        "img_url": SERVER_ROOT_URL + "/static/img/activity/6.jpg",
                        "detail_url": SERVER_ROOT_URL + "/static/img/activity/6",
                        "type": "2",
                    }
            )
            db["Activities"].insert(
                    {
                        "title": "PS讲座",
                        "read_nums": "0",
                        "start_date": "2015-11-11 19:00",
                        "end_date": "2015-11-11 22:00",
                        "sponsor": "红牛",
                        "organizer": "摄影协会",
                        "img_url": SERVER_ROOT_URL + "/static/img/activity/7.jpg",
                        "detail_url": SERVER_ROOT_URL + "/static/img/activity/7",
                        "type": "3",
                    }
            )

            # db["Activities"].update_one(
            #         {
            #             "_id": aid_object
            #         },
            #         {
            #             "$set": {"detail_url": SERVER_ROOT_URL + "/static/img/activity/" + str(aid_object) + ".png"}
            #         }
            # )

if __name__ == "__main__":
    pass
