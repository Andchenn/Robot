import itchat
from itchat.content import *
import json
import requests


@itchat.msg_register([TEXT])
def text_reply(msg):
    info = msg['Text'].encode('utf-8')
    url = 'http://www.tuling123.com/openapi/api'
    data = {u"key": "这里填入你的API-key", "info": info, u"loc": "", "userid": ""}
    response = requests.post(url, data).content
    s = json.loads(response, encoding='utf-8')
    print('s == %s' % s)
    if s['code'] == 100000:
        itchat.send(s['text'], msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run(debug=True)
