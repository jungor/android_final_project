# -*-coding:utf-8 -*-

import os
import re
from datetime import datetime

import pymongo
from bson.objectid import ObjectId

from consts import *

from db import get_db

IMG_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "static", "img", "activity")


class Activity(object):
    @classmethod
    def get_recommend_acts(cls):
        db = get_db()
        cursor = db["Activities"].find({}).sort("start_date", pymongo.ASCENDING).limit(10)
        return list(cursor)

    @classmethod
    def get_all_acts_by_club(cls, cname):
        db = get_db()
        cursor = db["Activities"].find({"organizer": cname}).sort("start_date", pymongo.ASCENDING).limit(10)
        return list(cursor)

    @classmethod
    def get_some_acts_by_type(cls, t):
        db = get_db()
        cursor = db["Activities"].find({"type": t}).sort("start_date", pymongo.DESCENDING).limit(1)
        return list(cursor)

    @classmethod
    def get_more_acts_by_type(cls, t, s):
        db = get_db()
        cursor = db["Activities"].find({"type": t}).sort("start_date", pymongo.DESCENDING).limit(1).skip(s)
        return list(cursor)

    # @classmethod
    # def get_recent_acts_by_club(cls, cname, ):
    #     db = get_db()
    #     cursor = db["Activities"].find({"organizer": cname})
    #     return list(cursor)

    @classmethod
    def reset(cls):
        db = get_db()
        db["Activities"].remove({})
        db["Activities"].insert(
                {
                    "id": "0",
                    "title": "校园跑",
                    "place": "内环",
                    "read_nums": "0",
                    "start_date": "2015-10-11",
                    "end_date": "2015-10-11",
                    "start_time": "19:00",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "一起跑",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/0.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/0",
                    "type": "0",
                    "detail": "无",
                }
        )
        db["Activities"].insert(
                {
                    "id": "1",
                    "title": "三下乡",
                    "place": "河源",
                    "read_nums": "0",
                    "start_date": "2015-11-11",
                    "end_date": "2015-11-11",
                    "start_time": "19:00",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "软件学院团委",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/1.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/1",
                    "type": "1",
                    "detail": "无",
                }
        )
        db["Activities"].insert(
                {
                    "id": "2",
                    "title": "认识毒药",
                    "place": "公教楼B202",
                    "read_nums": "0",
                    "start_date": "2015-11-11",
                    "end_date": "2015-11-11",
                    "start_time": "19:00",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "软件学院学生会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/2.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/2",
                    "type": "2",
                    "detail": "无",
                }
        )
        db["Activities"].insert(
                {
                    "id": "3",
                    "title": "食在广州",
                    "place": "天河区",
                    "read_nums": "0",
                    "start_date": "2015-11-11",
                    "end_date": "2015-11-11",
                    "start_time": "19:00",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "旅游协会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/3.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/3",
                    "type": "3",
                    "detail": "无",
                }
        )
        db["Activities"].insert(
                {
                    "id": "4",
                    "title": "教室电影",
                    "place": "公教楼B202",
                    "read_nums": "0",
                    "start_date": "2015-11-11",
                    "end_date": "2015-11-11",
                    "start_time": "19:00",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "科幻协会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/4.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/4",
                    "type": "0",
                    "detail": "无",
                }
        )
        db["Activities"].insert(
                {
                    "id": "5",
                    "title": "3D打印前景",
                    "place": "公教楼B202",
                    "read_nums": "0",
                    "start_date": "2015-11-11",
                    "end_date": "2015-11-11",
                    "start_time": "19:00",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "IBM俱乐部",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/5.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/5",
                    "type": "1",
                    "detail": "无",
                }
        )
        db["Activities"].insert(
                {
                    "id": "6",
                    "title": "净化心灵",
                    "place": "公教楼B202",
                    "read_nums": "0",
                    "start_date": "2015-11-11",
                    "end_date": "2015-11-11",
                    "start_time": "19:00",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "心理学社",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/6.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/6",
                    "type": "2",
                    "detail": "无",
                }
        )
        db["Activities"].insert(
                {
                    "id": "7",
                    "title": "PS讲座",
                    "place": "公教楼B202",
                    "read_nums": "0",
                    "start_date": "2015-11-11",
                    "end_date": "2015-11-11",
                    "start_time": "19:00",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "摄影协会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/7.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/7",
                    "type": "3",
                    "detail": "无",
                }
        )
        db["Activities"].insert(
                {
                    "id": "8",
                    "title": "假面舞会",
                    "place": "至善学生活动中心",
                    "read_nums": "0",
                    "start_date": "2015-11-28",
                    "end_date": "2015-11-28",
                    "start_time": "20:00",
                    "end_time": "23:30",
                    "sponsor": "红牛",
                    "organizer": "广播台",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/8.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/8",
                    "type": "3",
                    "detail": "假面舞会作为最具浪漫气质的激情活动之一，源于西方的万圣节，颇具西方文化色彩，充满了新奇和绚烂的气氛。这也是我们放开日常身份，与面具背后的陌生朋友共度美好夜晚的机会。",
                }
        )
        db["Activities"].insert(
                {
                    "id": "9",
                    "title": "Color run",
                    "place": "内环",
                    "read_nums": "0",
                    "start_date": "2015-10-11",
                    "end_date": "2015-10-11",
                    "start_time": "15:00",
                    "end_time": "17:00",
                    "sponsor": "红牛",
                    "organizer": "一起跑",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/9.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/9",
                    "type": "3",
                    "detail": "距离为5公里的Color Run不计时，跑者每一公里都将经过一个色彩站，从头到脚都会被抛洒上不同的颜色。在终点舞台区将开始一场更加壮观的色彩派对，届时大家会一起把手中的彩色粉向空中抛洒，每个人都会像调色板一样色彩缤纷。相信我们，这将是你所见过最棒的5公里跑完成后的派对",
                }
        )
        db["Activities"].insert(
                {
                    "id": "10",
                    "title": "LOL校园争霸赛",
                    "place": "天城网吧",
                    "read_nums": "0",
                    "start_date": "2015-12-17",
                    "end_date": "2015-12-26",
                    "start_time": "14:00",
                    "end_time": "21:00",
                    "sponsor": "红牛",
                    "organizer": "电子竞技协会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/10.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/10",
                    "type": "3",
                    "detail": "想知道谁是中大第一中单吗？想知道中大第一战队花落谁家吗？无级别限制，无段位门槛，只要五个人凑得起，大家都是出门泉水0级，谁都能再乱战中怒夺胜利。谁是线上单挑王？谁是团战carry大boss？在这里，才是真正的开黑五连坐！",
                }
        )
        db["Activities"].insert(
                {
                    "id": "11",
                    "title": "中大答人决赛",
                    "place": "明德学生活动中心",
                    "read_nums": "0",
                    "start_date": "2015-04-17",
                    "end_date": "2015-04-17",
                    "start_time": "19:30",
                    "end_time": "21:30",
                    "sponsor": "红牛",
                    "organizer": "摄影协会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/11.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/11",
                    "type": "3",
                    "detail": "最强智力风暴，最牛团队协作，中大答人争霸赛终于迎来决赛！这里有数学达人，有文学精灵，有物理先锋，还有艺术大神！精英荟萃，谁能最终问鼎冠军，在擂台上站到最后一刻？感受最强的智力对决，享受脑力对决的快感吧！",
                }
        )
        db["Activities"].insert(
                {
                    "id": "12",
                    "title": "维纳斯歌手大赛启动仪式",
                    "place": "传设小礼堂",
                    "read_nums": "0",
                    "start_date": "2015-04-09",
                    "end_date": "2015-04-09",
                    "start_time": "19:00",
                    "end_time": "21:00",
                    "sponsor": "红牛",
                    "organizer": "广播台",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/12.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/12",
                    "type": "3",
                    "detail": "眼眸中，CD是狂热的见证。脑海里，音符是梦想的征程。再多的乔庄，也掩藏不了内心对音乐的热诚。又是一年维纳斯，又是一段充满奇遇的音乐之旅，4月9日晚，我们一同起航。",
                }
        )
        db["Activities"].insert(
                {
                    "id": "13",
                    "title": "软件创新大赛决赛",
                    "place": "行政楼B102",
                    "read_nums": "0",
                    "start_date": "2015-12-23",
                    "end_date": "2015-12-23",
                    "start_time": "19:00",
                    "end_time": "21:30",
                    "sponsor": "红牛",
                    "organizer": "软件学院团委",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/13.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/13",
                    "type": "3",
                    "detail": "第十一届中山大学“37游戏杯”软件创新开发大赛决赛，玩心创造世界，创意改变未来，让我们相约，用我们的双眼见证科技带来璀璨光明。在这个夜晚，十二支决赛队伍将进行最后的展示，谁能最终胜出？你就是见证者！",
                }
        )
        db["Activities"].insert(
                {
                    "id": "14",
                    "title": "校园美食节",
                    "place": "中心花坛",
                    "read_nums": "0",
                    "start_date": "2015-05-09",
                    "end_date": "2015-05-09",
                    "start_time": "9:30",
                    "end_time": "17:30",
                    "sponsor": "红牛",
                    "organizer": "软件学院学生会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/14.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/14",
                    "type": "3",
                    "detail": "为了弘扬餐饮文化，增强后勤与同学们之间的沟通联系， 在食堂与同学之中架起及时交流的桥梁，加强学生的动手实践能力，激发食堂员工的创新意识，展现校园文化及当代大学生的青春魅力与风采。让你的味蕾享受一次心动之旅吧。",
                }
        )
        db["Activities"].insert(
                {
                    "id": "15",
                    "title": "吉他狂欢夜",
                    "place": "中心花坛",
                    "read_nums": "0",
                    "start_date": "2015-05-16",
                    "end_date": "2015-05-16",
                    "start_time": "19:30",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "广播台",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/15.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/15",
                    "type": "3",
                    "detail": "最先锋的乐手，最前卫的观众，最震撼的气场，最有范儿的音乐。这个夜晚，一把吉他，一首歌，一次感动，是不眠之夜与琴弦之音的交织，16号晚7点，一起迷失在吉他的世界，寻找属于自己的声音。",
                }
        )
        db["Activities"].insert(
                {
                    "id": "16",
                    "title": "舞坛争霸",
                    "place": "工学院广场",
                    "read_nums": "0",
                    "start_date": "2015-04-25",
                    "end_date": "2015-04-25",
                    "start_time": "19:30",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "广播台",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/16.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/16",
                    "type": "3",
                    "detail": "享受全身细胞一起律动的快感，在旋律的引领下释放全身的热血。在这里，你将看到经过两周比赛最终脱颖而出的八支最强队伍，究竟他们谁能展现最为惊艳的终极秀？节奏与动感，准备好彻夜抖脚了吗？",
                }
        )
        db["Activities"].insert(
                {
                    "id": "17",
                    "title": "你唱我猜",
                    "place": "明德学生活动中心",
                    "read_nums": "0",
                    "start_date": "2015-04-17",
                    "end_date": "2015-04-17",
                    "start_time": "14:30",
                    "end_time": "17:30",
                    "sponsor": "红牛",
                    "organizer": "广播台",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/17.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/17",
                    "type": "3",
                    "detail": "你觉得听过的歌很多吗？你觉得你是中华歌曲库吗？你能听到前奏秒猜歌曲吗？听歌之王就在这里，不服来战。",
                }
        )
        db["Activities"].insert(
                {
                    "id": "18",
                    "title": "CF校园赛",
                    "place": "天城网吧",
                    "read_nums": "0",
                    "start_date": "2015-05-10",
                    "end_date": "2015-05-17",
                    "start_time": "14:30",
                    "end_time": "21:30",
                    "sponsor": "红牛",
                    "organizer": "电子竞技协会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/18.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/18",
                    "type": "3",
                    "detail": "枪神一出，谁不应声倒地？想比试枪法吗？我没别的意思，只是想说在座的各位都是辣鸡，你若不服，CF校园赛，枪法见高低",
                }
        )
        db["Activities"].insert(
                {
                    "id": "19",
                    "title": "宠物障碍跑",
                    "place": "真草场",
                    "read_nums": "0",
                    "start_date": "2015-05-27",
                    "end_date": "2015-05-27",
                    "start_time": "14:30",
                    "end_time": "17:30",
                    "sponsor": "红牛",
                    "organizer": "软件学院学生会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/19.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/19",
                    "type": "3",
                    "detail": "猫奴狗奴集结号，相比比谁家的爱宠更出色吗？带它们来参加宠物障碍跑吧！",
                }
        )
        db["Activities"].insert(
                {
                    "id": "20",
                    "title": "电影马拉松之夜",
                    "place": "传设小礼堂",
                    "read_nums": "0",
                    "start_date": "2015-05-28",
                    "end_date": "2015-05-28",
                    "start_time": "19:30",
                    "end_time": "2:00",
                    "sponsor": "红牛",
                    "organizer": "科幻协会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/20.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/20",
                    "type": "3",
                    "detail": "你试过连续看电影吗？你试过连续看三部电影吗？28号晚，《盗墓迷城》三连发，带你度过木乃伊之夜。",
                }
        )
        db["Activities"].insert(
                {
                    "id": "21",
                    "title": "这才是真正的吹牛逼",
                    "place": "明德学生活动中心",
                    "read_nums": "0",
                    "start_date": "2015-10-18",
                    "end_date": "2015-10-18",
                    "start_time": "19:30",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "软件学院学生会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/21.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/21",
                    "type": "3",
                    "detail": "见过扯淡的，没见过这么扯蛋的！听说你很会吹牛逼？倒是上台看看谁更会吹啊。",
                }
        )
        db["Activities"].insert(
                {
                    "id": "22",
                    "title": "即兴涂鸦赛",
                    "place": "至善学生活动中心",
                    "read_nums": "0",
                    "start_date": "2015-10-23",
                    "end_date": "2015-10-23",
                    "start_time": "19:30",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "摄影协会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/22.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/22",
                    "type": "3",
                    "detail": "涂涂画画，画画图图，笔墨横飞，色彩纷呈，谁是涂鸦王者？多说无益，你行你来画。",
                }
        )
        db["Activities"].insert(
                {
                    "id": "23",
                    "title": "叫我大胃王",
                    "place": "中心花坛",
                    "read_nums": "0",
                    "start_date": "2015-06-06",
                    "end_date": "2015-06-06",
                    "start_time": "11:30",
                    "end_time": "13:30",
                    "sponsor": "红牛",
                    "organizer": "软件学院学生会",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/23.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/23",
                    "type": "3",
                    "detail": "这是我三天的食量啊兄弟，你说你一顿就能吃完？吃完我就叫你大胃王！",
                }
        )
        db["Activities"].insert(
                {
                    "id": "24",
                    "title": "群星模仿秀",
                    "place": "至善学生活动中心",
                    "read_nums": "0",
                    "start_date": "2015-11-21",
                    "end_date": "2015-11-21",
                    "start_time": "19:30",
                    "end_time": "22:00",
                    "sponsor": "红牛",
                    "organizer": "广播台",
                    "img_url": SERVER_ROOT_URL + "/static/img/activity/24.jpg",
                    "detail_url": SERVER_ROOT_URL + "/activity/24",
                    "type": "3",
                    "detail": "“刚刚我是看到刘德华了吗？”“天啊，真的好像周杰伦！”“额，其实我是模仿李荣浩…”",
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
