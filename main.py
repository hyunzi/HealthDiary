# Last Update Date: 2020/11/07

#(완료)1주차-데이터 저장 형식 json. 저장 포맷은 README.md에 상세기재
import json

#(완료)1주차-데이터 read 함수 구현
def read_data(file_name):
  data_list = []
  with open(file_name, encoding='utf-8') as json_file:
      data_list = json.load(json_file)
  return data_list

#(완료)1주차-메인화면(최초 접속 화면) 구현
def print_menu():
    print ('=============================')
    print ('    <나만의 건강 다이어리>    ')
    print ('=============================')
    print ('1. 식단기록     2. 운동기록')
    print ('3. 휴식기록     4. 수면기록')
    print ('5. 보고서 확인  6. 종료')
    print ('=============================')
    print ()

#(예정)2주차-식단기록 함수 구현
def food_record():
    print('<식단을 기록해보자>')

#(예정)2주차-운동기록 함수 구현 
def workout_record():
    print('<운동을 기록해보자>')

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