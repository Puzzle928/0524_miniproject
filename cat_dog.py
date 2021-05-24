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
    print("당신은 강아지형 인간? 고양이형 인간?.")

    cat = 0
    dog = 0
    time.sleep(1) #화면 잠시 멈춤 sleep()는 잠시동안 멈춤을 유지
    clear()
    print("친구들과 다같이 식당에 간 당신. 직원이 다가와 주문을 할거냐 묻는다. 당신의 행동은??")
    print("1.친구들이 주문하는 내용을 듣고 주문한다")
    print("2.누구 보다 빠르게, 가장 먼저 주문한다")
    q1 = int(input("번호를 입력해주세요:")) # int 정수값으로 변환

    if q1 == 1: # 1번을 선택할 경우  a에 1이 추가가 되어 나중에 a 와 b 값의 경우의수로 다른 결과값을 출력하기 위한 축적
        dog += 1
    if q1 == 2:
        cat += 1
    else:
        print("다시입력하세요")

    clear()
    print("따스한 봄날을 즐기며 한가롭게 거리를 거닐던 당신. 저 멀리서 싫어하는 선배(직장 상사)가 다가오는 것을 보았다. 상대방은 아직 당신을 알아차리지 못했다. 어떻게 할까?")
    print("1.상대방과 마주하면 대놓고 불쾌감을 표출한다")
    print("2.다른 길로 도망친다")
    print("3.상대방이 알아차리면 인사하고, 아니면 무시한다")
    print("3.태연하게 인사한다")
    q2 = int(input("번호를 입력해주세요:"))

    if q2 == 1:
        dog += 1
    if q2 == 2:
        dog += 1
    if q2 == 3:
        cat += 1
    if q2 == 4:
        cat += 1
    clear()
    print("당신이 선호하는 직장의 모습은?")
    print("1.인간관계가 온화하고 친근한 분위기의 직장")
    print("2.전문성을 쌓을 수 있는 직장")
    print("3.여러가지 일을 해볼 수 있는 직장")
    print("4.공과 사가 철저한 직장")
    q3 = int(input("번호를 입력해주세요:"))

    if q3 == 1:
        dog += 1
    if q3 == 2:
        cat += 1
    if q3 == 3:
        dog += 1
    if q3 == 4:
        cat += 1

    clear()
    print("배가 고프다. 다음 메뉴 중 어떤 것을 먹을까?")
    print("1.깔끔한 초밥")
    print("2.국민점심 제육덮밥")
    print("3.뜨근한 국밥한뚝배기")
    print("4.간단한 면요리")
    q4 = int(input("번호를 입력해주세요:"))


    if q4 == 1:
        cat += 1
    if q4 == 2:
        dog += 1
    if q4 == 3:
        dog += 1
    if q4 == 4:
        cat += 1
    clear()
    print("간만의 휴일을 맞이한 당신, 당신이 빌려보고 싶은 비디오(DVD) 영화장르는?")
    print("1.로맨틱, 코미디 ,멜로")
    print("2.스릴러, 공포 ,액션물")
    print("3.에로, 성인물")
    print("4.빌려보기 귀찮다")    
    q5 = int(input("번호를 입력해주세요:"))

    if q5 == 1:
        cat += 1
    if q5 == 2:
        dog += 1
    if q5 == 3:
        dog += 1
    if q5 == 4:
        cat += 1
    clear()
    print("미로를 헤매이던 당신. 그러던 중 계단과 마주했다. 다음 중 당신이 택할 계단은?")
    print("1.오르막계단")
    print("2.내리막계단")
    q6 = int(input("번호를 입력해주세요:"))

    if q6 == 1:
        dog += 1
    if q5 == 2:
        cat += 1

    print("결과는")
    clear()
    script_dir = os.path.dirname(os.path.abspath(__file__))


    if cat > dog:
        print("당신은 고양이과")
        image = Image.open(os.path.join(script_dir, 'b1.jpg'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'b2.jpg'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'b3.jpg'))
        plt.imshow(image)
        plt.show()
    elif dog > cat:
        print("당신은 강아지과")
        image = Image.open(os.path.join(script_dir, 'a1.jpg'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'a2.jpg'))
        plt.imshow(image)
        plt.show()
        image = Image.open(os.path.join(script_dir, 'a3.jpg'))
        plt.imshow(image)
        plt.show()        
    else:
        print("당신은 반반")
        image = Image.open(os.path.join(script_dir, 'C.jpg'))
        plt.imshow(image)
        plt.show()
    n = int(input("종료하려면 1을 입력, 다시시작하려면 아무숫자나 입력하시오"))
    if n == 1:
        break