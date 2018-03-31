# -*- coding: utf-8 -*-

import web

class Index(object):
    def GET(self):
        data = web.input()
        if len(data) == 0:
            return "Hello,Welcome to XB's Home Page.\nwww.logread.cn"