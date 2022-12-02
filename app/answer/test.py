test_answer={'위치_문의':'[답변]위치는...','오픈시간_문의':'[답변]오픈시간은...'}

class FIND_ANSWER:
    def __init__(self,id,intent):
        self.id=id
        self.intent=intent
        self.answer=self.get_answer_by_intent(intent)


    def get_answer_by_intent(self,intent):
        ### DB에서 답변 가져오기
        return test_answer[intent]


ans1=FIND_ANSWER('BREAD_123','위치_문의')
print(ans1.answer)
ans2=FIND_ANSWER('BREAD_123','오픈시간_문의')
print(ans2.answer)