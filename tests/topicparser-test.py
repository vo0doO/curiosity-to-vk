import CuriosityTopicparser
from CuriosityTrendingparser import TrendingParser as TrendingParser

# ТУЧА С ДАННЫМИ

topic_img_1_href = []
topic_channel = []
topic_title = []
topic_text_1 = []
topic_img_2_href = []
topic_img_3_href = []
topic_video_1_title = []
topic_video_1_data_scr = []
topic_tags = []
# ==========TEST================TEST======================TEST============== #

in_db, new, to_post = TrendingParser.change_href()
for href in new:
    try:
        img_1_href, channel, title, text_1, img_2_href, img_3_href, video_1_title, video_1_data_scr, soup, topic_contents, topic_tag = CuriosityTopicparser.topic_parser(
            href)

        # ЗАПОЛНЯЕМ СПИСКИ
        # каналы
        topic_channel.append(str(channel))

        # заголовки
        topic_title.append(str(title))

        # ссылок на 1 изображения
        topic_img_1_href.append(
            "http://curiosity-data.s3.amazonaws.com/images/content/hero/standard/" + img_1_href[0] + ".png")

        # текты первых блоков
        topic_text_1.append(str(text_1))

        # ссылки на 2 изображения
        topic_img_2_href.append(str(img_2_href))

        # ссылки на 3 изображения
        topic_img_3_href.append(str(img_3_href))

        # заголовки видеороликов
        topic_video_1_title.append(str(video_1_title))

        # ссылки на видеоролики
        topic_video_1_data_scr.append(str(video_1_data_scr))

        topic_tags.append(str(topic_tag).replace("\n", " #"))

    except:
        print("Ошибочка выскочила")

print("СТОПАК-ДЛЯ-ДЕБАГ")

if __name__ == "__main__":
    print("Парсимс")
