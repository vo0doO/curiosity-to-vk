# -*- coding: utf-8 -*-
import re
import time

import requests
import vk_api
from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageOps
from bs4 import BeautifulSoup

import CuriosityTopicparser
import CuriosityTrendingparser


# TODO: 2. Прописать рекурсивную подгузку и доработку поста
# TODO: 2.1. ссылки на магазин
# TODO: 2.2. ссылки на журнал
# TODO: 2.1. апач с файлами HTML
# TODO: 3. Добавить логотип школы изобылия
# TODO: 4. Запустить асинхронного бота
# TODO: 4.1 Настроить репост


class Curiosity:
    # РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
    re_zero_img = re.compile(r"https://curiosity-data\.s3\.amazonaws\.com/images/content/meme/standard/(.*?)\.png")
    # СПИСКИ С АНГЛИЙСКИМ ТЕКТОМ
    topic_href = []
    topic_channel = []
    topic_tags = []
    topic_title = []
    topic_img_0_href = []
    topic_img_0_hrefs = []
    topic_img_0_scr = []
    topic_img_0_alt = []
    topic_text_1 = []
    topic_img_1_href = []
    topic_img_1_scr = []
    topic_img_2_href = []
    topic_img_2_src = []
    topic_img_3_href = []
    topic_img_3_src = []
    topic_video_1_title = []
    topic_video_1_data_scr = []
    # СПИСКИ С РУССКИМ ТЕКСТОМ
    topic_channel_ru = []
    topic_title_ru = []
    topic_img_0_alt_ru = []
    topic_text_1_ru = []
    topic_tags_ru = []

    def __init__(self, *args):
        self.args = args


# ПОМОШНИК АНАЛИЗАТОРА
def img_0_alt_parser():
    respon = requests.get("http://curiosity.com/trending/day/")
    html = respon.text
    soup = BeautifulSoup(html, "lxml")
    trending_grid = soup.find("div", {"class": "js-trending-grid"})
    all_a = trending_grid.find_all("img")
    for item in all_a:
        alt = item["alt"]
        Curiosity.topic_img_0_alt.append(str(alt))
    print("Анализатор получил текст заманух")


# ГРУЗЧИК
def img_0_downloader():
    respon = requests.get("http://curiosity.com/trending/day/")
    html = respon.text
    zero_img_srcs = re.findall(Curiosity.re_zero_img, html)
    for x in zero_img_srcs[::3]:
        Curiosity.topic_img_0_hrefs.append(x)
    count = 0
    max_ind = len(Curiosity.topic_channel) - 1
    while count <= max_ind:
        Curiosity.topic_img_0_href.append(
            "http://curiosity-data.s3.amazonaws.com/images/content/meme/standard/" + Curiosity.topic_img_0_hrefs[
                count] + ".png")
        res = requests.get(Curiosity.topic_img_0_href[count])
        with open('C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/0-img-' + str(count) + '.png',
                  'wb') as zero:
            zero.write(res.content)
        Curiosity.topic_img_0_scr.append(
            '/home/ubuntu/workspace/curiosity-to-v/topics/0-img-' + str(count) + '.png')
        count += 1
    print("Скачены изображениея обложек")
    return Curiosity.topic_img_0_scr


# ПЕРЕВОДЧИК
def translater():
    # ВРЕМЕННЫЕ ПЕРЕМЕННЫЕ ДЛЯ ЦИКЛОВ
    count = 0
    max_index = len(Curiosity.topic_channel) - 1
    # ПЕРЕВОДИМ СПИСКИ
    while count <= max_index:
        # КАНАЛ
        channel = {
            "key": "trnsl.1.1.20170730T114755Z.994753b77b648f24.f3ed7d2f59fcb232c089a1a3328c0e0b900d4925",
            "text": f"{Curiosity.topic_channel[count]}.",
            'lang': 'en-ru',
            'format': 'plain'
        }
        # ЗАГОЛОВОК
        title = {
            "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
            "text": f"{Curiosity.topic_title[count]}.",
            'lang': 'en-ru',
            'format': 'plain'
        }
        # ЗАМАНУХА
        alt = {
            "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
            "text": f"{Curiosity.topic_img_0_alt[count]}.",
            'lang': 'en-ru',
            'format': 'plain'
        }
        # ТЕКСТ
        text_1 = {
            "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
            "text": f"{Curiosity.topic_text_1[count]}.",
            'lang': 'en-ru',
            'format': 'plain'
        }
        # ТЕГИ
        '''
        tags = {
            "key": "trnsl.1.1.20170514T220842Z.5b2c14ecd7990670.3ccb355751262f1359f3c3ff0b9b7d5447ce39a1",
            "text": f"{Curiosity.topic_tags[count]}.",
            'lang': 'en-ru',
            'format': 'plain'
        }
        '''
        # ДЕЛАЕМ ЗАПРОС К ЯНДЕКС ПЕРЕВОДЧИКУ И СОХРАНЯЕМ ОТВЕТ
        channel_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=channel).json()
        # КАНАЛ
        title_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=title).json()
        # ЗАГОЛОВОК
        text_1_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=text_1).json()
        # ЗАМАНУХА
        img_0_alt_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=alt).json()
        # ТЕГИ
        # tags_ru = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=tags).json()
        # ЗАПОЛНЯЕМ СПИСКИ С РУССКИМ ТЕКСТОМ
        # ЗАГОЛОВОК
        Curiosity.topic_title_ru.append(title_ru['text'][0])
        # ЗАГОЛОВОК
        Curiosity.topic_channel_ru.append(channel_ru['text'][0])
        # КАНАЛ
        Curiosity.topic_text_1_ru.append(text_1_ru['text'][0])
        # ЗАМАНУХА
        Curiosity.topic_img_0_alt_ru.append(img_0_alt_ru["text"][0])
        # ТЕГИ
        # Curiosity.topic_tags_ru.append((tags_ru["text"][0]))
        count += 1
    print("Переводчик выполнил свою работу")


# КИСТЬ
def draw(count):
    # =========================
    # #######НАСТРОЙКА КИСТИ##########
    # =========================
    # НАЗВАНИЕ КАНАЛА
    try:
        channel = Curiosity.topic_channel_ru[count].upper()
        # ЗАГОЛОВОК
        if len(Curiosity.topic_title_ru[count]) <= 40:
            title = Curiosity.topic_title_ru[count]
        else:
            titlelist = list(Curiosity.topic_title_ru[count])
            titlelist.insert(40, '-\n')
            title = ''.join(titlelist)
    except AttributeError:
        channel = "УДИВИТЕЛЬНАЯ ПЛАНЕТА"
        title = "Ну что вы тут ещё не видели люди на этой удивительной планете?"
        if len(title) <= 41:
            title = title
        else:
            titlelist = list(title)
            titlelist.insert(41, '\n')
            title = ''.join(titlelist)
    # ОБЛОЖКА ТОПИКА НА АНГЛ.
    img_composit = Image.open(
        "C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/0-img-" + str(count) + ".png").convert("RGBA")
    # БАЗА, ОНА ЖЕ - ЛОГО_ПАИНТЕР
    logo_painter = Image.open('C:/Users/Елена/PycharmProjects/curiosity-to-vk/desing/logo-playload.png').convert("RGBA")
    # ШРИФТЫ
    channel_font = ImageFont.truetype(
        "C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/Roboto-Fonts/Roboto-Bold.ttf", 42)
    title_font = ImageFont.truetype("C:/Users/Елена/PycharmProjects/curiosity-to-vk/Roboto-Fonts/Roboto-Bold.ttf", 42)
    # РАЗМЕР БЛОКА ТЕКСТА С НАЗВАН
    channel_size = channel_font.getsize(str(channel))
    # РАЗМЕР БЛОКА ТЕКСТА С НАЗВАНИЕМ КАНАЛА В КОРТЕЖЕ
    _size = (channel_size[0] + 20, channel_size[1] + 40)
    # НОВОЕ ИЗОБРАЖЕНИЕ ДЛЯ НАНЕСЕНИЯ ТЕКСТА С НАЗВАНИЕМ КАНАЛА
    channel_im = Image.open('./Button.png').convert("RGBA")
    # ИЗМЕНЯЕМ РАЗМЕР ИЗОБРАЖЕНИЯ
    channel_img = channel_im.resize(_size, resample=0)
    # КИСТЬ для пустое ИЗОБРАЖЕНИЕ для нанесения текста с названием КАНАЛА
    channel_draw = ImageDraw.Draw(channel_img)
    # МЕТОД ПРОРИСОВКИ мультистрокового ТЕКСТА с названием канала на изобрание
    x = (_size[0] - channel_size[0]) / 2
    y = (_size[1] - channel_size[1]) / 2
    channel_draw.multiline_text((x, y), channel, font=channel_font, align="center")
    # ========================
    # #########МОДИФИКАЦИЯ ИЗОБРАЖЕНИЯ#######
    # =========================
    # МОДИФИКАЦИЯ нижней части ОСНОВНОГО ИЗОБРАЖЕНИЯ
    box = (1, 875, 999, 999)
    # ВЫРЕЗАЕМ
    text = img_composit.crop(box)
    # СОЗДАЕМ ФИЛТР
    gaus = ImageFilter.GaussianBlur(radius=20)
    # ПРИМЕНЯЕМ ФИЛТР К ВЫРЕЗКЕ
    textarea = text.filter(gaus)
    # АВТОКОНТРАСТ
    # ImageOps.autocontrast(textarea, cutoff=0, ignore=None)
    # УДАЛЯЕМ ГРАНИЦЫ
    ImageOps.crop(textarea)
    # ВСТАВЛЯЕМ ВЫРЕЗКУ НАЗАД
    img_composit.paste(textarea, (1, 875))
    img_composit.save("./topics/0-img-" + str(
        count) + ".png")
    # КИСТЬ для ЗАГРУЗЧИКА
    logo_painter_draw = ImageDraw.Draw(logo_painter)
    # ПРОРИСОВКА канал загрузчик
    logo_painter.paste(channel_img, (27, 800))
    # ПРОРИСОВКА заголовок на ЗАГРУЗЧИК ЛОГОТИПОВ
    logo_painter_draw.multiline_text((27, 890), title, font=title_font, align="left")  # fill=(255,0,255,255)
    # МОДИФИКАЦИЯ нижней части ОСНОВНОГО ИЗОБРАЖЕНИЯ
    # ВЫРЕЗАЕМ
    img_composits = Image.open(
        "C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/0-img-" + str(count) + ".png").convert("RGBA")
    logo_box = (1, 70, 999, 70)
    logob = img_composits.crop(logo_box)
    gaus = ImageFilter.GaussianBlur(radius=2)
    logoArea = logob.filter(gaus)
    img_composits.paste(logoArea, (1, 1))
    # ЗАКАТЫВАЕМ ПОЛУЧЕНЫЙ КОМПОТ
    img_composits.save("./topics/0-img-" + str(count) + ".png")
    # СВЕДЕНИЕ СЛОЕВ обложки и загрузчика логотипов
    img_composite = Image.open("./topics/0-img-" + str(count) + ".png", mode='r').convert("RGBA")
    img_composite = Image.alpha_composite(img_composite, logo_painter)
    # СОХРАНЯЕМ РЕЗУЛЬТАТ - ГОТОВУЮ ОБЛОЖКУ ПОСТА в файл
    img_composite.save("./topics/0-img-" + str(count) + "-composite.png")


# ГЛАВНЫЙ АНАЛИЗАТОР
def topicsparser():
    # ПОЛУЧАЕМ СГРУПИРОВАННЫЕ ССЛЫКИ НА ПОСТЫ ОТ АНАЛИЗАТОРА ТРЕНДОВ
    in_db, new, to_post = CuriosityTrendingparser.TrendingParser.change_href()
    for href in new:
        try:
            img_1_href, channel, title, text_1, img_2_href, img_3_href, video_1_title, video_1_data_scr = CuriosityTopicparser.topic_parser(
                href)
            # ЗАПОЛНЯЕМ СПИСКИ
            # каналы
            Curiosity.topic_channel.append(str(channel))
            # заголовки
            Curiosity.topic_title.append(str(title))
            # ссылок на 1 изображения
            Curiosity.topic_img_1_href.append(
                "http://curiosity-data.s3.amazonaws.com/images/content/hero/standard/" + img_1_href[0] + ".png")
            # текты первых блоков
            Curiosity.topic_text_1.append(str(text_1))
            # ссылки на 2 изображения
            Curiosity.topic_img_2_href.append(str(img_2_href))
            # ссылки на 3 изображения
            Curiosity.topic_img_3_href.append(str(img_3_href))
            # заголовки видеороликов
            Curiosity.topic_video_1_title.append(str(video_1_title))
            # ID видеороликов
            Curiosity.topic_video_1_data_scr.append(str(video_1_data_scr))
            # ТЕГИ
            #Curiosity.topic_tags.append(str(topic_tag))
        except ArithmeticError:
            print("Ошибочка выскочила")


# ЖУРНАЛИСТ
def post():
    # Аутинтификация
    login, password = '89045155434', '778899'
    vk_session = vk_api.VkApi(login, password)
    # проверка сессиии
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    # получаем объект API
    vk = vk_session.get_api()
    # получаем файловый объект сессии используемый для загрузки
    upload = vk_api.VkUpload(vk_session)
    # ЦИКЛ ПОСТОВ
    count = 0
    max_index = 8
    while count <= max_index:
        # получаем объект конкретной фотографии
        try:
            photo = upload.photo(
                'C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/0-img-' + str(count) + '-composite.png',
                album_id=248018572)
        except:
            photo = None
            print("Фото 1 не загруженно")
        try:
            photo2 = upload.photo(
                'C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/1-img-' + str(count) + '.png',
                album_id=248018572)
        except:
            photo2 = None
            print("Фото 2 не загруженно")
        try:
            photo3 = upload.photo(
                'C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/2-img-' \
                + str(count) + '.png',
                album_id=248018572)
        except:
            photo3 = None
            print("Фото 2 не загруженно")
        try:
            photo4 = upload.photo(
                'C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/3-img-' + str(count) + '.png',
                album_id=248018572)
        except:
            photo4 = None
            print("Фото 3 не загруженно")

        # ССЫЛКА НА САЙТ
        #  ☀☀☀☀☀☀☀ 🌈🌈🌈🌈🌈🌈 ✨✨✨✨✨🇷🇺 💡 🇷🇺
        # ПОДГОТОВКА ПЕРЕМЕННЫХ ДЛЯ ПОСТА
        # tag = Curiosity.topic_tags_ru[count].replace("\n", "#")
        # tag = tag.replace(".", "")
        # tag = tag.replace('#', "🇷🇺#")
        # channel_tag = Curiosity.topic_channel_ru[count].replace(".", "")
        topic_text = Curiosity.topic_text_1_ru[count].replace("\n\n\n", "\n", 1)
        # ТЕКСТ СТАТЬИ ДЛЯ ПОСТА  # {tag}{channel_tag}🇷🇺\n\n
        post_message = f"✨✨✨Любопытство делает Вас умнее✨✨✨\n💡💡💡{Curiosity.topic_img_0_alt_ru[count].replace('n', ' ').upper()}💡💡💡\n{topic_text}"
        # ВИДОС
        link = f"https://www.youtube.com/watch?v={Curiosity.topic_video_1_data_scr[count]}"

        if photo and photo2 and photo3 and photo4 is None:
            vk.wall.post(
                owner_id=279286486,
                friends_only=0,
                from_group=0,
                message=str(post_message[:]),
                attachments=f'photo{photo[0]["owner_id"]}_{photo[0]["id"]},photo{photo2[0]["owner_id"]}_{photo2[0]["id"]},photo{photo3[0]["owner_id"]}_{photo3[0]["id"]},photo{photo4[0]["owner_id"]}_{photo4[0]["id"]}, {link}')
        elif photo and photo2 and photo3 is not None:
            vk.wall.post(
                owner_id=279286486,
                friends_only=0,
                from_group=0,
                message=str(post_message[:]),
                attachments=f'photo{photo[0]["owner_id"]}_{photo[0]["id"]},photo{photo2[0]["owner_id"]}_{photo2[0]["id"]},photo{photo3[0]["owner_id"]}_{photo3[0]["id"]}, {link}')
        elif photo and photo2 is not None:
            vk.wall.post(
                owner_id=279286486,
                friends_only=0,
                from_group=0,
                message=str(post_message[:]),
                attachments=f'photo{photo[0]["owner_id"]}_{photo[0]["id"]},photo{photo2[0]["owner_id"]}_{photo2[0]["id"]}, {link}')
        else:
            vk.wall.post(
                owner_id=279286486,
                friends_only=0,
                from_group=0,
                message=str(post_message[:]),
                attachments=f'photo{photo[0]["owner_id"]}_{photo[0]["id"]}, {link}')
        print(f"Пост № {str(count)} выполнен")
        # time.sleep(600)
        count += 1


# ГРУЗЧИК
def img_3_downloader():
    count = 0
    max_index = len(Curiosity.topic_img_3_href) - 1
    while count <= max_index:
        try:
            res = requests.get(Curiosity.topic_img_3_href[count])
            with open('C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/3-img-' + str(count) + '.png',
                      'wb') as zero:
                zero.write(res.content)
                # Curiosity.topic_img_3_scr.append('/home/ubuntu/workspac/curiosity-to-v/topics/two-img-' + str(count) + '.png')
        except:
            with open('C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/3-img-' + str(count) + '.png',
                      'wb') as zero:
                zero.close()
        count += 1
    print("Скачены третьи изображениея")
    # return Curiosity.topic_img_3_scr


# ГРУЗЧИК
def img_2_downloader():
    count = 0
    max_index = len(Curiosity.topic_img_2_href) - 1
    while count <= max_index:
        try:
            res = requests.get(Curiosity.topic_img_2_href[count])
            with open('C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/2-img-' + str(count) + '.png',
                      'wb') as zero:
                zero.write(res.content)
        except:
            with open('C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/2-img-' + str(count) + '.png',
                      'wb') as zero:
                zero.close()
        count += 1
    print("Скачены вторые изображениея")


# ГРУЗЧИК
def img_1_downloader():
    count = 0
    max_index = len(Curiosity.topic_img_1_href) - 1
    while count <= max_index:
        res = requests.get(Curiosity.topic_img_1_href[count])
        with open('C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/1-img-' + str(count) + '.png',
                  'wb') as zero:
            zero.write(res.content)
        Curiosity.topic_img_1_scr.append(
            '/home/ubuntu/workspac/curiosity-to-v/topics/1-img-' + str(count) + '.png')
        count += 1
    print("Скачены первые изображениея")
    return Curiosity.topic_img_1_scr


# ХУДОЖНИК
def painters() -> object:
    # ЦИКЛ ПРОХОДА ИЗОБРАЖЕНИЙ ДЛЯ ХУДОЖНИКА
    count = 0
    max_index = len(Curiosity.topic_title) - 1
    while count <= max_index:
        draw(count)
        count += 1
    print(f"ХУДОЖНИК УСПЕШНО ОТРИСОВАЛ {max_index} ИЗОБРАЖЕНИЙ")
    return
    # ======ТЕСТЫ==========ТЕСТЫ===============ТЕСТЫ=============ТЕСТЫ============== #


CuriosityTrendingparser.TrendingParser.change_href()
img_0_alt_parser()
topicsparser()
img_0_downloader()
translater()
painters()
img_1_downloader()
img_3_downloader()
img_2_downloader()
post()
x = 0
# ======КОД ВЫПОЛНЯЕМЫЙ ПРИ ИМПОРТЕ============== #
if __name__ == "__main__":
    print("Любопытcтво делает вас умнее")