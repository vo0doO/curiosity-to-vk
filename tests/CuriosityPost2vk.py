# -*- coding: utf-8 -*-
import vk_api

from pycache.run import post_data


def post():
    # Аутинтификация
    login, password = '89214447344', 'e31f567b'
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
    max_index = len(post_data.topic_title_ru) - 1
    while count <= max_index:
        # получаем объект конкретной фотографии
        try:
            photo = upload.photo(
                'C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/0-img-' + str(count) + '-composite.png',
                album_id=243696878)
        except:
            photo = None
            print("Фото 1 не загруженно")
        try:
            photo2 = upload.photo(
                'C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/1-img-' + str(count) + '.png',
                album_id=243696878)
        except:
            photo2 = None
            print("Фото 2 не загруженно")
        try:
            photo3 = upload.photo(
                'C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/2-img-' + str(count) + '.png',
                album_id=243696878)
        except:
            photo3 = None
            print("Фото 2 не загруженно")
        try:
            photo4 = upload.photo(
                'C:/Users/Елена/PycharmProjects/curiosity-to-vk/topics/3-img-' + str(count) + '.png',
                album_id=243696878)
        except:
            photo4 = None
            print("Фото 3 не загруженно")

        # формируем сообщение для поста  #   ☀☀☀☀☀☀☀ 🌈🌈🌈🌈🌈🌈 ✨✨✨✨✨
        post_message = f"✨✨✨Любопытство делает Вас умнее✨✨✨\n" + f"{post_data.topic_text_1_ru[count]}" + f"✨{post_data.topic_paragraph_2_title_ru[count]}" + f"{post_data.topic_paragraph_2_text_ru[count]}" + f"✨{post_data.topic_paragraph_3_title_ru[count]}" + f"{post_data.topic_paragraph_3_text_ru[count]}" + f"#{post_data.topic_channel_ru[count]}"

        link = 'https://www.youtube.com/watch?v=tkm0TNFzIeg'
        # ПОСТИМ ВСЕ ЭТО ДЕЛО

        if photo and photo2 and photo3 and photo4 is None:
            post(owner_id=408323065,
                 friends_only=0,
                 from_group=1,
                 message=str(post_message[:]),
                 attachments=f'photo{photo[0]["owner_id"]}_{photo[0]["id"]},photo{photo2[0]["owner_id"]}_{photo2[0]["id"]},photo{photo3[0]["owner_id"]}_{photo3[0]["id"]},photo{photo4[0]["owner_id"]}_{photo4[0]["id"]}')
        elif photo and photo2 and photo3 is not None:
            post(owner_id=408323065,
                 friends_only=0,
                 from_group=0,
                 message=str(post_message[:]),
                 attachments=f'photo{photo[0]["owner_id"]}_{photo[0]["id"]},photo{photo2[0]["owner_id"]}_{photo2[0]["id"]},photo{photo3[0]["owner_id"]}_{photo3[0]["id"]}')
        elif photo and photo2 is not None:
            post(owner_id=408323065,
                 friends_only=0,
                 from_group=0,
                 message=str(post_message[:]),
                 attachments=f'photo{photo[0]["owner_id"]}_{photo[0]["id"]},photo{photo2[0]["owner_id"]}_{photo2[0]["id"]}')
        else:
            post(owner_id=408323065,
                 friends_only=0,
                 from_group=0,
                 message=str(post_message[:]),
                 attachments=f'photo{photo[0]["owner_id"]}_{photo[0]["id"]}')
        print(f"Пост № {str(count)} выполнен")
        count += 1


post()
print("СТОПАК ДЛЯ ДЕБАГ")
if __name__ == '__main__':
    print("Пост выполнен")
