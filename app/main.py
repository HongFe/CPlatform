#-*- encode:UTF-8 -*-

# if __name__ == '__main__':
# 	if __package__ is None:
# 		import sys
# 		from os import path
# 		print(path.dirname( path.dirname( path.abspath(__file__) ) ))
# 		sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
# 		from channel_message import channel_message_module
# 		from intend_inference import intend_inference_module
# 		from channel_interface import channel_interface_module
# 		from language_understand import language_understand_module
# 		from answer import answer_module
# 	else:
# 		from .channel_message import channel_message_module
# 		from .intend_inference import intend_inference_module
# 		from .channel_interface import channel_interface_module
# 		from .language_understand import language_understand_module
# 		from .answer import answer_module
import json
import sys
from os import path

print(path.dirname(path.dirname(path.abspath(__file__))))
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from channel_message import channel_message_module
from intend_inference import intend_inference_module
from channel_interface import channel_interface_module
from language_understand import language_understand_module
from answer import answer_module

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
async def root():
	return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
	return {"message": f"Hello {name}"}


@app.get("/question")
async def call_test():
	return {"message": pipeline_test()}


### 순서


def pipeline_test():
	test1 = channel_message_module.MESSAGE_DATA("head content1", "빵집1", "2022-12-02 17:34:32", "오픈시간 보여줘", "text",
												"123")
	print(test1)

	msg1 = channel_interface_module.MESSAGE_DATA(test1.data_to_json_str())
	print(msg1)

	lum = language_understand_module.TEXT_ANALYTICS(msg1.company_id, msg1.sentence, msg1.sentence_type)  ## 테스트용
	print(lum)

	iim = intend_inference_module.INTENT_ANALYTICS_TEXT(lum.company_id, lum.sentence, lum.sentence_type)  ## 테스트용
	print(iim)

	am = answer_module.FIND_ANSWER(iim.intent)
	print(am)

	result=json.dumps({"answer":am.answer},ensure_ascii=False)
	print(result)
	return result


'''
channel_message
test1=MESSAGE_DATA("head content1","빵집1","2022-12-02 17:34:32", "오픈시간 보여줘","QUESTION","123")
print(test1.data_to_json())

channel_interface
msg1=MESSAGE_DATA('{"head": "head content1","company_id":"빵집1" ,"datetime": "2022-12-02 17:34:32", "sentence": "오픈시간 보여줘", "sentence_type": "text", "session_id":"12345"}')
print(msg1.msg_data)

language_understand
test1=TEXT_ANALYTICS('빵집1','위치알고싶어','text') ## 테스트용
test1.company_id, test1.sentenc, test1.sentence_type

intend_inference
test1=INTENT_ANALYTICS_TEXT('빵집1','위치알고싶어','text') ## 테스트용
test1.intent

answer
ans1=FIND_ANSWER('위치_문의')
print(ans1.answer)
'''
