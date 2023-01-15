import requests
from bs4 import BeautifulSoup, Tag

# url = 'https://www.dyson.com.tr/shop/sac-sekillendiricileri'
url = 'https://www.dyson.com.tr/products/cord-free/dyson-v11-absolute-extra-vacuums'

def parse_dyson():
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    offer_blocks = soup.find_all("div", {"class": "slider__item"})
    for offer_block in offer_blocks:
        if offer_block:
            buttons_block = offer_block.find('div', {'class': 'card__action'})
            # for button_block in buttons_block:
            if buttons_block:
                for element in buttons_block.contents:
                    if isinstance(element, Tag) and element.name == 'div':
                        txt = element.text
                        if 'Sepete Ekle' in txt:
                            res_text = 'Позиция в наличии '
                            name_header = offer_block.find('a', {'class': 'product-item-link'})
                            try:
                                res_text += f'{name_header.text}'.strip()
                            except:
                                pass
                            try:
                                res_text += '\n' + f"{name_header.attrs['href']}".strip()
                            except:
                                pass
                            return res_text




# print(parse_dyson())
