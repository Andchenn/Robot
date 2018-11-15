# import json
# import urllib.request
#
# api_url = "http://openapi.tuling123.com/openapi/api/v2"
# text_input = input('我：')
#
# req = {
#     "perception":
#         {
#             "inputText":
#                 {
#                     "text": text_input
#                 },
#             "selfInfo":
#                 {
#                     "location":
#                         {
#                             "city": "广州",
#                             "province": "广州",
#                             "street": "越秀区"
#                         }
#                 }
#         },
#     "userInfo":
#         {
#             "apiKey": "75d09346247d46839168e4a97d8e5404",
#             "userId": "OnlyUserAlphabet"
#         }
# }
# req = json.dumps(req).encode('utf-8')
#
# http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
# response = urllib.request.urlopen(http_post)
# response_str = response.read().decode('utf-8')
# response_dic = json.loads(response_str)
#
# intent_code = response_dic['intent']['code']
# results_text = response_dic['results'][0]['values']['text']
# print('code:' + str(intent_code))
# print('text:' + results_text)

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
