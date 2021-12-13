import matplotlib.pyplot as plt
import pandas as pd
import json
import mpld3

data = pd.read_csv('crimeBusan.csv', encoding='cp949')
murder = data.groupby('police')['murder'].sum()
robbery = data.groupby('police')['robbery'].sum()
sex_offence = data.groupby('police')['sex_offence'].sum()
theft = data.groupby('police')['theft'].sum()
violence = data.groupby('police')['violence'].sum()
plt.rcParams['font.family'] = "NanumGothic"

f = plt.figure(figsize=(30, 10))
plt.subplot(2, 3, 1)
plt.grid()
plt.title('살인')
plt.bar(murder.index, murder, color='#E57373')

plt.subplot(2, 3, 2)
plt.grid()
plt.title('강도')
plt.plot(robbery.index, robbery, color='orange', marker='d', linestyle='-')

plt.subplot(2, 3, 3)
plt.grid()
plt.title('성범죄')
plt.bar(sex_offence.index, sex_offence, color='#677EF2')

plt.subplot(2, 3, 4)
plt.grid()
plt.title('절도')
plt.bar(theft.index, theft)

plt.subplot(2, 3, 5)
plt.grid()
plt.title('폭력')
plt.plot(violence.index, violence, color='#e35f62', marker='o', linestyle='--')
plt.savefig('result.svg')

plt.show()

# print(mpld3.fig_to_html(f, figid='THIS_IS_FIGID')) # html코드로 저장해줌
