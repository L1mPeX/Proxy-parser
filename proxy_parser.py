from bs4 import BeautifulSoup
import requests
import time


def whilee():
    try:
        dta = []

        def get_html(site):
            r = requests.get(site)
            return r.text

        def get_page_data(html):
            soup = BeautifulSoup(html, 'lxml')
            line = soup.find('table', id='theProxyList').find('tbody').find_all('tr')

            for tr in line:
                td = tr.find_all('td')
                ip = td[1].text
                port = td[2].text

                data = str(ip + ":" + port)
                dta.append(data)

        def main():
            for ul in range(1, 7):
                url = 'http://foxtools.ru/Proxy?Page=' + str(ul)
                get_page_data(get_html(url))

            with open('proxy.txt', 'w') as fa:
                fa.write('')

        if __name__ == '__main__':
            main()

        l = dta

        proxy_list = l

        def get_proxy():
            for index, proxy in enumerate(proxy_list):
                url = 'http://' + proxy
                try:
                    r = requests.get('http://ya.ru', proxies={'http': url})
                    if r.status_code == 200:
                        print(index, ">>", proxy)
                        with open('proxy.txt', 'a') as f:
                            f.write(proxy + "\n")
                except requests.exceptions.ConnectionError:
                    continue

        get_proxy()
    except:
        whilee()


while True:
    whilee()
    time.sleep(30)
