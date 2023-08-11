import bs4.element
import requests
from bs4 import BeautifulSoup
import json


def parser_table(table: bs4.element.Tag) -> list:
    return_list = []
    tr_list = table.find_all("tr")
    for tr in tr_list:
        td_list = tr.find_all("td")
        if td_list[1].text.lower() != "unicode point":
            unicode_point = td_list[1].text
            unicode_character = chr(int(unicode_point, 16))
            return_list.append({td_list[2].text: unicode_character})
    return return_list


def main():
    r = requests.get('https://learn.microsoft.com/en-us/windows/apps/design/style/segoe-fluent-icons-font')
    soup = BeautifulSoup(r.content, 'html.parser')
    t_list = soup.find_all("table")
    font_list = []
    for t in t_list:
        font_list += parser_table(t)
    with open("font_list.json", "w", encoding='utf-8') as f:
        json.dump(font_list, f, indent=4, ensure_ascii=True)


if __name__ == '__main__':
    main()
