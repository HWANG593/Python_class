import os

try:
    base_dir = 'C:\\iotest'
    os.chdir(base_dir)
    if os.path.exists("today.txt") :
        f = open("today.txt", "wt", encoding="UTF-8")
        f.write("""오늘은 2021년 01월 18일입니다.\n오늘은 월요일입니다.\n나는 목요일에 태어났습니다.""")
    else:
        f = open("today.txt", "w", encoding="UTF-8")
        f.write("""오늘은 2021년 01월 18일입니다.\n오늘은 월요일입니다.\n나는 목요일에 태어났습니다.""")

finally:
    f.close()
    print('저장이 완료되었습니다.')
