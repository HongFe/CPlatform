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

from db_handler import DB_HANDLER
import _property

USER_TB = _property.USER_TB
COMPANY_TB = _property.COMPANY_TB
USER_COMPANY_TB = _property.USER_COMPANY_TB
CHANNEL_TB = _property.CHANNEL_TB
INTENT_TB = _property.INTENT_TB
ANSWER_TB = _property.ANSWER_TB
QUESTION_TB = _property.QUESTION_TB



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

        self.get_company_info(self.company_id) ## 회사정보 확인

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

    ## 회사 ID로 정보 가져오기
    def get_company_info(self, company_id):
        try:
            db = DB_HANDLER()
            data = db.select_tb(COMPANY_TB, "select * from {} where id_pk={}".format(COMPANY_TB, company_id))
            # print(data)
            print("\033[92m[SUCCESS] \033[97m회사 정보 가져오기 성공")
        except Exception as e:
            print("\033[41m[FAIL] \033[97m회사 정보 가져오기 실배", e)

    def print_data(self):
        print('{},{},{},{},{},{},{}'.format(self.head,self.company_id,self.datetime,self.sentence,
        self.sentence_type,self.session_id,self.g_session_id))


'''============================TEST============================'''
if __name__ == '__main__':
    msg1 = MESSAGE_DATA(
        '{"head": "head content1","company_id":"1" ,"datetime": "2022-12-02 17:34:32", "sentence": "오픈시간 보여줘", "sentence_type": "text", "session_id":"12345"}')
    msg2 = MESSAGE_DATA(
        '{"head": "head content2", "company_id":"2","datetime": "2022-12-02 18:23:43", "sentence": "위치좀 알려줘", "sentence_type": "text", "session_id":"125"}')
    print(msg1.sentence)
    print(msg1)
'''================================================================'''