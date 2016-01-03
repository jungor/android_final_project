# -*-coding:utf-8 -*-

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from bson.json_util import dumps
from tornado.options import define, options

from models.activity import Activity
from models.user import User
from models.club import Club

define("port", default=8000, help="run on the given port", type=int)


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        super(BaseHandler, self).data_received()

    def make_result(self, code, msg, data):
        self.set_header("Content-type", "application/json")
        rst = {
            "code": code,
            "msg": msg,
        }
        if data:
            rst["data"] = data
        return dumps(rst)

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")


class LoginHandler(BaseHandler):
    def post(self, *args, **kwargs):
        name = self.get_argument("name", None)
        pwd = self.get_argument("pwd", None)
        user_doc = User.authenticate(name, pwd)
        if user_doc:
            self.write(self.make_result(1, "login OK", user_doc))
        else:
            self.write(self.make_result(0, "user not found or wrong password", None))


class RegisterHandler(BaseHandler):
    def post(self, *args, **kwargs):
        new_user_kw = {
            "name": self.get_argument("name", None),
            "pwd": self.get_argument("pwd", None),
            "sex": self.get_argument("sex", None),
            "major": self.get_argument("major", None),
            "grade": self.get_argument("grade", None),
            "avatar": self.request.files["avatar"][0]["body"] if "avatar" in self.request.files else None,
        }
        if User.is_name_exist(new_user_kw["name"]):
            self.write(self.make_result(0, "name already exists", None))
            return
        try:
            new_user = User(**new_user_kw)
            new_user.save()
            self.write(self.make_result(1, "register OK", None))
        except ValueError, e:
            self.write(self.make_result(0, str(e), None))
        except IOError, e:
            self.write(self.make_result(0, str(e), None))


class UserUpdateHandler(BaseHandler):
    def post(self, *args, **kwargs):
        user_kw = {
            "uid": self.get_argument("uid", None),
            "pwd": self.get_argument("pwd", None),
            "sex": self.get_argument("sex", None),
            "major": self.get_argument("major", None),
            "grade": self.get_argument("grade", None),
        }
        print user_kw
        try:
            user = User.get(user_kw["uid"])
            if user:
                if user_kw["pwd"]:
                    user.pwd = user_kw["pwd"]
                if user_kw["sex"]:
                    user.sex = user_kw["sex"]
                if user_kw["major"]:
                    user.major = user_kw["major"]
                if user_kw["grade"]:
                    user.grade = user_kw["grade"]
                user.save()
                self.write(self.make_result(1, "user update OK", None))
            else:
                self.write(self.make_result(0, "user not found or wrong password", None))
        except ValueError, e:
            self.write(self.make_result(0, str(e), None))
        except IOError, e:
            self.write(self.make_result(0, str(e), None))


class UserUploadHandler(BaseHandler):
    def post(self, *args, **kwargs):
        user_kw = {
            "uid": self.get_argument("uid", None),
            "avatar": self.get_argument("avatar", None),
        }
        try:
            user = User.get(user_kw["uid"])
            if user:
                if user_kw["avatar"]:
                    user.avatar_url = user_kw["avatar"]
                user.save()
                self.write(self.make_result(1, "user upload OK", {"avatar_url": user.avatar_url}))
            else:
                self.write(self.make_result(0, "user not found or wrong password", None))
        except ValueError, e:
            self.write(self.make_result(0, str(e), None))
        except IOError, e:
            self.write(self.make_result(0, str(e), None))


class UserResetHandler(BaseHandler):
    def post(self, *args, **kwargs):
        User.reset()
        self.write(self.make_result(1, "user reset OK", None))


class ClubResetHandler(BaseHandler):
    def post(self, *args, **kwargs):
        Club.reset()
        self.write(self.make_result(1, "club reset OK", None))


class ClubIndexHandler(BaseHandler):
    def post(self, *args, **kwargs):
        all_clubs = Club.get_all_clubs()
        self.write(self.make_result(1, "get all clubs OK", all_clubs))


class ClubDetailHandler(BaseHandler):
    def post(self, *args, **kwargs):
        pass


class ActivityIndexByClubHandler(BaseHandler):
    def post(self, *args, **kwargs):
        cname = self.get_argument("cname", None)
        result = Activity.get_all_acts_by_club(cname)
        self.write(self.make_result(1, "get acts by club OK", result))


class ActivityResetHandler(BaseHandler):
    def post(self, *args, **kwargs):
        Activity.reset()
        self.write(self.make_result(1, "activity reset OK", None))


class ActivityIndexByTypeHandler(BaseHandler):
    def post(self, *args, **kwargs):
        t = self.get_argument("type", None)
        result = Activity.get_all_acts_by_type(t)
        self.write(self.make_result(1, "get acts by club OK", result))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    APP = tornado.web.Application(
            handlers=[
                (r'/', IndexHandler),
                (r'/api/login', LoginHandler),
                (r'/api/register', RegisterHandler),
                (r'/api/user/update', UserUpdateHandler),
                (r'/api/user/upload', UserUploadHandler),
                (r'/api/user/reset', UserResetHandler),
                (r'/api/club/reset', ClubResetHandler),
                (r'/api/club/index', ClubIndexHandler),
                (r'/api/club/detail', ClubDetailHandler),
                (r'/api/activity/get_all_acts_by_club', ActivityIndexByClubHandler),
                (r'/api/activity/get_all_acts_by_type', ActivityIndexByTypeHandler),
                (r'/api/activity/reset', ActivityResetHandler),

            ],
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            login_url='/login'
    )

    http_server = tornado.httpserver.HTTPServer(APP)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
