'''
- 전달받은 문장의 의도를 파악함
- DATA
    - request: 회사ID, 문장, 문장 타입
    - response: 의도를 파악 (의도DB 연결 필요)
- TO
    - 답변을 찾아주는 시스템에 전달

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

test_intent_db={}


class INTENT_ANALYTICS:
    def __init__(self,company_id, sentence, sentence_type):
        self.intent=self.inference_intent(company_id, sentence)

    def __str__(self):
        return f"INTENT_ANALYTICS({self.intent})"

    def inference_intent(self, company_id, sentence):
        # TODO: 회사ID기준 의도 찾기
        pass

class INTENT_ANALYTICS_TEXT(INTENT_ANALYTICS):
    def __init__(self,company_id, sentence, sentence_type):
        super().__init__(company_id, sentence, sentence_type)

    def inference_intent(self, company_id, sentence):
        # TODO: 회사ID기준 의도 찾기
        ## set_intent, get_intent...
        try:
            db = DB_HANDLER()
            data = db.select_tb(QUESTION_TB, "select * from {}".format(QUESTION_TB)) ## 질문을 통해 인텐트 ID 찾기

            for i in data:
                if i[1] in sentence: ## 등록된 질문과 유사한 것 찾기
                 intent_id = i[3]

            print("\033[92m[SUCCESS] \033[97m추론된 의도 가져오기 성공")
        except Exception as e:
            intent_id = 'No Intent'
            print("\033[41m[FAIL] \033[97m추론된 의도 가져오기 실배", e)
        finally:
           return intent_id


'''============================TEST============================'''
if __name__ == '__main__':
    test1=INTENT_ANALYTICS_TEXT('1','어딨어','text') ## 테스트용
    print(test1.intent)
    print(test1)


'''================================================================'''