class TEXT_ANALYTICS:
    def __init__(self):
        pass

    def pre_handling(self,sentence):
        ## 문장 가공 불필요시 X
        self.fixed_sentence=sentence
        return self.fixed_sentence