# -*-coding:utf-8 -*-


import pymongo


def get_db():
    client = pymongo.MongoClient()
    # client["test"].authenticate("jj", "2333")
    db = client["test"]
    return db
