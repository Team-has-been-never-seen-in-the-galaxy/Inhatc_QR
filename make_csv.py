import csv

def make(file_name, data):
    with open(str(file_name) + ".csv", mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        
        # 헤더를 쓰려면 필요하다면 아래 주석을 해제
        # writer.writerow(["거래일시", "의뢰인/수취인", "입금금액"])
        
        # 데이터 쓰기
        writer.writerow([data['학번'], data['이름'], data['전화번호']])