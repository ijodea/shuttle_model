# shuttle_model

지금 방식 → 때려맞추기 csv를 사용중

메인 페이지에 “지금 탔어요” 버튼을 만들어서

이 버튼 누르면 그 시간들을 데이터 수집

이거가지고 머신러닝 돌리기 → 새로운 csv 나옴

이걸 주기적으로 업데이트해주기

주의사항:

- 비정상적인 데이터 걸러야함(ex 밤 11시 데이터)


## V1
- RandomForestRegressor 사용
- gStation2 데이터는 gStation데이터를 월화수목금으로 펼침
- STATION_DEPART 값이 모두 같은 값이 됐음;;

## V2
- RandomForestRegrssor 사용
- 그럴싸한 데이터가 나왔지만 08:00 -> 08:15 -> 08:30은 2대가 운행되는데 한대라거나 잘 안됐음

## V3
- XGboost 사용
- SCHOOL_DEPART 07:45, STATION_DEPART 10:49 -> 이렇게 2시간걸리는 말도안되는 시간표

## V4

