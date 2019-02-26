# -*- coding: utf-8 -*-

a = " Hello EveryBody "

# isalpha: 오직 문자인지 체크
txt1 = "helloWorld"
print(txt1.isalpha())

# isdigit: 숫자인지 체크
# num1 = 123
# print(num1.isidigit())

# isalnum: 알파벳 혹은 숫자 체크
txt2 = "안녕"
print(txt2.isalnum())

# upper: 모두 대문자로
print(a.upper())

# lower: 소문자로
print(a.lower())

# strip: 좌우 공백제거
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# count: 해당 문자 개수 세기
print(a.count("e"))
print(a.count("Hello"))

a = " Hello EveryBody "

# find: 해당 문자 인덱스
print(a.find("H"))
print(a.find("E"))
print(a.find("v"))      # return -1 if no match found
print(a.find("y", 10))  # Finds the letter after 10th index

# split: 문자열 분리
# url = "http://naver.com"
# logs = "name:홍길동, age:17, gender:남, nation:조선"
# print(url.split(":"))
# print(log.split()) # split by space
# for each in log.split(","):
#     a,b = each.split(":")
#     print("%s -> %s" %(a.strip(), b.strip()))

# join: 문자열을 요소로 가지는 리스트의 요소들을 특정 문자를 기준으로 결합
a = ["hello", "world", "good", "bye", "baby"]
print(";".join(a))


# replace: 문자열 내 특정 문자(열)를 찾아 다른 문자로 변경
a = " Hello EveryBody "
print(a.replace("Hello", "Good bye").strip())

# encode: 문자를 바이트 객체로 바꾸기
u = "I love python"
l = u.encode()  # default : utf-8
print(u)    # unicode
print(l)    # byte (UTF8 encoded)
print(l[0])
ret1 = u[0] == "I"  # ret1 = "I"
ret2 = l[0] == "I"  # ret2 = 73 (바이트라서)
print(ret1)
print(ret2)

# decode: 바이트 객체를 문자로 바꾸기
u = "I love python"
l = u.encode("utf-8")
print(l)
print(l.decode("utf-8"))
print(list(range(10)))

# sorted : 사전 정렬하기
names = {"Mary":10999, "Sams":2111, "Amy":9778, "Tom":20245, "Michael":27115, "Bob": 5687, "Kelly":7885}
ret1 = sorted(names)    # key를 기준으로, 오름차순 정렬
print(ret1)
ret2 = sorted(names.items(), key= lambda x: x[0])   # key의 인자는 반드시 함수이어야 한다. 정렬할 값이 key에 정의 된 함수의 파라미터로 전달된다.
print(ret2)     # [('Amy', 9778), ('Bob', 5687), ('Kelly', 7885), ('Mary', 10999), ('Michael', 27115), ('Sams', 2111), ('Tom', 20245)]
ret3 = sorted(names.items(), key= lambda x: x[1])
print(ret3)     # [('Sams', 2111), ('Bob', 5687), ('Kelly', 7885), ('Amy', 9778), ('Mary', 10999), ('Tom', 20245), ('Michael', 27115)]
ret4 = sorted(names.items(), key= lambda x: x[1], reverse=True)
print(ret4)     # [('Michael', 27115), ('Tom', 20245), ('Mary', 10999), ('Amy', 9778), ('Kelly', 7885), ('Bob', 5687), ('Sams', 2111)]

# ord : 문자 코드값 구하기
ch = "김"
chv = ord(ch)
print("String: %s \t Code Value:%d \t Hexa Code: %s" %(ch, chv, hex(chv)))

# chr : 코드값으로 문자 구하기
u = "I love python"
l = u.encode()  # default : utf-8
print(ord(u[0])) # l[0]과 같다
for i in l:
    print(i, chr(i))

# String->Code / Code->String 정리
# ord: 문자로 코드값 구하기 / encode: 문자를 바이트 객체로 바꾸기
# chr: 코드값으로 문자 구하기 / decode: 바이트 객체를 문자로 바꾸기

# eval : 문자열로 된 식을 실행하기
expr1 = "2+3"
expr2 = "round(3.7)"
ret1 = eval(expr1)
ret2 = eval(expr2)
print("%s를 eval()로 실행한 결과: %d" %(expr1, ret1))

# map : iteratable한 자료를 돌며 결과값 구하기
li = (1,2,3,4,5)
ki = [" 이것은 아무 문자열이지롱 ", "스트립으로 공백을 없애보자  ", "  그냥하면 재미 없으니 람다 map을 쓰자"]
ret1 = [1,2,3,4,5]
ret2 = [5,6,7,8,9]
after_li = list(map(lambda x: x**2, li))
after_ki = list(map(lambda x: x.strip(), ki))
after_ci = list(map(lambda x,y : x+y, ret1, ret2))
print(after_li)
print(after_ki)
print(after_ci)


# read: 파일을 열고 읽음
with open("stockcode.txt", "r") as f:
    data = f.read()
    print(data)

# readline: 텍스트파일 한줄씩 읽고 출력, 파일이 클 경우 한번에 read하면 메모리 문제가 있을 수 있음
f = open("stockcode.txt", "r")
line = f.readline()
while line:
    print("%s" %(line), end="")
    line = f.readline()
f.close()

# readlines: 텍스트 파일을 한 줄씩 다 읽고 각 줄을 요소로하는 리스트를 리턴
# print("")
# f = open("stockcode.txt", "r")
# lines = f.readlines()
# for line_num, line in enumerate(lines):
#     print("%d %s" %(line_num, line), end="")

# read, write: 바이너리 파일 복사/쓰기
bufsize = 1024 # byte 즉, 1kb임
s = open("main_landing.jpg", "rb")
k = open("main_landing_copy.jpg", "wb")
data = s.read(bufsize)
while data:
    k.write(data)
    data = s.read(bufsize)  # 기존에 bufsize 읽은만큼은 없어지게 되므로 무한루프가 아니다.
s.close()
k.close()

# seek : 해당위치(byte)부터 파일을 읽어들임, 원래는 open()으로 열면 파일 맨 처음부터 읽음.
# s = open("stockcode.txt", "r")
# h = open("stockcode_cop.txt", "w")
# s.seek(500)
# data = s.read(300)
# h.write(data)
# s.close()
# h.close()

# os Module

# os.path.getsize: 파일의 크기
from os.path import getsize
file1 = "stockcode.txt"
file1_size = getsize(file1)
print(file1, file1_size)

# os.remove: 파일 삭제
from os import remove
target_file = "main_landing_copy.jpg"
remove(target_file)

# os.rename : 파일명을 바꾸거나 다른 디렉토리로 옮기기
# from os import rename, getcwd
# new_name = getcwd() + "/stockcode.txt"
# rename("stockcode.txt", new_name)   # 파일명, 경로+새로만들파일명

# os.listdir, glob.glob: 디렉토리에 있는 파일 목록 얻기
import os, glob
folder = os.getcwd()
file_list = os.listdir(folder)
print(file_list)

files = "*.*" # wildcard를 사용할 수 있어 확장자로 파일을 구분할 수 있다.
file_list = glob.glob(files)
print(file_list)

# os.chdir: 작업 디렉토리 변경하기
# os.rmdir : 디렉토리 삭제하기
# os.mkdir : 디렉토리 생성하기 (빈 디렉토리만 삭제할 수 있음)

# os.path.exists: 파일이나 디렉토리가 존재하는지 확인하기
# shutil.rmtree : 하위 디렉토리 및 파일 전체 삭제하기
# from os.path import exists
# import shutil
# if not exists("test-folder"):
#     os.mkdir(os.getcwd() + "/test-folder")

# nd = os.getcwd()+"/test-folder"
# nf = nd + "/helloworld.txt"; print(nf)
# with open(nf, "w") as f:
#     f.write("Hello world")
# target_folder = os.getcwd()+"/test-folder"; print(target_folder)
# print("file list -----------")
# for file in os.listdir(target_folder):
#     print(file)
# print("---------------------")
# q = input("위의 모든 디렉토리와 파일을 삭제할까? (y/n)")
# if q == "y":
#     try:
#         shutil.rmtree(target_folder)
#         print("모두삭제완료!")
#     except Exception as e:
#         print(e)
# print(after_ci)
# # index : List 내 찾는 값의 Index, Index값으로 리스트 내 값 바꾸기
# solarsys = ["a","b","c"]
# t = "a"
# i = solarsys.index(t)
# solarsys[i] = "kk"

# reverse : List의 값을 역순으로 정렬함. 원본 리스트를 바꿈. Call by Refer
# print(solarsys.reverse())

# reversed : 인자로 받는 List를 역순으로 정렬하지만 원본값을 바꾸지 않음 call by val
# t = list(reversed(solarsys))
# print(solarsys)
# print(solarsys[::-1]) # reversed와 같음
# print(t)

# sort = 원본 리스트값을 정렬 (list.sort())
# sorted = 새롭게 정렬 된 리스트를 리턴 (sorted(list))
# reverse = 원본 리스트값을 역정렬 (list.reverse())
# reveresed = 새롭게 역정렬 된 리스트를 리턴 (reversed(list))

# insert : append와 비슷하지만, 삽입할 위치(인덱스)를 지정할 수 있음.
li = ["Hello", "World", "Nice", "Meeting", "You"]
ind = li.index("Nice")
print(ind)  # 2
li.insert(ind, "Pleasure")  # Nice의 위치(2)에 Pleasure가 삽입 됨.
print(li)

# del list[index], list.remove("sth") : list내 값을 인덱스를 통하여 혹은 값 자체로 지움
k = lambda x, y : y.remove(x)
print(k("Hello", li))
print(li)

# del : 요소를 지움. 리스트 뿐만 아니라 다른 것도 포함
t = {"hello":"world", "Nice":"ToMeet"}
del t["hello"]
print(t)

# shuffle : list내 요소를 무작위로 섞기, call by refer
from random import shuffle
li = ["Hello", "World", "Nice", "Meeting", "You"]
shuffle(li)
print(li)

# enumerate : 리스트 요소와 인덱스를 쌍으로 추출
li = ["Hello", "World", "Nice", "Meeting", "You"]
for index, content in enumerate(li):
    print("인덱스 %s의 컨텐츠는 %s" %(index, content))

# all, any : 리스트 내의 모든 요소가 True인지 False인지 체크

# enumerate : 리스트 두개를 dictionary화
ko = ["엑서핏", "QR코드", "실버", "책"]
en = ["xcerfit", "qrcode", "silver", "book"]
new_dict = {}
for i, c in enumerate(ko):
    new_dict[c] = en[i]
print(new_dict)

# os.path.isfile, os.path.isdir : 파일인지 디렉터리인지 확인
import os
from os.path import exists, isdir, isfile

# wd = os.getcwd()
# if not exists(os.getcwd()+"/test"):
#     os.mkdir(os.getcwd()+"/test")
# nd = os.getcwd()+"/test"
# os.chdir(nd)
# os.mkdir("newdir")
# with open("helloworld.txt", "w") as f:
#     f.write("Hello world\n This is a new file")
# print(isfile(nd+"/helloworld.txt"))
# print(isdir(nd+"/newdir"))

# localtime, strftime : 현재 시간을 연월일 시분초로 출력하기
from time import localtime, strftime
#
# log = ""
# logfile = "new_test.log"
# def writelog(logfile, log):
#     time_stamp = strftime("%Y-%m-%d %X\t", localtime())
#     log = time_stamp + log + "\n"
#     with open(logfile, "a") as f:
#         f.writelines(log)
# writelog(logfile, "첫 문장입니다")

# 12/09/18 19:56:41 로 출력
print(strftime("%x %X", localtime()))

# 연, 월, 일, 시, 분, 초, 요일은 localtime의 n번째 변수
print(localtime()[0])   # 연
print(localtime()[1])   # 월
print(localtime()[2])   # 일

# id : 변수가 가리키는 메모리 주소를 나타냄
my_var = 10
my_var2 = 20
print(hex(id(my_var)))
print(hex(id(my_var2)))


class Rectangle:

# Property를 굳이 주는 이유는 값이 set 될 때 제약조건을 줄 수 있기 때문.
# 만약 제약조건이 필요 없는 부분이라면

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width Must be positive")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Width Must be positive")
        else:
            self.height = height

    def __str__(self):
        # here self.width calls width method
        return "Rectangle : width={}, height={}".format(self.width, self.height)

    def __repr__(self):
        return "RECTANGLE width {} / height {}".format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

# Reference Count
import sys, ctypes

def ref_count(address: int):
    # low-level에서 제공하는 ref counter
    return ctypes.c_long.from_address(address).value
a = [1,2,3]
print(sys.getrefcount(a)) # 메소드를 호출하는 시점에 또 참조를 하니까 참조수가 2
print(ref_count(id(a)))
a_id = id(a)
a = None
print(ref_count(a_id))

# GC
import ctypes
import gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "NOT FOUND"

class A:
    def __init__(self):
        self.b = B(self)
        print("A : self : {0}, b: {1}".format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print("B : self : {0}, a: {1}".format(hex(id(self)), hex(id(self.a))))

# gc.disable()
my_var = A()
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))
a_id = id(my_var)
b_id = id(my_var.b)

print(hex(a_id))
print(hex(b_id))
print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))

my_var = None
print(gc.collect())

print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))


# sys.intern : Interned String 불러오기
# time.perf_counter: 펑션 실행시간 카운팅
# 아래는 Interning한 String comparison과 일반 comparison을 비교한 예제
import sys
import time


def compare(n):
    a = "a long string that is not interned" * 200
    b = "a long string that is not interned" * 200
    for i in range(n):
        if a == b:
            pass


def compare_intern(n):
    a = sys.intern("a long string that is not interned" * 200)
    b = sys.intern("a long string that is not interned" * 200)
    for i in range(n):
        if a is b:
            pass

start = time.perf_counter()
compare(10000)
end = time.perf_counter()
print(end - start)

def my_func():
    a = 24 * 60
    b = (1,2) * 11
    c = "abc"
    d = "ab" * 11
    e = "the quick brown fox" * 5
    f = ["a","b"] * 3
    g = ["a","a","a","a","a","a","a","a","a","a","a","a","a"]
    
print(my_func.__code__.co_consts) # 해당 펑션의 상수를 나타낸다.


import itertools
for p in itertools.permutations("ABCD"):
    print(p)
    
# 아래와 같은 결과물이 나온다
# ('A', 'B', 'C', 'D')
# ('A', 'B', 'D', 'C')
# ('A', 'C', 'B', 'D')
# ('A', 'C', 'D', 'B')
# ('A', 'D', 'B', 'C')
# ('A', 'D', 'C', 'B')


# ----- 환경변수에 등록하고 value 꺼내오기 (config.json과 같이) ---- #
import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

print(os.getenv("HELLO"))

#.env 파일은 HELLO=WORLD


# Nest Dict
class NestedDict(dict):
    def __getitem__(self, key):
        if key in self:
            return self.get(key)
        return self.setdefault(key, NestedDict())

    def __add__(self, other):
        return other

    def __sub__(self, other):
        return other

    
# SQLAlchemy simple connection making, filtering

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:", echo=False)
Base = declarative_base()

if engine is not None:
    Session = sessionmaker(bind=engine)
    session = Session()
else:
    Session = sessionmaker()
    engine = create_engine("sqlite:///:memory:", echo=False)
    Session.configure(bind=engine)
    session = Session()


class User(Base):
    __tablename__ = "users"

    no = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    id = Column(String(20))
    name = Column(String(20))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "no : {2} //id : {0} // name : {1}".format(self.id, self.name, self.no)

Base.metadata.create_all(engine)

a = User("alpha", "world")
b = User("beta", "world")
session.add_all([a, b])
session.commit()

# filtering example
# for id, name in session.query(User.id, User.name):
#     print(id, name)

# for row in session.query(User).all():
#     print(row)

print(session.query(User).filter(User.id.like("%a")).one_or_none())
# print(session.query(User).filter(User.id.in_(["alpha", "beta"])).all())
# print(session.query(User).filter_by(id="alpha"))
# print(session.query(User).filter(User.id == "alpha"))

import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description == __doc__)
    parser.add_argument("code", type=str, help="Python code snippet")
    parser.add_argument("-r", "--repeats", type=int, default=10, help="Number of repeated times")
    args = parser.parser_args()
    print(args.code)
    print(args.repeats)

# __main__ 의 장점은 실행기점일 때 설정 외에도
# 1) 커맨드라인에서 <python 디렉토리명> 을 입력하면 디렉토리 내의 __main__.py을 찾고 이를 자동으로 실행한다는 것
# 2) zip파일 안에 __main__이 있다면 zipfile 라이브러리를 이용하여 zip을 풀지 않고도 실행시킬 수 있다는 것
# 사실 2번은 __main__빨은 아니고 파이썬의 특징임. 그냥 zip파일내의 소스도 실행가능한데 zip과 __main__의 궁합이 잘 맞는 듯. 
    
