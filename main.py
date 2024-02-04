# 학번, 이름, 전화번호 입력
# 분실시 개인 책임을 명시, 동의받기
# 졸업자 명단과 대조 후 qr 링크 발급

# 해당 링크로 접속시 유효한 qr 코드 사진 제공
# 전화번호로 링크가 포함된 안내 문자메시지 전송

# 학사복 대여, 반납시 담당자는 개개인의 qr을 스캔.
# 누가 언제 빌려가고 반납했는지 DB에 기록



# URL 설계는 학번을 기준으로 할 것  jwjung.kro.kr/qr/202345047
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

code = 202312345
name = '카리나'
phone = '010-1234-5678'

users = {}

app = FastAPI()
templates = Jinja2Templates(directory="./")

class Input(BaseModel):
    code: int
    name: str
    phone: str

@app.get("/register")
async def register_get(request: Request):
    return templates.TemplateResponse("register.html",{"request":request})

@app.post("/register") 
def register(data : Input):
    tmp = {}
    tmp['code'] = data.code
    tmp['name'] = data.name
    tmp['phone'] = data.phone


    users[data.code] = tmp
    print(users)

    return users
