import time # 현재 시간을 가지고 오는 모듈
import os # 프로그램을 돌리는 컴퓨터의 운영체제를 검사할 수 있도록 하기위한  모듈
import platform # 현재 사용하고 시스템 유형을 알려주는 모듈
import matplotlib.pyplot as plt # 파이썬과 그림파일을 연결하여 원하는 이미지파일이 실행되게 하기위한 모듈
from PIL import Image # 파이썬과 그림파일을 연결하여 원하는 이미지파일이 실행되게 하기위한 모듈


def clear(): # window 에 경우는  cls 이지만 ios 맥을 사용하는 사람의 경우 clear 으로 명령어가 다르기때문에 def 로 정의하여 표현
    os_type = platform.system()
    if os_type == 'Windows': # 윈도우 일 경우
        os.system('cls') # window 시스템의 cls 기능 실행
    else:
        os.system('clear') #  아닐경우 ios운영체제일 경우 이므로 clear 기능 실행


clear() # 화면 클리어 하기
while True:
    print("무료 성격 유형 검사 입니다.")

    a = 0
    b = 0
    time.sleep(1) #화면 잠시 멈춤 sleep()는 잠시동안 멈춤을 유지
    clear()
    print("조별 과제에 당신의 역활은?")
    print("1.자료 조사 및 정리")
    print("2.정리된 자료로 PPT 만들기 ( 발표 빼고")
    q1 = int(input("번호를 입력해주세요:")) # int 정수값으로 변환

    if q1 == 1: # 1번을 선택할 경우  a에 1이 추가가 되어 나중에 a 와 b 값의 경우의수로 다른 결과값을 출력하기 위한 축적
        a += 1
    if q1 == 2:
        b += 1
    else:
        print("다시입력하세요")

    clear()
    print("이 중에서 운명적인 이끌림이 느껴지는 것은? 없다면 눈을 감고 찍어보세요!")
    print("1.흑백으로 이루어진 데이터베이스에서 원하는 정보만 쏙 뽑아내서 정리하기")
    print("2.컬러풀한 화면을 보며 사용자가 보기 좋고 편리하게 정보 배치하기")
    q2 = int(input("번호를 입력해주세요:"))

    if q2 == 1:
        a += 1
    if q2 == 2:
        b += 1
    clear()
    print("밴드에 들어가기로 했어요. (실력은 동일하다고 했을 때)")
    print("1.보컬 할래.")
    print("2.베이스기타 할래.")
    q3 = int(input("번호를 입력해주세요:"))

    if q3 == 1:
        a += 1
    if q3 == 2:
        b += 1

    clear()
    print("아이언맨 수트과 자비스 중 하나를 만들 수 있다면?")
    print("1.자비스")
    print("2.아이언맨 수트")
    q4 = int(input("번호를 입력해주세요:"))


    if q4 == 1:
        a += 1
    if q4 == 2:
        b += 1
    clear()
    print("이성규님의 생일은?")
    print("1.6월 23일")
    print("2.몰라요 ㅎ")
    q5 = int(input("번호를 입력해주세요:"))
    clear()
    print("이성규님의 계좌는?")
    print("1.케이뱅크 100-163-780056")
    print("2.몰라요 ㅎ")
    q6 = int(input("번호를 입력해주세요:"))

    print("결과는")
    clear()
    script_dir = os.path.dirname(os.path.abspath(__file__))


    if a > b:
        print("백엔드")
        image = Image.open(os.path.join(script_dir, 'a.jpg'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'a1.jpg'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'a2.jpg'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'a3.jpg'))
        plt.imshow(image)
        plt.show()
    elif b > a:
        print("프론트앤드")
        image = Image.open(os.path.join(script_dir, 'b.png'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'b2.png'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'b3.png'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'b4.png'))
        plt.imshow(image)
        plt.show()
    else:
        print("풀스택")
        image = Image.open(os.path.join(script_dir, 'C.png'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'C1.png'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'C2.png'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'C3.png'))
        plt.imshow(image)
        plt.show()
    n = int(input("종료하려면 1을 입력, 다시시작하려면 아무숫자나 입력하시오"))
    if n == 0:
        break