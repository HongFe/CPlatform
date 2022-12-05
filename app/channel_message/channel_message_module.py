import json

'''
- 채널에서 필요한 값을 전달 (TEST)
- DATA
    - 전달값: head, 입력일시, 문장, 데이터 타입, 세션ID(채널)
'''

class MESSAGE_DATA:
    msg_data={}

#    def __init__(self,msg_head,company_id,msg_datetime,msg_sentence,msg_type,msg_session_id):
    def __init__(self,msg):
        self.msg_data={}
        self.msg_data['head']=msg[0]
        self.msg_data['company_id']=msg[1]
        self.msg_data['datetime']=msg[2]
        self.msg_data['sentence']=msg[3]
        self.msg_data['sentence_type']=msg[4] ## question, answer..
        self.msg_data['session_id']=msg[5]

    def __str__(self):
        return f"MESSAGE_DATA({self.msg_data})"

    def data_to_json_str(self):
        return json.dumps(self.msg_data)




'''============================TEST============================'''
if __name__ == '__main__':
    test1=MESSAGE_DATA(["head content1","빵집1","2022-12-02 17:34:32", "오픈시간 보여줘","QUESTION","123"])
    test2=MESSAGE_DATA(["head content2","식당1","2022-12-02 18:23:43", "위치좀 알려줘","QUESTION","124"])

    ##### test print
    print(test1.msg_data)
    print(test1.data_to_json_str())
    print(json.loads(test1.data_to_json_str()))

'''================================================================'''