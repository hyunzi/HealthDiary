# Last Update Date: 2020/11/29

#(완료)1주차-데이터 저장 형식 json. 저장 포맷은 README.md에 상세기재
import json
import math
from os import read, startfile
from datetime import datetime, timedelta

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

def input_time(title):
    while True:
        i_time = input(title+'시간(hh:mm): ')
        if i_time.find(':') == -1:
            print("잘못된 값 입력")
        else:
            hh = i_time.split(':')[0]
            mm = i_time.split(':')[1]
            if not (hh.isdigit() and mm.isdigit()):
                print("잘못된 값 입력")
            elif not (int(hh) >= 00 and int(hh) <= 23):
                print("잘못된 값 입력")
            elif not (int(mm) >= 00 and int(mm) <= 59):
                print("잘못된 값 입력")
            else: break
    return i_time

def input_food():
    while True:
        f_name = input('식품명: ')
        if len(f_name) < 1 or len(f_name) > 100:
            print("잘못된 값 입력")
        else: break
    while True:
        f_amount = input('섭취량(g): ')
        if not f_amount.isdigit():
            print("잘못된 값 입력")
        else: break
    while True:
        f_calorie = input('칼로리(kcal): ')
        if not f_calorie.isdigit():
            print("잘못된 값 입력")
        else: break
    return f_name, f_amount, f_calorie

def input_workout():
    while True:
        w_name = input('운동명: ')
        if len(w_name) < 1 or len(w_name) > 100:
            print("잘못된 값 입력")
        else: break
    w_starttime = input_time('시작')
    w_endtime = input_time('종료')
    while True:
        w_condition = input('컨디션(1~10): ')
        if not w_condition.isdigit():
            print("잘못된 값 입력")
        else: break
    return w_name, w_starttime, w_endtime, w_condition

def input_rest():
    while True:
        r_name = input('휴식명: ')
        if len(r_name) < 1 or len(r_name) > 100:
            print("잘못된 값 입력")
        else: break
    r_starttime = input_time('시작')
    r_endtime = input_time('종료')
    while True:
        r_condition = input('컨디션(1~10): ')
        if not r_condition.isdigit():
            print("잘못된 값 입력")
        else: break
    return r_name, r_starttime, r_endtime, r_condition

def input_sleep():
    s_starttime = input_time('시작')
    s_endtime = input_time('종료')
    while True:
        s_condition = input('컨디션(1~10): ')
        if not s_condition.isdigit():
            print("잘못된 값 입력")
        else: break
    return s_starttime, s_endtime, s_condition

#(완료)2주차-식단기록 함수 구현
def food_record():
    food_data = []
    foods = []
    print('<식단을 기록해보자>')
    print ('===============================')
    print ('1. 아침 2. 점심 3. 저녁 4. 간식')
    print ('===============================')
    
    while True:
        f_type = input('식사종류(1~4): ')
        if f_type not in ['1', '2', '3', '4']:
            print("잘못된 값 입력")
        else: break
    f_time = input_time('식사')
    f_name, f_amount, f_calorie = input_food()
    foods.append({"name":f_name, "amount":f_amount, "calorie":f_calorie})

    while True:
        choice = input('추가입력 여부(Y/N): ')
        if choice == 'Y' or choice == 'y':
            f_name, f_amount, f_calorie = input_food()
            foods.append({"name":f_name, "amount":f_amount, "calorie":f_calorie})
        elif choice == 'N' or choice == 'n':
            food_data.append({"date": today, "type":f_type, "time":f_time, "food": foods})
            save_data('diary_food.txt', food_data)
            print('식단을 저장했습니다!')
            break
        else:
            print("잘못된 값 입력")

#(완료)2주차-운동기록 함수 구현 
def workout_record():
    workout_data = []
    print('<운동을 기록해보자>')
    w_name, w_starttime, w_endtime, w_condition = input_workout()
    workout_data.append({"date":today, "name":w_name, "starttime":w_starttime, "endtime":w_endtime, "condition":w_condition})
    while True:
        choice = input('추가입력 여부(Y/N): ')
        if choice == 'Y' or choice == 'y':
            w_name, w_starttime, w_endtime, w_condition = input_workout()
            workout_data.append({"date":today, "name":w_name, "starttime":w_starttime, "endtime":w_endtime, "condition":w_condition})
        elif choice == 'N' or choice == 'n':
            save_data('diary_workout.txt', workout_data)
            print('운동을 저장했습니다!')
            break
        else:
            print("잘못된 값 입력")

#(완료)3주차-휴식기록 함수 구현 
def rest_record():
    rest_data = []
    print('<휴식을 기록해보자>')
    r_name, r_starttime, r_endtime, r_condition = input_rest()
    rest_data.append({"date":today, "name":r_name, "starttime":r_starttime, "endtime":r_endtime, "condition":r_condition})
    while True:
        choice = input('추가입력 여부(Y/N): ')
        if choice == 'Y' or choice == 'y':
            r_name, r_starttime, r_endtime, r_condition = input_rest()
            rest_data.append({"date":today, "name":r_name, "starttime":r_starttime, "endtime":r_endtime, "condition":r_condition})
        elif choice == 'N' or choice == 'n':
            save_data('diary_rest.txt', rest_data)
            print('휴식을 저장했습니다!')
            break
        else:
            print("잘못된 값 입력")

#(완료)3주차-수면기록 함수 구현
def sleep_record():
    sleep_data = []
    print('<수면을 기록해보자>')
    s_starttime, s_endtime, s_condition = input_sleep()
    sleep_data.append({"date":today, "starttime":s_starttime, "endtime":s_endtime, "condition":s_condition})
    while True:
        choice = input('추가입력 여부(Y/N): ')
        if choice == 'Y' or choice == 'y':
            s_starttime, s_endtime, s_condition = input_sleep()
            sleep_data.append({"date":today, "starttime":s_starttime, "endtime":s_endtime, "condition":s_condition})
        elif choice == 'N' or choice == 'n':
            save_data('diary_sleep.txt', sleep_data)
            print('수면을 저장했습니다!')
            break
        else:
            print("잘못된 값 입력")

#(예정)4주차-보고서 생성 함수 구현
def create_report(): 
    report_start = (datetime.today()+timedelta(days=-7)).strftime("%m/%d")
    report_end = datetime.today().strftime("%m/%d")
    print('<최근 일주일('+report_start+'~'+report_end+') 요약 보고서>')
    food_list = read_data('diary_food.txt')
    workout_list = read_data('diary_workout.txt')
    rest_list = read_data('diary_rest.txt')
    sleep_list = read_data('diary_sleep.txt')
    b_cal_avg, b_time_avg = get_food_avg(food_list, 1)
    l_cal_avg, l_time_avg = get_food_avg(food_list, 2)
    d_cal_avg, d_time_avg = get_food_avg(food_list, 3)
    s_cal_avg, s_time_avg = get_food_avg(food_list, 4)
    ws_time_avg, we_time_avg, w_cond_avg = get_list_avg(workout_list)
    rs_time_avg, re_time_avg, r_cond_avg = get_list_avg(rest_list)
    ss_time_avg, se_time_avg, s_cond_avg = get_list_avg(sleep_list)
    print('아침: 평균 '+b_cal_avg+'kcal 섭취 / 평균 식사 시간 '+b_time_avg)
    print('점심: 평균 '+l_cal_avg+'kcal 섭취 / 평균 식사 시간 '+l_time_avg)
    print('저녁: 평균 '+d_cal_avg+'kcal 섭취 / 평균 식사 시간 '+d_time_avg)
    print('간식: 평균 '+s_cal_avg+'kcal 섭취 / 평균 식사 시간 '+s_time_avg)
    print('운동: 평균 시작 '+ws_time_avg+' / 평균 종료 '+we_time_avg+' / 컨디션 평균 '+w_cond_avg)
    print('휴식: 평균 시작 '+rs_time_avg+' / 평균 종료 '+re_time_avg+' / 컨디션 평균 '+r_cond_avg)
    print('수면: 평균 시작 '+ss_time_avg+' / 평균 종료 '+se_time_avg+' /  컨디션 평균 '+s_cond_avg)

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
            print("잘못된 값 입력")
        print()

def get_food_avg(list, type):   
    type_len = 0
    sec_sum = 0
    cal_sum = 0
    for item in list:
        if item['type'] == str(type):
            type_len += 1
            hh = int(item['time'].split(':')[0])
            mm = int(item['time'].split(':')[1])
            sec_sum += hh*60*60 + mm*60
            for food in item['food']:
                cal_sum += int(food['calorie'])

    if type_len > 0:
        sec_avg = sec_sum/type_len/60
        time_avg = str(math.floor(sec_avg/60)).zfill(2)+':'+str(math.floor(sec_avg%60)).zfill(2)
        cal_avg = str(math.floor(cal_sum/type_len))
        return cal_avg, time_avg
    else:
        return '0', '-'

def get_list_avg(list):   
    list_len = len(list)
    cond_sum = 0
    start_sec_sum = 0
    end_sec_sum = 0
    for item in list:
        s_hh = int(item['starttime'].split(':')[0])
        s_mm = int(item['starttime'].split(':')[1])
        e_hh = int(item['endtime'].split(':')[0])
        e_mm = int(item['endtime'].split(':')[1])
        start_sec_sum += s_hh*60*60 + s_mm*60
        end_sec_sum += e_hh*60*60 + e_mm*60
        cond_sum += int(item['condition'])

    start_sec_avg = start_sec_sum/list_len/60
    end_sec_avg = end_sec_sum/list_len/60
    start_time_avg = str(math.floor(start_sec_avg/60)).zfill(2)+':'+str(math.floor(start_sec_avg%60)).zfill(2)
    end_time_avg = str(math.floor(end_sec_avg/60)).zfill(2)+':'+str(math.floor(end_sec_avg%60)).zfill(2)
    cond_avg = str(math.floor(cond_sum/list_len))

    return start_time_avg, end_time_avg, cond_avg

#메인 함수 실행
if __name__ == '__main__':
    main()

#(예정)5주차-README.md 파일에 프로그램 설명 작성