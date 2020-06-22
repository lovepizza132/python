
# (1) 전체 모듈 사용시
import mypackage.mymodule

print('오늘의 날씨 : ', mypackage.mymodule.get_weather())
print('오늘의 요일 : ', mypackage.mymodule.get_date())


from mypackage import mymodule

print('오늘의 날씨 : ', mymodule.get_weather())
print('오늘의 요일 : ', mymodule.get_date())


from mypackage import mymodule as mymo

print('오늘의 날씨 : ', mymo.get_weather())
print('오늘의 요일 : ', mymo.get_date())


# (2) 모듈에서 부분적으로 사용시
# from mypackage.mymodule import get_weather, get_date
# print('오늘의 날씨 : ', get_weather())
# print('오늘의 요일 : ', get_date())
