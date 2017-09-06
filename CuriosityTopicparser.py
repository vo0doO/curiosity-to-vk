import re

import requests
from bs4 import BeautifulSoup


def topic_parser(href):
    # НАСТРАИВАЕМ ПАРСЕРА

    r = requests.get(href)

    html = r.text.encode("utf-8")

    with open(file="C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/" + str(href).replace(
        "http://curiosity.com/topics/", "").replace("/", "") + ".html", mode="w") as th:
        th.write(str(html))

    soup = BeautifulSoup(html, "lxml")

    topic_page = soup.find("div", {"class": "topic-page"})

    content_header = topic_page.find_all("div", {"class": "image-header"})

    topic_contents = topic_page.find("div", {"class": ["topic-content", "content-items"]})

    topic_content_item = topic_contents.find_all("div", {"class": "content-item"})

    regexp_img_1 = re.compile(r'/curiosity-data\.s3\.amazonaws\.com/images/content/hero/standard/(.*?)\.png\"\)')

    tags = topic_page.find("div", {"class", "topic-tags"}).text


    # Головные данные
    for item in content_header:
        # ТЕГИ HTML

        # ТЕГИ ТЕКСТ
        topic_page.find("div", {"class", "topic-tags"}).text
        # ID 1-го изображения
        img_1_href = re.findall(regexp_img_1, item.find('style').text)
        # ТЕКСТ СТАТЬИ ПОСТА TODO: Формируем текст поста {topic_content_item[0].text};{topic_content_item[2].text}; {topic_content_item[4].text}; {topic_content_item[3].text}; {topic_content_item[5].text}; {topic_content_item[7].text}; {topic_content_item[9].text}{topic_content_item[10].text}{topic_content_item[14].text}
        text_1 = f"{topic_content_item[1].text}{topic_content_item[6].text}{topic_content_item[8].text}"
        '''
        if "google" in text_1:
            text_1 = f"{topic_content_item[0].text}{topic_content_item[1].text}{topic_content_item[3].text}{topic_content_item[4].text}{topic_content_item[5].text}"
        else:
            text_1 = f"{topic_content_item[0].text}{topic_content_item[1].text}{topic_content_item[2].text}{topic_content_item[3].text}{topic_content_item[4].text}{topic_content_item[5].text}"
        '''
        # ссылка на 2-е изображения
        try:
            img_2_href = \
                topic_contents.find("div", {"class": "embedded-graphic-content"}).find("img", {"class": "lazyload"})[
                    "data-src"]
        except AttributeError:
            img_2_href = None
            print("ссылка на 2-е изображения не найдена")

        # ссылка на 3-е изображение
        try:
            img_3_href = \
                topic_contents.find("div", {"class": "embedded-graphic-content"}).find("img", {"class": "lazyload"})[
                    "data-src"]
        except AttributeError:
            img_3_href = None
            print("ссылка на 3-е изображения не найдена")

        # заголовок видеоролика
        try:
            video_1_title = topic_contents.find("div", {"class": "first-video"}).find("h4").text
        except:
            video_1_title = None
            print("заголовок видео не найден")

        # ID видеоролика
        try:
            video_1_data_scr = \
                topic_contents.find("div", {"class": "first-video"}).find("div", {"class": "module-video"}).find("div",{"class": "js-media-player"})["data-src"]
        except:
            video_1_data_scr = None
            print("ссылка на видео не найдена")

        # условия прохода если HTML топика с багами
        if item.find("div", {"class": "header-content"}).find('a') != None:

            # название канала
            channel = item.find("div", {"class": "header-content"}).find('a').text

            # заголовок топика
            title = item.find("div", {"class": "header-content"}).find('h1').text

        elif item.find("div", {"class": "header-content"}).find('a') == None:

            channel = item.find("div", {"class": "header-content"}).find('h5').text

            title = item.find("div", {"class": "header-content"}).find('h1').text

    # Данные в теле

    # основной текст топика

    return img_1_href, channel, title, text_1, img_2_href, img_3_href, video_1_title, video_1_data_scr


# href = "https://curiosity.com/topics/the-gish-gallop-wins-debates-with-a-deluge-of-lies-curiosity/"
# img_1_href, channel, title, text_1, img_2_href, img_3_href, video_1_title, video_1_data_scr, soup, topic_contents, topic_tag = topic_parser(href)
# x = 0
if __name__ == "__main__":
    print("Парсимс")
