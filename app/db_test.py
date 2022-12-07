from db_handler import DB_HANDLER

# ========================= DB정보 및 생성 =========================
# 명명 규칙 https://velog.io/@jkijki12/Database-이름-짓기-어려우세요

tb_name_list = ['X_USER_TB','X_COMPANY_TB','X_USER_COMPANY_TB','X_CHANNEL_TB','X_INTENT_TB','X_ANSWER_TB','X_QUESTION_TB']

USER_TB='X_USER_TB'
COMPANY_TB='X_COMPANY_TB'
USER_COMAPNY_TB='X_USER_COMPANY_TB'
CHANNEL_TB='X_CHANNEL_TB'
INTENT_TB='X_INTENT_TB'
ANSWER_TB='X_ANSWER_TB'
QUESTION_TB='X_QUESTION_TB'

create_query_list =[
    "CREATE TABLE {} (\
             id_pk INTEGER PRIMARY KEY,\
             user_id TEXT NOT NULL,\
             password TEXT NOT NULL,\
             name TEXT NOT NULL,\
             phonenumber TEXT NOT NULL,\
             email TEXT NOT NULL\
             );".format(USER_TB),
    "CREATE TABLE {} (\
             id_pk INTEGER PRIMARY KEY,\
             name TEXT NOT NULL,\
             phonenumber TEXT NOT NULL,\
             email TEXT NOT NULL\
             );".format(COMPANY_TB),
    "CREATE TABLE {} (\
             role TEXT NOT NULL,\
             user_id_fk TEXT,\
             user_name_fk TEXT,\
             company_id_fk TEXT,\
             company_name_fk TEXT\
             );".format(USER_COMAPNY_TB,USER_TB,USER_TB,COMPANY_TB,COMPANY_TB),
             # user_id_fk TEXT,\
             # FOREIGN KEY (user_id_fk)\
             #    REFERENCES {} (id)\
             #        ON UPDATE RESTRICT\
             #        ON DELETE RESTRICT\
             # user_name_fk TEXT,\
             # FOREIGN KEY (user_name_fk)\
             #    REFERENCES {} (name) \
             #        ON UPDATE RESTRICT\
             #        ON DELETE RESTRICT\
             # company_id_fk TEXT,\
             # FOREIGN KEY (company_id_fk)\
             #    REFERENCES {} (id)\
             #        ON UPDATE RESTRICT\
             #        ON DELETE RESTRICT\
             # company_name_fk TEXT\
             # FOREIGN KEY (company_name_fk)\
             #    REFERENCES {} (name)\
             #        ON UPDATE RESTRICT\
             #        ON DELETE RESTRICT\
             # );".format(USER_COMAPNY_TB,USER_TB,USER_TB,COMPANY_TB,COMPANY_TB),
    "CREATE TABLE {} (\
             id_pk INTEGER PRIMARY KEY,\
             name TEXT NOT NULL,\
             type TEXT,\
            company_id_fk TEXT,\
            company_name_fk TEXT\
            );".format(CHANNEL_TB,COMPANY_TB,COMPANY_TB),
             # company_id_fk TEXT,\
             # FOREIGN KEY (company_id_fk)\
             #    REFERENCES {} (id)\
             #        ON UPDATE RESTRICT\
             #        ON DELETE RESTRICT\
             # company_name_fk TEXT\
             # FOREIGN KEY (company_name_fk)\
             #    REFERENCES {} (name)\
             #        ON UPDATE RESTRICT\
             #        ON DELETE RESTRICT\
             # );".format(CHANNEL_TB,COMPANY_TB,COMPANY_TB),
    "CREATE TABLE {} (\
             id_pk INTEGER PRIMARY KEY,\
             intent TEXT NOT NULL,\
             company_id_fk TEXT\
             );".format(INTENT_TB, COMPANY_TB),
             # company_id_fk TEXT\
             # FOREIGN KEY (company_id_fk)\
             #    REFERENCES {} (id)\
             #        ON UPDATE RESTRICT\
             #        ON DELETE RESTRICT\
             # );".format(INTENT_TB, COMPANY_TB),

    "CREATE TABLE {} (\
             id_pk INTEGER PRIMARY KEY,\
             answer TEXT NOT NULL,\
             type TEXT NOT NULL,\
             intent_id_fk TEXT\
             );".format(ANSWER_TB,INTENT_TB),
             # intent_id_fk TEXT\
             # FOREIGN KEY (intent_id_fk)\
             #    REFERENCES {} (id)\
             #        ON UPDATE RESTRICT\
             #        ON DELETE RESTRICT\
             # );".format(ANSWER_TB,INTENT_TB),
    "CREATE TABLE {} (\
             id_pk INTEGER PRIMARY KEY,\
             question TEXT NOT NULL,\
             type TEXT NOT NULL,\
             answer_id_fk TEXT\
             );".format(QUESTION_TB, ANSWER_TB)
             # answer_id_fk TEXT\
             # FOREIGN KEY (answer_id_fk)\
             #    REFERENCES {} (id)\
             #        ON UPDATE RESTRICT\
             #        ON DELETE RESTRICT\
             # );".format(QUESTION_TB, ANSWER_TB)
               ]
values_list = [
    ( # USER TB
        ('abc123', '12w345', '홍길동', '010-0000-1111', 'abcd@abc.com'),
        ('test2', '1212d', '영심이', '010-1100-2233', 'bvc@zoo.com'),
        ('anvc123', '0293d', '루피', '010-3344-2222', 'anvc@abc.com')
    ),
    ( # COMPANY_TB
        ('화리화게트', '070-0000-0000', 'help@abc.com'),
        ('은평식당', '070-0000-1001', 'help@zoo.com')
    ),
    ( # USER_COMPANY_TB
        ('Admin','홍길동key','홍길동','화리화게트key','화리화게트'),
        ('ServiceAdmin','영심이key','영심이','화리화게트key','화리화게트'),
        ('Admin','루피key','루피','은평식당key','은평식당'),
    ),
    ( # CHANNEL_TB
        ('카카오톡_챗봇', 'text', '화리화게트거key....', '화리화게트'),
        ('카카오톡_챗봇', 'text', '은평식당key....', '은평식당')
    ),
    ( # INTENT_TB
        ('[위치_문의]', '화리화게트거id....'),
        ('[오픈시간_문의]', '화리화게트거id....'),
        ('[위치문의]', '은평식당id....'),
        ('[오픈시간_문의]', '은평식당id....')
    ),
    ( # ANSWER
        ('위치질문답변...', 'text', '[위치_문의] id'),
        ('오픈시간답변...', 'text', '[오픈시간_문의] id'),
        ('위치질문답변...', 'text', '[위치문의] id'),
        ('오픈시간답변...', 'text', '[오픈시간_문의] id')
    ),
    ( # QUESTION
        ('어딨어', 'text', '[위치질문답변] id'),
        ('오픈시간 알려줘', 'text', '[오픈시간답변] id'),
        ('어디 입니까', 'text', '[위치질문답변] id'),
        ('언제 열어요', 'text', '[오픈시간답변] id')
    )
    ]
insert_query_list = [
    "INSERT INTO {} (user_id, password, name, phonenumber, email) VALUES (?,?,?,?,?);".format(USER_TB),
    "INSERT INTO {} (name, phonenumber, email) VALUES (?,?,?);".format(COMPANY_TB),
    "INSERT INTO {} (role,user_id_fk,user_name_fk,company_id_fk,company_name_fk) VALUES (?,?,?,?,?);".format(USER_COMAPNY_TB),
    "INSERT INTO {} (name, type, company_id_fk, company_name_fk) VALUES (?,?,?,?);".format(CHANNEL_TB),
    "INSERT INTO {} (intent, company_id_fk) VALUES (?,?);".format(INTENT_TB),
    "INSERT INTO {} (answer, type, intent_id_fk) VALUES (?,?,?);".format(ANSWER_TB),
    "INSERT INTO {} (question, type, answer_id_fk) VALUES (?,?,?);".format(QUESTION_TB),
    ]

############################## MAIN ##############################

if __name__ == "__main__":
    db = DB_HANDLER()

    for tb_name, create_query, insert_query, values in zip(tb_name_list, create_query_list, insert_query_list, values_list):
        db.set_tb_for_test(tb_name, create_query, insert_query, values)



'''
========= 사용자 정보 (고객사 등)
[X_USER_TB]
ID_PK: [PK] 사용자 ID
USER_ID: 사용자가 쓰는 ID
PASSWORD: 암호 (암호화 필수)
NAME: 사용자 이름
PHONENUMBER: 사용자 연락처
EMAIL: 사용자 이메일

========= 회사(고객사) 정보
[X_COMPANY_TB]
ID_PK: [PK] 회사 ID
NAME: 회사 이름
PHONENUMBER: 회사 연락처 (추후 상담 문의를 포워딩 할 대상임)
EMAIL: 회사 이메일 (추후 상담 문의를 포워딩 할 대상임

========= 회사(고객사)-사용자 매핑 정보
[X_USER_COMPANY_TB]
ROLE: 역할 [Admin/ServiceAdmin/ServiceSubAdmin] -> admin은 총 관리자! 우리가됨
USER_ID_FK: [FK] 유저테이블의 아이디
USER_NAME_FK: [FK] 유저테이블의 이름
COMPANY_ID_FK: [FK] 회사정보 테이블의 회사ID 
COMPANY_NAME_FK: [FK] 회사정보 테이블의 회사이름

========= 회사별 채널 정보
[X_CHANNEL_TB]
ID_PK: [PK] 채널 별도 ID
NAME: 채널이름
TYPE: 채널 유형 [text/ voice]
COMPANY_ID_FK: [FK] 회사정보 테이블의 회사ID 
COMPANY_NAME_FK: [FK] 회사정보 테이블의 회사이름

CREATE TABLE X_CHANNEL_TB (ID_PK PRIMARYKEY text, NAME text, TYPE text, COMPANY_ID_FK text, COMPANY_NAME_FK text)
INSERT INTO TABLE X_CHANNEL_TB(ID_PK, NAME, TYPE, COMPANY_ID_FK, COMPANY_NAME_FK) VALUES () 

========= 인텐트
[X_INTENT_TB]
ID: 의도의 ID값
INTENT: 의도명
COMPANY_ID_FK: [FK] 회사 테이블의 ID값

========= 질문/답변 set (추론모델 및 답변 활용) : 답변
[X_ANSWER_TB]
ID: 답변의 ID값
ANSWER: 답변
TYPE: 채널 유형 [text/ voice]
INTENT_ID_FK: [FK] 인텐트 테이블의 ID값

========= 질문/답변 set (추론모델 및 답변 활용) : 질문(예문들)
[X_QUESTION_TB]
ID: 질문의 ID값
QUESTION: 질문 
TYPE: 채널 유형 [text/ voice]
ANSWER_ID_FK: 답변 테이블의 ID값 (질문은 반드시 답변이 있어야함)
'''

'''
========= 회사별 질문 응답 템플릿 정보????? -> NoSQL?
=> 질문답변 테이블과 이어져야할듯????? 안해도 될듯??
[X_TEMPLET_TB]
'''

'''
========= 서비스 로그
X_SERVICE_HIST


========= 고객 로그(서비스 사용자)
X_USER_HIST

========= 추론 모델 로그???
X_MODEL_HIST


'''

''' update 수정법
# ? 표시자를 활용 - 튜플 입력
cur.execute("UPDATE '210227_test' SET name = ? WHERE id_num = ?", ('YB_수정', 4))

# 딕셔너리 활용(key : value형태)
cur.execute("UPDATE '210227_test' SET name = :username WHERE id_num = :id", {"username":'Banana', "id":'3'})

# %s 표시자를 활용 - 튜플 입력
cur.execute("UPDATE '210227_test' SET name = '%s' WHERE id_num = '%s'" % ('2', 'LaLALand'))
'''
