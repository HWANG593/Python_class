import os

base_dir = 'C:\\iotest'
os.chdir(base_dir)

try:
    if os.path.exists("yersterday.txt"):
        f = open("yesterday.txt", "rt", encoding="UTF-8")
        rows = f.readlines()  # 모든 행을 읽어서 리스트로 리턴
        lyrics = " ".join(rows)
        lyrics_small = lyrics.lower()
        count = lyrics_small.count('yesterday')
        f.close()
except  FileNotFoundError:
    print('파일을 읽을 수 없어요')
else:
    print("Number of a word 'Yesterday'", count)
finally:
    print("수행완료!!")