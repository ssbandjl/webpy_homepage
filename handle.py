# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import reply
import receive
import web

class Handle(object):
    def GET(self): #如果微信服务器发送GET请求,则走验证token的流程
        try:
            data = web.input() #接受微信服务器的数据
            if len(data) == 0:
                return "Hello,Welcome to MyTest Page."
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "wqqyq" #请按照公众平台官网\基本配置中信息填写
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return "" #微信服务器在五秒内收不到响应会断掉连接，并且重新发起请求，总共重试三次。假如服务器无法保证在五秒内处理并回复，可以直接回复空串，微信服务器不会对此作任何处理，并且不会发起重试
        except Exception, Argument:
            return Argument
        
    def POST(self): #如果微信服务器发送POST请求...
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData #将微信服务器POST的数据打印出来
            recMsg = receive.parse_xml(webData)
            print "recMsg:", recMsg
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
		    user_content = recMsg.Content
		    print "user_content:", user_content
		    content = "您的输入:"+user_content+"\n"+"您好！欢迎关注【无情却有情】, 影视、情感、小说等更多资源正在建设中，敬请等待..."
		    replyMsg = reply.TextMsg(toUser, fromUser, content)
		    return replyMsg.send()
		if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
            else:
                print "暂且不处理"
                return "success" #假如服务器无法保证在五秒内处理回复，则必须回复“success”或者“”（空串），否则微信后台会发起三次重试
        except Exception, Argment:
            return Argment
