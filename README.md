** HealthDiary
** 프로젝트명: '나만의 건강 다이어리'
** 프로젝트 기간: 2020/11/01 ~ 2020/12/05
** 프로젝트 개발자: 융합보안학과 2020113156 주현지

** (완료)1주차-데이터 저장 포맷 설계
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

* (예정)5주차-프로그램 설명 작성