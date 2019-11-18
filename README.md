# 2019-2-OSSP1-3355-3
2019년 2학기 공개SW프로젝트 3조 삼삼오오

## 프로젝트 주제  
딥러닝 기반 운동 자세 교정 프로그램 - HomePT

## 프로젝트 설명  
수많은 dataset의 keypoint detection을 인식하여 딥러닝을 기반으로 운동 자세를 교정해주는 홈트레이닝 운동 자세 교정 프로그램입니다.

## 프로그램 메인 로고
![logo](https://user-images.githubusercontent.com/55729131/67072681-6b6f9380-f1c0-11e9-8609-adc2d611cdc5.png)

## 사용법
### 1) cmd창에서 폴더에 들어간 뒤 pyinstaller -w -F realMain.py 명령어를 입력한다.
### 2) 생성된 dist 폴더 내의 realMain.exe 파일을 실행한다.
### 3) 원하는 운동을 선택한다.
### 4) 해당 운동 동영상 파일을 불러온다.
### 5) 분석된 결과를 보고 올바른 자세를 파악한다.

## 팀원  
오유민, 배진우, 유성근, 신승윤  

## TODO
- [x] keypoint detection - proto
- infer time : 1.3 (hourglass stack 2)
- [x] PyQt GUI proto
  - [x] Make Logo
  - [x] put image in GUI
  - [x] button event
- [ ] keypoint detection - more accurate ver
- [x] PyQt GUI
- [ ] person detection
- [ ] pose estimation (LSTM)


