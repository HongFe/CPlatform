import json

class MESSAGE_DATA:
    msg_data={}

    def __init__(self, str_msg):
        self.tmp_data=self.json_to_data(str_msg)

        self.msg_data={}
        self.msg_data['head']=self.tmp_data[0]
        self.msg_data['datetime']=self.tmp_data[1]
        self.msg_data['sentence']=self.tmp_data[2]
        self.msg_data['type']=self.tmp_data[3] ## question, answer..

    def json_to_data(self,str_msg):
        return json.loads(str_msg)


msg1=MESSAGE_DATA("{'head': 'head content1', 'datetime': '2022-12-02 17:34:32', 'sentence': '오픈시간 보여줘', 'type': 'QUESTION'}")
msg2=MESSAGE_DATA("{'head': 'head content2', 'datetime': '2022-12-02 18:23:43', 'sentence': '위치좀 알려줘', 'type': 'QUESTION'}")

print(msg1)
print(msg2)