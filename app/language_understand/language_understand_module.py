
'''
- 전달받은 문장을 이해하고 전처리
- DATA
    - request: 회사ID, 문장, 문장타입(text, voice)
    - response: 문장 타입에 맞는 적합한 전처리후 의도분석기에 전달
- TO
    - 답변을 찾아주는 시스템에 전달

'''
class TEXT_ANALYTICS:
    def __init__(self,company_id,sentence,sentence_type):

        self.company_id=company_id
        self.sentence_type=sentence_type

        if sentence_type=='text':
            self.sentence =self.pre_handling_text(sentence)

        elif sentence_type=='voice':
            self.sentence =self.pre_handling_voice(sentence)

    def __str__(self):
        return f"TEXT_ANALYTICS({self.company_id,self.sentence,self.sentence_type}"

    def pre_handling_text(self,sentence):
        ## 문장 가공 불필요시 X
        sentence='[수정됨]'+sentence
        return sentence

    def pre_handling_voice(self,sentence):
        ## 문장 가공 불필요시 X
        sentence='[수정됨]'+sentence
        return sentence

'''============================TEST============================'''
if __name__ == '__main__':
    test1=TEXT_ANALYTICS('빵집1','위치알고싶어','text') ## 테스트용
    print(test1.sentence)
    print(test1)


'''================================================================'''