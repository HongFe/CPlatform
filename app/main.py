#-*- encode:UTF-8 -*-

import json
from datetime import datetime
import sys
from os import path

print(path.dirname(path.dirname(path.abspath(__file__))))
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from channel_message import channel_message_module
from intend_inference import intend_inference_module
from channel_interface import channel_interface_module
from language_understand import language_understand_module
from answer import answer_module


from typing import Union
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
	head: Union[str, None] = None
	company_id: str
	datetime: str
	sentence: str
	sentence_type: str ## question, answer..
	session_id: str


@app.get("/")
async def root():
	return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
	return {"message": f"Hello {name}"}

@app.get("/items/")
async def read_item(item: Item):
	item_dict=item
	return item_dict

## 테스트 주소
# http://127.0.0.1:8000/question?head=head_content1&company_id=빵집1&datetime=2022-12-02%2017:34:32&sentence=오픈시간%20보여줘&sentence_type=text&session_id=123
@app.get("/question")
async def call_test(head: Optional[str]=None,company_id: Optional[str]=None,
					channel_datetiem: Optional[str]=None, sentence: Optional[str]=None, sentence_type: Optional[str]=None,session_id: Optional[str]=None ):
	# channel_datetiem은 채널에서 보내주는 시간정보이고, start_datetime은 현재 시스템에서 전달받은 시간
	start_datetime=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) ## 날짜 다시 셋팅
	res=pipeline_test(head,company_id,start_datetime,sentence,sentence_type,session_id)
	err="Error! Some..."
	if res!=None:
		return {"status":"clear","message":f"{res}"}
	else:
		return {"status":"fail","message":f"{err}"}

def pipeline_test(*args):
	print("- 입력된 파라미터들: {}\n".format(args))
	# test1 = channel_message_module.MESSAGE_DATA("head content1", "빵집1", "2022-12-02 17:34:32", "오픈시간 보여줘", "text","123")
	test1 = channel_message_module.MESSAGE_DATA(args)
	print('[실행된 클래스]',test1.__class__)
	print('[전달할 값]',test1)

	msg1 = channel_interface_module.MESSAGE_DATA(test1.data_to_json_str())
	print('[실행된 클래스]',msg1.__class__)
	print('[전달할 값]',msg1)

	lum = language_understand_module.TEXT_ANALYTICS(msg1.company_id, msg1.sentence, msg1.sentence_type)  ## 테스트용
	print('[실행된 클래스]',lum.__class__)
	print('[전달할 값]',lum)

	iim = intend_inference_module.INTENT_ANALYTICS_TEXT(lum.company_id, lum.sentence, lum.sentence_type)  ## 테스트용
	print('[실행된 클래스]',iim.__class__)
	print('[전달할 값]',iim)

	am = answer_module.FIND_ANSWER(iim.intent)
	print('[실행된 클래스]',am.__class__)
	print('[전달할 값]',am)

	result=json.dumps({"g_session_id":msg1.g_session_id,"answer":am.answer},ensure_ascii=False)
	print('[최종 값]',result)

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
