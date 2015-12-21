# -*-coding:utf-8 -*-

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from bson.json_util import dumps
from tornado.options import define, options

from models.user import User

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
        if User.is_exist(new_user_kw["name"]):
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
            "old_name": self.get_argument("old_name", None),
            "old_pwd": self.get_argument("old_pwd", None),
            "pwd": self.get_argument("pwd", None),
            "sex": self.get_argument("sex", None),
            "major": self.get_argument("major", None),
            "grade": self.get_argument("grade", None),
            "avatar":  self.request.files["avatar"][0]["body"] if "avatar" in self.request.files else None,
        }
        # if not User.authenticate(user_kw["old_name"], user_kw["old_pwd"]):
        #     self.write(self.make_result(0, "user authenticate failed", None))
        #     return
        print user_kw
        try:
            user = User.get_user(user_kw["old_name"], user_kw["old_pwd"])
            if user_kw["pwd"]:
                user.pwd = user_kw["pwd"]
            if user_kw["sex"]:
                user.sex = user_kw["sex"]
            if user_kw["major"]:
                user.major = user_kw["major"]
            if user_kw["grade"]:
                user.grade = user_kw["grade"]
            if user_kw["avatar"]:
                user.avatar_url = user_kw["avatar"]
            user.save()
            self.write(self.make_result(1, "user update OK", None))
        except ValueError, e:
            self.write(self.make_result(0, str(e), None))
        except IOError, e:
            self.write(self.make_result(0, str(e), None))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    APP = tornado.web.Application(
            handlers=[
                (r'/', IndexHandler),
                (r'/login', LoginHandler),
                (r'/register', RegisterHandler),
                (r'/user/update', UserUpdateHandler),
            ],
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            login_url='/login'
    )

    http_server = tornado.httpserver.HTTPServer(APP)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
