# Last Update Date: 2020/11/14

#(완료)1주차-데이터 저장 형식 json. 저장 포맷은 README.md에 상세기재
import json
from os import read
from datetime import datetime

#전역변수 - 오늘날짜
today = datetime.today().strftime("%Y%m%d")

#(완료)1주차-데이터 read 함수 구현
def read_data(file_name):
    data_list = []
    with open(file_name, encoding='utf-8') as json_file:
        data_list = json.load(json_file)
    return data_list

#(완료)2주차-데이터 write 함수 추가
def save_data(file_name, list):
    data_list = read_data(file_name)
    data_list.extend(list)
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=4)

#(완료)1주차-메인화면(최초 접속 화면) 구현
def print_menu():
    print ('===============================')
    print ('    <나만의 건강 다이어리>    ')
    print ('===============================')
    print ('1. 식단기록     2. 운동기록')
    print ('3. 휴식기록     4. 수면기록')
    print ('5. 보고서 확인  6. 종료')
    print ('===============================')
    print ()

#(완료)2주차-식단기록 함수 구현
def food_record():
    food_data = []
    foods = []
    print('<식단을 기록해보자>')
    print ('===============================')
    print ('1. 아침 2. 점심 3. 저녁 4. 간식')
    print ('===============================')
    
    f_type = input('식사종류(1~4): ')
    f_time = input('식사시간(hh:mm): ')
    f_name = input('식품명: ')
    f_amount = input('섭취량(g): ')
    f_calorie = input('칼로리(kcal): ')
    foods.append({"name":f_name, "amount":f_amount, "calorie":f_calorie})
    while True:
        choice = input('추가입력 여부(Y/N): ')
        if choice == 'Y' or choice == 'y':
            f_name = input('식품명: ')
            f_amount = input('섭취량(g): ')
            f_calorie = input('칼로리(kcal): ')
            foods.append({"name":f_name, "amount":f_amount, "calorie":f_calorie})
        elif choice == 'N' or choice == 'n':
            food_data.append({"date": today, "type":f_type, "time":f_time, "food": foods})
            save_data('diary_food.txt', food_data)
            print('식단을 저장했습니다!')
            break
        else:
            print ("잘못된 값 입력")

#(완료)2주차-운동기록 함수 구현 
def workout_record():
    workout_data = []
    print('<운동을 기록해보자>')
    w_name = input('운동명: ')
    w_starttime = input('시작시간(hh:mm): ')
    w_endtime = input('종료시간(hh:mm): ')
    w_condition = input('컨디션(1~10): ')
    workout_data.append({"date":today, "name":w_name, "starttime":w_starttime, "endtime":w_endtime, "condition":w_condition})
    while True:
        choice = input('추가입력 여부(Y/N): ')
        if choice == 'Y' or choice == 'y':
            w_name = input('운동명: ')
            w_starttime = input('시작시간(hh:mm): ')
            w_endtime = input('종료시간(hh:mm): ')
            w_condition = input('컨디션(1~10): ')
            workout_data.append({"date":today, "name":w_name, "starttime":w_starttime, "endtime":w_endtime, "condition":w_condition})
        elif choice == 'N' or choice == 'n':
            save_data('diary_workout.txt', workout_data)
            print('운동을 저장했습니다!')
            break
        else:
            print ("잘못된 값 입력")

#(예정)3주차-휴식기록 함수 구현 
def rest_record():
    print('<휴식을 기록해보자>')

#(예정)3주차-수면기록 함수 구현
def sleep_record():
    print('<수면을 기록해보자>')

#(예정)4주차-보고서 생성 함수 구현
def create_report(): 
    print('<일주일 건강 보고서>')

#(완료)1주차-메인 함수 구현
def main():
    while True:
        print_menu()
        choice = input('번호 선택: ')
        if choice == '1':
            food_record()
        elif choice == '2':
            workout_record()
        elif choice == '3':
            rest_record()
        elif choice == '4':
            sleep_record()
        elif choice == '5':
            create_report()
        elif choice == '6':
            print('종료')
            break
        else:
            print ("잘못된 값 입력")
        print()

#메인 함수 실행
if __name__ == '__main__': 
  main()

#(예정)5주차-README.md 파일에 프로그램 설명 작성