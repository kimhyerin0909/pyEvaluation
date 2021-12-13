import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

svg = open('Busan_districts.svg', 'r').read()
f = open('crimeBusan.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

police = []
crime = ['살인', '강도', '성범죄', '절도', '폭력']

murder = []
robbery = []
sex_offence = []
theft = []
violence = []

data = pd.read_csv('crimeBusan.csv', encoding='utf-8')
test = data.groupby('police')['murder'].sum()
plt.rcParams['font.family'] = "NanumGothic"

plt.figure(figsize=(8,5))
plt.bar(test.index, test)
plt.title('요일에 따른 치킨 주문량 합계')
plt.show()

# for line in rdr:
#     police.append(line[1])
#     murder.append(line[2])
#     robbery.append(line[3])
#     sex_offence.append(line[4])
#     theft.append(line[5])
#     violence.append(line[6])
#
# police.remove("police")
# murder.remove("murder")
# robbery.remove("robbery")
# sex_offence.remove("sex_offence")
# theft.remove("theft")
# violence.remove("violence")
#
# x = np.arange(15)
# plt.title("살인")
# plt.figure(figsize=(19, 10))
# plt.plot(police, murder, color='green', marker='o')
# plt.grid()
# plt.show()

# select = int(input('특정 지역의 5대 범죄 현황을 보고 싶다면 1, 부산 전체의 5대 범죄 현황을 보고 싶다면 2를 입력해주세요.'))
# name = input('5대 범죄 현황을 알고 싶은 지역의 이름을 입력해주세요. : ')

# if select == 1:
#     for row in rdr:
#         if name in row[1]:
#             for i in row[3:]:
#                 result.append(i)
#             plt.style.use('ggplot')
#             plt.rc('font', family='NanumGothic')
#             plt.title(name + '구의 5대 범죄 현황')
#             plt.bar(x, result, color='y')
#             plt.xticks(x, crime)
#             plt.show()
#         else:
#             print("지역의 이름이 일치하지 않습니다.")
# elif select == 2:
#     for line in rdr:
#         a = line[1]
#         locate.append(a)
#         b = line[3]
#         murder.append(b)
#         c = line[4]
#         robbery.append(c)
#         d = line[5]
#         sex_offence.append(d)
#         e = line[6]
#         theft.append(e)
#         g = line[7]
#         violence.append(g)
#     y = np.arange(15)
#     plt.rc('font', family='NanumGothic')
#     plt.style.use('ggplot')
#     plt.title('살인 범죄')
#     plt.figure(figsize=(17, 8))
#     plt.subplot(2, 3, 1)
#     plt.bar(y, sorted(murder), color='y')
#     plt.xticks(visible=False)
#
#     plt.style.use('ggplot')
#     plt.title('강도 범죄')
#     plt.subplot(2, 3, 2)
#     plt.bar(y, sorted(robbery), color='r')
#     plt.xticks(y, locate)
#
#     plt.style.use('ggplot')
#     plt.title('성범죄')
#     plt.subplot(2, 3, 3)
#     plt.bar(y, sorted(sex_offence), color='r')
#     plt.xticks(visible=False)
#
#     plt.style.use('ggplot')
#     plt.title('절도')
#     plt.subplot(2, 3, 4)
#     plt.bar(y, sorted(theft), color='r')
#     plt.xticks(y, locate)
#
#     plt.style.use('ggplot')
#     plt.title('폭력')
#     plt.subplot(2, 3, 6)
#     plt.bar(y, sorted(violence), color='r')
#     plt.xticks(y, locate)
#
#     plt.show()
# else:
#     print("잘 못 입력하셨습니다.")


# f.close()
