import os
import datetime

base_dir = 'C:\\iotest'
os.chdir(base_dir)


try:
    f = open("sample.txt", "rt", encoding= "UTF-8")
    new = open("sample_yyyy_mm_dd.txt", "at", encoding="UTF-8")
    rows = f.readlines()
    for row in rows:
        new.write(row)
    new.write("\n\n")
    f.close()
    new.close()
    print("저장이 완료되었습니다.")

except FileNotFoundError:
    print("파일이 없습니다. 다시 확인해주세요.")