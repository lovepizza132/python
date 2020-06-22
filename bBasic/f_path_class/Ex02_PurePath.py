"""
# Path는 파일 시스템에 접근하기 때문에, 기본적으로 운영체제 상에 조작 대상 파일 경로가 존재해야 합니다.
# PurePath는 순수 경로의 기반 클래스입니다.
# 파일 시스템에 접근하지 않기 때문에, 운영체제 상에 존재하지 않는 파일 경로를 다룰 수도 있습니다.
"""

from pathlib import PurePath, PureWindowsPath
#-------------------------------------------------------------------
# 1 - 존재하지 않는 파일
# p = PurePath(r'\\192.168.0.111\Share\kosmo')
p = PurePath('C:\Windows\System32\drivers\etc\hosts')
print(p)
print(p.drive)  # 존재하지 않는 파일임에도 p.drive가 나옴
print(p.parts[3])   # \단위로 쪼개서 가져오는 듯함
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
print(p.parents[3])
print(p.parents[4])
# print(p.parents[5]) # 더 이상 부모가 없어서 에러
print(p.as_uri())       # 실제 파일을 가져다 올 수 있는 url로 제공





#-------------------------------------------------------------------
# 2. 실제 경로로 아닌 가짜 경로를 관리하는 PurePath를 어디에 사용할까?
# 아마도 경로나 파일명만 조작할 때 사용하지 않을까?
# 해당 경로나 파일명이 현재 컴퓨터가 아니기에 이름만 관리하는 작업이 필요할 듯 싶다