import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import datetime

head = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}
base_url = 'http://rate.am/'


res = requests.get(base_url,headers=head)

soup = BeautifulSoup(res.text,'html.parser')

mid_value = soup.find_all('tr',class_='btm')[2]

mid_dollar = float(mid_value.find_all('td',class_='fhd')[1].get_text())
mid_euro = float(mid_value.find_all('td',class_='fhd')[3].get_text())
mid_rub = float(mid_value.find_all('td',class_='fhd')[5].get_text())

def main(a,b):

    plt.bar(a,b,width=0.8)
    for i in range(len(a)):
        pos = b[i]
        string = '{:} դրամ'.format(pos)
        plt.text(i,pos,string,ha='center',color='black')

    plt.show()

plt.title(f"{datetime.datetime.now().date()} դրամ դոլար եվրո")

plt.xlabel('արժույթ')
plt.ylabel('գին')


try:
    values =['$','€','₽']
    values2 = [mid_dollar,mid_euro,mid_rub]
    main(values,values2)
except Exception:
    print('erorr')