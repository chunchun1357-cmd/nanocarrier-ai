# Day 1 - Read particle sizes from CSV
# Goal : Load formulation_data.csv and classify particle sizes

import csv # CSV 처리 도구 불러오기

file_path = "data/formulation_data.csv" # data 폴더 안의 formulation_data.csv 파일을 사용할 것

with open(file_path, newline="", encoding="utf-8") as file: # 파일 열기 file_path에 적힌 csv 파일을 열고, 그 열린 파일을 file이라는 이름으로 부른다
    # newline은 줄바꿈을 python이 임의로 바꾸지 않게 하는 것, encoding="utf-8"은 글자를 읽는 방식을 지정. 
    reader = csv.DictReader(file) # DictReader는 CSV의 첫 줄을 열 이름으로 읽는다. 열 이름으로 값을 꺼낼 수 있게 한다.

    for row in reader: # CSV 파일에서 데이터를 한 행씩 꺼내고 아래의 과정을 반복 실행한다
        formulation_id = row["formulation_id"]
        size_text = row["particle_size_nm"] # 각 열 이름으로 값을 꺼냄. 여기의 값은 문자취급.

        if size_text == "": # size_text 값이 비어있다면
            print(formulation_id, "Missing paticle size") # Missing particle size를 출력해라. 결측치가 있으면 숫자로 바꾸다가 에러가 나서 비어있는 값은 이걸로 채우기
            continue # 다음 행으로 넘어가라

        size = float(size_text)

        if size < 150:
            print(formulation_id, size, "Small")

        elif size < 200:
            print(formulation_id, size, "Good")
        
        else:
            print(formulation_id, size, "Too large")
