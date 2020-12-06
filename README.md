--HealthDiary
-- 프로젝트명: '나만의 건강 다이어리'
-- 프로젝트 기간: 2020/11/01 ~ 2020/12/06
-- 프로젝트 개발자: 융합보안학과 2020113156 주현지

(완료)1주차-데이터 저장 포맷 설계
1. 식단기록 저장 포맷
- 파일명: food_diary.txt
- 저장예시:
{
    "date": "20201101",
    "type": "아침",
    "time": "1030",
    "food":{
        {"name": "닭가슴살", "amount": "100", "calorie": "120"},
        {"name": "블루베리", "amount": "50", "calorie": "80"},
        {"name": "치즈", "amount": "40", "calorie": "60"}
    }
}

2. 운동기록 저장 포맷
- 파일명: workout_diary.txt
- 저장예시:
{
    "date": "20201101",
    "startTime": "1930",
    "endTime": "2030",
    "name": "필라테스",
    "condition": "7"
}

3. 휴식기록 저장 포맷
- 파일명: rest_diary.txt
- 저장예시:
{
    "date": "20201101",
    "startTime": "1500",
    "endTime": "1520",
    "name": "음악감상",
    "condition": "5"
}

4. 수면기록 저장 포맷
- 파일명: sleep_diary.txt
- 저장예시:
{
    "date": "20201102",
    "startTime": "2230",
    "endTime": "0800",
    "condition": "10"
}

5. 보고서 저장 포맷
- 파일명: report_mmdd~mmdd.txt
{
    "startDate": "20201101",
    "endDate": "20201107",
    "food_report": 
    {
        {"type": "1", "timeAvg": "1020", "calorieAvg": "350"},
        {"type": "2", "timeAvg": "1400", "calorieAvg": "520"},
        {"type": "3", "timeAvg": "1830", "calorieAvg": "660"}
    },
    "workout_report": {"timeAvg": "35", "conditionAvg": "5"}
    "rest_report": {"timeAvg": "15", "conditionAvg": "8"}
}

(완료)5주차-프로그램 설명 작성

1. 프로그램 소개
    - '나만의 건강 다이어리'는 개인이 꾸준히 식단, 운동, 수면, 휴식을 기록한 후 보고서 형태로 열람하여 건강을 관리할 수 있도록 돕기 위한 프로그램이다.
    - 프로그램 실행 후 기록한 정보는 파일에 저장되어 종료 시에도 삭제되지 않고 다음날 재실행하여 기록하면 파일에 추가되어 저장된다.
    - 보고서는 기본적으로 최근 일주일 간의 기록을 취합하여 제공한다.

2. 다이어리 기록 방법
    0) 프로그램 실행 후 식단, 운동, 휴식, 수면 기록 중 한 가지를  1~4 사이의 번호로 선택한다. (전체 프로그램은 선택지에 없는 값이나, 형식에 맞지 않는 잘못된 값을 입력한 경우 오류메시지를 출력하며 재입력을 받도록 구현되어 있다.)

    1) 식단기록 선택 시
    - ① 아침, 점심, 저녁, 간식 중 한 가지를 1~4 사이의 번호로 선택한다.
    - ② 식사 시간을 '시:분' 형태로 입력한다. (예: 10:30, 19:40 등)
    - ③ 식품명을 자유롭게 입력한다.
    - ④ 섭취량을 g 단위의 숫자로만 입력한다.
    - ⑤ 섭취한 음식의 칼로리를 숫자로만 입력한다.
    - ⑥ 추가입력 여부를 Y/N (소문자 가능)으로 선택한다. Y 선택 시 ③~⑤ 과정을 반복한다. N 선택 시 식단기록이 종료된다.

    2) 운동기록 선택 시
    - ① 운동명을 자유롭게 입력한다.
    - ② 시작시간, 종료시간을 '시:분" 형태로 입력한다.
    - ③ 운동 후 컨디션을 최소 1 ~ 최대 10 사이의 값으로 입력한다.
    - ④ 추가입력 여부를 Y/N (소문자 가능)으로 선택한다. Y 선택 시 ②~③ 과정을 반복한다. N 선택 시 운동기록이 종료된다.

    3) 휴식기록, 수면기록도 2) 운동기록과 동일한 형태로 다이어리에 기록한다.

3. 보고서 확인 방법
    1) 메인화면에서 '5. 보고서 확인'을 클릭하면 최근 일주일 간의 기록을 바탕으로 보고서를 자동으로 생성해준다.
    2) 각 보고서 항목 및 노출 데이터는 아래와 같다.
        - 아침, 점심, 저녁, 간식: 기록하지 않은 날을 제외하고 평균 칼로리 및 식사시간을 계산하여 노출
        - 운동, 휴식, 수면: 기록하지 않은 날을 제외하고 평균 시작시간, 종료시간 및 평균 컨디션을 계산하여 노출

4. 느낀 점
    5주 동안의 파이썬 프로그램 제작을 마치는 내 감정은 뿌듯함으로 가득하다.
    파이썬을 학습하고 프로그래밍 하는 것이 처음이다보니 어려움이 컸지만 점점 완성되는 모습에 재미도 많이 느꼈다. 수업 시간에 학습한 소스를 많이 참고하였는데 문제 풀이를 할 때는 잘 실행이 되다가 내 프로그램에 맞게 고치고 나서는 오류가 나는 경우가 많았다. 그래서 인터넷에서 찾아보고 수정하며 애를 먹었는데 역시 다른 소스를 이해하고 사용하는 것이 쉽지 않은 일이라는 것을 느꼈다.
    다이어리라는 프로그램 특성상 입력 받는 값이 많은데 잘못된 값을 입력하는 케이스에 대해서 초반에는 생각하지 못하고 있다가 내가 숫자를 입력받는 곳에 문자를 입력해서 오류가 나는 것을 보고 충격을 받아 모두 체크하게 되었다. 이런 부분은 정말 프로그램을 많이 실행해보고 경험해봐야 알 수 있는 것 같다.
    또한, 프로그램을 짜다 보니 점점 길어져 일부는 함수로 분리하여 구현했는데 함수명을 짓는 것도 고민이 필요하다는 걸 알게 되었고 알아보기 쉬운 변수명의 중요성도 느꼈다.
    그리고 계획서를 작성하며 시간 계산에 대한 나만의 알고리즘을 수학 공식을 통해 생각해서 작성했었는데 미리 고민을 해둔 결과가 프로그램으로 정확히 확인이 되니 무척 희열감이 느껴졌다.
    결과적으로 최초에 계획서를 쓰며 넣고자 했던 기능을 대부분 구현할 수 있어 뿌듯했으나, 좀 더 활용도 높은 프로그램이 되려면 보고서 기능을 고도화 시켜야할 것 같다는 생각이 든다.
    일주일 간 성실하게 입력한 값을 유의미하게 활용하기 위해서는 보고서에서 단순한 평균 값 계산 뿐만 아니라, 부족한 부분 안내 및 차주에 어떻게 관리하면 좋을지 권고하는 기능이 추가되면 좋을 것 같다.
    5주가 완벽한 프로그램을 만들기에는 짧은 시간이지만, 꾸준히 프로그램에 필요한 기술을 찾아보고 학습하고, vscode, github, sourcetree 등의 툴을 익히고 새로운 프로그램 제작에 대한 열정을 갖게 하는 데에는 충분한 기회의 시간이었던 것 같다. 추후 보고서 기능까지 업데이트 해보고 주변인들에게 소개하는 기회도 가지려고 한다.