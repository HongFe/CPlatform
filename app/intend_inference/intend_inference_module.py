'''
- 전달받은 문장의 의도를 파악함
- DATA
    - request: 회사ID, 문장, 문장 타입
    - response: 의도를 파악 (의도DB 연결 필요)
- TO
    - 답변을 찾아주는 시스템에 전달

'''

test_intent_db={}


class INTENT_ANALYTICS:
    def __init__(self,company_id, sentence, sentence_type):
        self.intent=self.inference_intent(company_id, sentence)

    def inference_intent(self, company_id, sentence):
        # TODO: 회사ID기준 의도 찾기
        return None ## 테스트용

class INTENT_ANALYTICS_TEXT(INTENT_ANALYTICS):
    def __init__(self,company_id, sentence, sentence_type):
        super().__init__(company_id, sentence, sentence_type)

    def inference_intent(self, company_id, sentence):
        # TODO: 회사ID기준 의도 찾기
        ## set_intent, get_intent...
        return '위치_문의' ## 테스트용


'''============================TEST============================'''
if __name__ == '__main__':
    test1=INTENT_ANALYTICS_TEXT('빵집1','위치알고싶어','text') ## 테스트용
    print(test1.intent)


'''================================================================'''