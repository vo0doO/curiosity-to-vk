import CuriosityTrendingparser
from curiosity import post_data


class Run:
    cache = []

    def __init__(self, *args):
        self.args = args

    @staticmethod
    def start():
        CuriosityTrendingparser.TrendingParser.change_href()
        post_data.topic_img_0_alt = img_0_alt_parser()
        topicsparser()
        # post_data.img_0_downloader()
        translater()
        # post_data.painters()
        # post_data.img_1_downloader()
        # post_data.img_3_downloader()
        # post_data.img_2_downloader()
        print("СТОПАК ДЛЯ ДЕБАГ")


Run.cache.append(Run.start())

if __name__ == "__main__":
    print("Миссия выполнена")
