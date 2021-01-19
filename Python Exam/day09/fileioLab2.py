import os
import shutil
import datetime

base_dir = 'C:\\iotest'
os.chdir(base_dir)

try:
    if os.path.exists("sample.txt"):
        if os.path.exists("sample_yyyy_mm_dd.txt"):
            shutil.copy("sample.txt", "sample_{0}_{1}_{2}.txt".format(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day))

        else:
            f = open("today.txt", "w", encoding="UTF-8")
            shutil.copy("sample.txt", "sample_yyyy_mm_dd.txt")
            f.close()


except FileNotFoundError:
    print("파일이 없습니다.")

