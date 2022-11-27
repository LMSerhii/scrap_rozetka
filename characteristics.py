import requests

from bs4 import BeautifulSoup

from headers_and_cookies import headers, cookies


def collect_data(url, headers, cookies):
    """ """
    response = requests.get(url=f"{url}characteristics/", headers=headers, cookies=cookies)

    soup = BeautifulSoup(response.text, "lxml")

    characteristics_items = soup.find("dl", class_="characteristics-full__list").find_all("div")

    characteristics = {}
    for characteristics_item in characteristics_items:
        dt = characteristics_item.find("dt")
        dd = characteristics_item.find("dd").find("ul").find_all("li")
        dd_list = ", ".join([d.text for d in dd])

        characteristics[dt.text] = dd_list

    return characteristics


def main():
    url = "https://rozetka.com.ua/ua/272870621/p272870621/"
    print(collect_data(url=url, headers=headers, cookies=cookies))


if __name__ == '__main__':
    main()

