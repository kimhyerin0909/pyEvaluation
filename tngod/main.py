import matplotlib.pyplot as plt
import csv
import operator

f = open('crimeBusan.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

police = []  # 경찰서
murder = []
robbery = []
sex_offence = []
theft = []
violence = []

for line in rdr:
    a = line[1]
    police.append(a)
    b = line[3]
    murder.append(b)
    c = line[4]
    robbery.append(c)
    d = line[5]
    sex_offence.append(d)
    e = line[6]
    theft.append(e)
    g = line[7]
    violence.append(g)

police.remove('경찰서')
murder.remove('살인')
robbery.remove('강도')
sex_offence.remove('성범죄')
theft.remove('절도')
violence.remove('폭력')

dic1 = {police[i] : murder[i] for i in range(len(police))}
# sdic1 = sorted(dic1.items(), key = lambda item: item[1])
#
# print(sdic1)
reverse = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.rc('font', family='NanumGothic')

plt.subplot(2, 1, 1)
plt.plot([0, 2], reverse, 'ro--')
plt.ylabel('살인')
plt.xticks(visible=False)
plt.title('2020 부산광역시 5대 범죄 발생 현황')

plt.tight_layout()
plt.show()
f.close()
