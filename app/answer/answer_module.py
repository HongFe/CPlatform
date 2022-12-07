'''
- 전달받은 의도에 맞는 답변을 찾아줌
- DATA
  - request: 의도
  - response: 답변
'''
from db_handler import DB_HANDLER
import _property

USER_TB = _property.USER_TB
COMPANY_TB = _property.COMPANY_TB
USER_COMPANY_TB = _property.USER_COMPANY_TB
CHANNEL_TB = _property.CHANNEL_TB
INTENT_TB = _property.INTENT_TB
ANSWER_TB = _property.ANSWER_TB
QUESTION_TB = _property.QUESTION_TB


test_answer_db={'[위치_문의] id':'[답변]위치는...','[오픈시간_문의] id':'[답변]오픈시간은...'}

class FIND_ANSWER:
    def __init__(self,intent_id):
        self.intent_id=intent_id
        self.answer=self.get_answer_by_intent(intent_id)

    def __str__(self):
        return f"FIND_ANSWER({self.intent_id,self.answer})"

    def get_answer_by_intent(self, intent_id):
        # TODO: DB연결하여 가져오기
        try:
            db = DB_HANDLER()
            data = db.select_tb(ANSWER_TB, "select * from {} where intent_id_fk={}".format(ANSWER_TB, intent_id))


            for i in data:
                if i[3] == intent_id:
                    answer = i[1]
            print("\033[92m[SUCCESS] \033[97m인텐트 답변 가져오기 성공")
        except Exception as e:
            answer = 'No Answer'
            print("\033[41m[FAIL] \033[97m인텐트 답변 가져오기 실배",e)
        finally:
            return answer

'''============================TEST============================'''
if __name__ == '__main__':
    ans1=FIND_ANSWER('1')
    print(ans1)
    ans2=FIND_ANSWER('2')
    print(ans2)
'''================================================================'''