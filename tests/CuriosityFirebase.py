import pyrebase

from curiosity import post_data


# работа с базой данных
def database():
    config = {
        "apiKey": "AIzaSyD6EzxDobegHGvkorLEle6OBt_RNedkD0g",
        "authDomain": "project-3931781304531690229.firebaseapp.com",
        "databaseURL": "https://project-3931781304531690229.firebaseio.com",
        "projectId": "project-3931781304531690229",
        "storageBucket": "project-3931781304531690229.appspot.com",
        "type": "service_account",
        "project_id": "project-3931781304531690229",
        "private_key_id": "fa36c163c3267295a17d6c34a7bbfb9fbb7fb860",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDH+ULfO0USH5/e\n8W274zuSjKMySBIJxU14tB1C+Sl4QREeMbndzflcnJ+HnRDNyvDL5Y9iaiHC+5Ao\nqdPJigr4ggR/jXZ7BMsAEcVVqyzzFZmnqhAdX//uxzjJQZFe8EdANdArhUHMWNr5\nWqY3zG27IqpxRb/75UevY3rWhiWiaIjSyCprNOhs1n16FG1Tjlgi1tG9C8F335qK\nAYiW1FhEZKYqDe82AZSTWwqx/hVl4D+m4BRpmvwbVdJY6cNqWKYUn7HcptmdpSon\nNLX5YxB02ATj1N9jjxzYxaw+msL0oN9ad1/2uzwl1CwdBVRpRGVl3gw6qAxgkTiR\ntExt33T5AgMBAAECggEBAJHiE5jKok7gZz67HfSNhu4YTw3ladNa7nN54kbzgf9K\naHSAjjlzg9C+KdtDB/k5bYUxyPJgvpSB9N7VVb2XSP2VzDZJOv/vtTAtxqoCoF4N\nifS4qdzkJc9J4vFfNe/ulewP1feJ1UCAKe7y5IOcTQjR90l/OtlGoI8goYJShq39\nDoEvp7oSQ3yy3WXSj+WwFrLPz79eLpFymw3WdJ1PRi2y2/ls+wLe5ostEG+FD3kq\ndGDOXXB+FJPJuJrODf6m9qPlxTQkWEXhMYMpMgfKWiAOKhNYYJQ4IpJLSXu4H3WY\ncVPaGRE1df9lrq1yBS35aWzeortebhWrlNKLHSUS4gECgYEA5D28n3NtSNYYhJhO\nLbvXvt7k80RyB+n/bZnX3U42NFrLdMt2yrB59MuDKkgKZubBZMBAZu6FDo6wC/6r\nSRbB30a3KoNlXhLeOGNGRqYLrJBL76Oxt0Ekm68nRdQEGbUUKza5hNoKJLnwBzdD\nazgUBc2gdncfw0xYdrKZ8QNhwpkCgYEA4EtrYk6b3ll2hVaWyZEYXA7upz+24A4k\neafLKMNP3tr0HU9V6VVcZRK72mRrAeBGAoSDm5/Mgvk8XQwr52/zvuV8yim1wmGd\nR1mpYGGSWBFaMxPwSgaBIOhDG0a3HSzfoTGXbUig0WaquMXXOrLk1b8HSBHPMWwR\n5Dm5LJAXIWECgYBS1ZkkYXbzLUh+ruwIqxjU2/5Jz7h26NTcCS6P0ffYLm+Sttkp\nHL1WO5oh+T1VNUBQ+XkmIkDGFMENyWKOxySbjQWi90cNylk+K8FwmIi6GzCEC2vP\nL2RC4GGndRf74H0uZdEUxzFRPO5BICxmuFaD+KnY9MjhT0733UADeY+8WQKBgQDG\nEnRTTV4ifljHKY9hk6uyaFFjC0YhGPwnHwGvDsPy5uLbG1ugAgzlCSUxmKpS7s6E\nnKdogDbnltgyx3PiHyBefWS1Vx42+WMeRlToU2IcOb6xCrORe6r+932DkfBVaHJY\ndGXoUVILeiHbqIMISEEDbX4tq+SQHYKzTDJ14w06IQKBgDZFDIVgk4v81yH0M+oe\nJ1oDUpFj//wVWfuOjalR/+udBIIVJXILchm6rVHOnTEWmvxFZCcD7Zxhy5pEGSDg\nHM/pHOPth8vh5qquEH+Ji613bp/VXVysN37xkpa23fhxSgankqbFiJoxpqOhgWYe\nxgKAzkt34Fug8XYO+hDAbL3X\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-alb7j@project-3931781304531690229.iam.gserviceaccount.com",
        "client_id": "105042264485843483839",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-alb7j%40project-3931781304531690229.iam.gserviceaccount.com",
        "serviceAccount": "/home/ubuntu/workspace/curiosity-to-vk/pycache/kirsanov-dot-com-fa36c163c326.json"
    }

    # инициализация базы

    firebase = pyrebase.initialize_app(config)

    # Получить ссылку на службу авторизации
    auth = firebase.auth()  # uid = 'some-uid'; custom_token = auth.create_custom_token(uid)

    # Зарегистрировать пользователя в базе
    user = auth.sign_in_with_email_and_password("danilakirsanovspb@gmail.com", "Nhb1,e2yfk3$")

    # Получить ссылку на службу базы данных
    db = firebase.database()

    data = {
        "curiosity/topics/" + str(post_data.topic_href).replace('http://curiosity.com/topics/', ''): {
            'id': db.generate_key(),
            'channel': post_data.topic_channel_ru,
            'title': post_data.topic_title_ru,
            'description': post_data.topic_text_1_ru,
            'img': post_data.topic_img_1_scr[0]
        }

    }

    db.update(data)

    # Передайте idToken пользователя методу push
    # results = db.child("curiosity").child("topics").push(data, user['idToken'])
