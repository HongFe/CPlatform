'''
- 전달받은 의도에 맞는 답변을 찾아줌
- DATA
  - request: 의도
  - response: 답변
'''

test_answer_db={'위치_문의':'[답변]위치는...','오픈시간_문의':'[답변]오픈시간은...'}

class FIND_ANSWER:
    def __init__(self,intent_name):
        self.intent_name=intent_name
        self.answer=self.get_answer_by_intent(intent_name)

    def __str__(self):
        return f"FIND_ANSWER({self.intent_name,self.answer})"

    def get_answer_by_intent(self,intent_name):
        # TODO: DB연결하여 가져오기
        return test_answer_db[intent_name] # 임시로 값 가져오기


'''============================TEST============================'''
if __name__ == '__main__':
    ans1=FIND_ANSWER('위치_문의')
    print(ans1)
    ans2=FIND_ANSWER('오픈시간_문의')
    print(ans2)
'''================================================================'''