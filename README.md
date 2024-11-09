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
- RandomForestRegressor로 다시 바꿈
- 셔틀 마지막차는 거의 고정으로 오니까 FIXED로 해서 FIXED = false인 데이터에 한해서 수정하기로 함 (gStation3)
- 최대한 꼼꼼히 전처리 함
- V4-1은 FIXED = true를 빨리 제외했더니 데이터중 정확하게 온 버스를 건너뛰고 이상한 곳에 매칭이 되어서 오차가 커짐
- V4-2에서 FIXED = true는 나중에 빼는걸로 수정함
- 예측값 파일 나름 만족스러움
- 근데 R2 Score너무 낮게 나옴
- ? 왜 ?
