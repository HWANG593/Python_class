class Book:
    store = "yes24"     # 클래스 변수
    def __init__(self,title,author,price):  # 멤버변수 title, author, price
        self.title = title          # 인스턴스 변수
        self.author = author        # 인스턴스 변수
        self.price = price          # 인스턴스 변수

    def getBookInfo(self):      # 매개변수는 없다.
        return ('책이름 : {0}\n저자 : {1}\n가격 : {2}'.format(self.title,self.author,self.price))



book1 = Book('파이썬 정복','김상형',19800)
book2 = Book('이것이 Maria DB다','우재남',27000)
book3 = Book('맛있는 MongoDB','정승호',25200)
book4 = Book('파이썬 웹 프로그래밍','김석훈',19800)
book5 = Book('생활코딩! HTML+ CSS+ 자바스크립트','이고잉',24300)


print(book1.getBookInfo())
print(book2.getBookInfo())
print(book3.getBookInfo())
print(book4.getBookInfo())
print(book5.getBookInfo())
