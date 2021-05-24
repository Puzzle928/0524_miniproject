import time
import os
import platform
import matplotlib.pyplot as plt
from PIL import Image


def clear(): #
    os_type = platform.system()
    if os_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


clear()
while True:
    print("무료 성격 유형 검사 입니다.")

    a = 0
    b = 0
    time.sleep(1)
    clear()
    print("조별 과제에 당신의 역활은?")
    print("1.자료 조사 및 정리")
    print("2.정리된 자료로 PPT 만들기 ( 발표 빼고")
    q1 = int(input("번호를 입력해주세요:"))

    if q1 == 1:
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