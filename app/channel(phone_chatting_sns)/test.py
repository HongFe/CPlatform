import json

class MESSAGE_DATA:
    msg_data={}

    def __init__(self,msg_head,msg_datetime,msg_sentence,msg_type):
        self.msg_data={}
        self.msg_data['head']=msg_head
        self.msg_data['datetime']=msg_datetime
        self.msg_data['sentence']=msg_sentence
        self.msg_data['type']=msg_type ## question, answer..

    def data_to_json(self):
        return json.dumps(self.msg_data)


test1=MESSAGE_DATA("head content1","2022-12-02 17:34:32", "오픈시간 보여줘","QUESTION")
test2=MESSAGE_DATA("head content2","2022-12-02 18:23:43", "위치좀 알려줘","QUESTION")

##### test print
print(test1.msg_data)
print(test1.data_to_json())
print(json.loads(test1.data_to_json()))