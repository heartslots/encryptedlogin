import math

sev = {}

def ascii(a):
    return ord(a)

def hashing(string):
    b = list(map(ascii, string))
    hashed = int(sum(b))
    logged = math.trunc(math.log10(hashed) * 10000000)

    while logged >= 100000000:
        logged = math.trunc(logged/10)

    return logged

def mainmenu():
    while True:
        inp = input()
        if inp == "/login":
            login()
            break
        elif inp == "/register":
            register()
            break
        elif inp == "/server":
            server()
            break
        elif inp == "/end":
            exit()
        else:
            print("다시 입력해주세요.")

def main():
    print("로그인, 회원가입시스템\n/login : 로그인\n/register : 회원가입\n/server : 서버에 저장된 값 보기\n/end : 끝내기")
    mainmenu()

def login():
    while True:
        logid = input("id를 입력하세요 : ")
        password = input("비밀번호를 입력하세요 : ")
        newpass = hashing(password)
        if sev[logid] == newpass:
            i = input("로그인 성공")
            main()
            break
        else:
            print("다시 입력해주세요")

def register():
    while True:
        logid = input("id를 입력하세요 : ")
        password = input("비밀번호를 입력하세요 : ")
        newpass = hashing(password)
        sev[logid] = newpass
        print("완료되었습니다")
        main()
        break

def server():
    for key, value in sev.items():
        print(key, value)
    main()

main()
