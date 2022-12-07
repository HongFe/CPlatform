import json
import random

'''
- 채널로부터 값을 전달받음
- DATA
    - request: 메시지 헤드, 회사명(고객사),입력일시, 문장(text, voice), 유형, 세션ID 
    - response:

- TO
    - 전달받은 데이터를 메시징 시스템(현재 없으니 언어이해로 전달)
'''
##### DB




class MESSAGE_DATA:
    def __init__(self, str_msg):
        self.tmp_data = self.json_to_data(str_msg)

        self.head = self.tmp_data['head']
        self.company_id = self.tmp_data['company_id']
        self.datetime= self.tmp_data['datetime']
        self.sentence = self.tmp_data['sentence']
        self.sentence_type = self.tmp_data['sentence_type']  ## question, answer..
        self.session_id= self.tmp_data['session_id']
        self.g_session_id = self.create_session_id()  # 상담 단위로 안겹치도록 해야함 -> session ID 통합관리 DB 필요할듯

    def __str__(self):
        return f"MESSAGE_DATA({self.head,self.company_id,self.datetime,self.sentence, self.sentence_type,self.session_id,self.g_session_id})"

    # 전달받은 json데이터를 포맷에 맞추어 변형
    def json_to_data(self, str_msg):
        res = json.loads(str_msg)
        return res

    def create_session_id(self):
        # TODO: session id 안겹치도록 생성 필요
        new_session_id = str(random.randint(1, 99999))  # 임시로 랜덤값
        return new_session_id

    def print_data(self):
        print('{},{},{},{},{},{},{}'.format(self.head,self.company_id,self.datetime,self.sentence,
        self.sentence_type,self.session_id,self.g_session_id))


'''============================TEST============================'''
if __name__ == '__main__':
    msg1 = MESSAGE_DATA(
        '{"head": "head content1","company_id":"빵집1" ,"datetime": "2022-12-02 17:34:32", "sentence": "오픈시간 보여줘", "sentence_type": "text", "session_id":"12345"}')
    msg2 = MESSAGE_DATA(
        '{"head": "head content2", "company_id":"식당2","datetime": "2022-12-02 18:23:43", "sentence": "위치좀 알려줘", "sentence_type": "text", "session_id":"125"}')
    print(msg1.sentence)
    print(msg1)
'''================================================================'''