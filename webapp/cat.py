CAT_PHOTO_PATH_1 = "images/cat1.png"
CAT_PHOTO_PATH_2 = "images/cat2.png"
class Cat:
    name = ""
    age = 1
    avatar = CAT_PHOTO_PATH_1
    satiety = 40
    happiness = 40

    @classmethod
    def get_avatar(cls):
        if cls.happiness > 50:
            cls.avatar =CAT_PHOTO_PATH_2
        else:
            cls.avatar =CAT_PHOTO_PATH_1

    @classmethod
    def play(cls):
        cls.happiness += 20
        cls.get_avatar()

    @classmethod
    def sleep(cls):
        cls.happiness += 10


    @classmethod
    def feed(cls):
        cls.satiety += 20