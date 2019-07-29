import random
from faker import Factory
import string


class TestdataGenerator(object):
    """一些生成器方法，生成随机数，手机号，以及连续数字等"""
    def __init__(self):
        self.fake = Factory().create('zh_CN')

    def random_phone_number(self):
        """随机手机号"""
        return self.fake.phone_number()

    def random_name(self):
        """随机姓名"""
        return self.fake.name()

    def random_address(self):
        """随机地址"""
        return self.fake.address()

    def random_email(self):
        """随机email"""
        return self.fake.email()

    def random_ipv4(self):
        """随机IPV4地址"""
        return self.fake.ipv4()

    def random_str(self, min_chars=0, max_chars=8):
        """长度在最大值与最小值之间的随机字符串，只包含a-zA-Z字母"""
        return self.fake.pystr(min_chars=min_chars, max_chars=max_chars)

    def random_int(self, min_value=0, max_value=9999, exclude=None):
        """返回[min_value, max_value]范围内的一随机数，可排除范围内任意数"""
        if exclude is not None:
            if not isinstance(exclude, list):
                return "exclude must a list"
        else:
            exclude = list()
        while True:
            value = self.fake.pyint(min_value=min_value, max_value=max_value)
            if value not in exclude:
                return value

    def random_letter_digit_str(self, min_chars=0, max_chars=8):
        """长度在最大值与最小值之间的随机字符串，只包含a-zA-Z字母和0-9数字"""
        if min_chars is None:
            return "".join(self.random_letters_digits(length=max_chars))
        else:
            assert (
                max_chars >= min_chars), "Maximum length must be greater than or equal to minium length"
            return "".join(
                self.random_letters_digits(
                    length=random.randint(min_chars, max_chars),
                ),
            )

    def random_letters_digits(self, length=16):
        """返回一随机字母、数字字符串(a-z 、A-Z 、0-9)."""
        return self.fake.random_choices(
            getattr(string, 'letters', string.ascii_letters + string.digits),
            length=length,
        )

    def random_punctuation_str(self, min_chars=0, max_chars=8):
        """返回长度在最大值与最小值之间的随机字符串，只包含英文标点符号"""
        if min_chars is None:
            return "".join(self.random_punctuation(length=max_chars))
        else:
            assert (
                    max_chars >= min_chars), "Maximum length must be greater than or equal to minium length"
            return "".join(
                self.random_punctuation(
                    length=random.randint(min_chars, max_chars),
                ),
            )

    def random_punctuation(self, length=16):
        """返回一随机英文标点符号"""
        return self.fake.random_choices(
            getattr(string, 'letters', string.punctuation),
            length=length,
        )

    @classmethod
    def factory_generate_ids(cls, starting_id=1, increment=1):
        """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """
        def generate_started_ids():
            val = starting_id
            local_increment = increment
            while True:
                yield val
                val += local_increment
        return generate_started_ids

    @classmethod
    def factory_choice_generator(cls, values):
        """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
        def choice_generator():
            my_list = list(values)
            while True:
                yield random.choice(my_list)
        return choice_generator


if __name__ == '__main__':
    g = TestdataGenerator()
    print(g.random_phone_number())
    print(g.random_name())
    print(g.random_address())
    print(g.random_email())
    print(g.random_ipv4())
    print(g.random_str(min_chars=4, max_chars=8))
    print(g.random_int(100000, 999999))
    print(g.random_int(100000, 999999, [125565, 497511, 899392, 875591]))
    print(g.random_letter_digit_str(min_chars=4, max_chars=8))
    print(g.random_letter_digit_str(min_chars=6, max_chars=6))
    print(g.random_punctuation_str(min_chars=4, max_chars=8))
    id_gen = g.factory_generate_ids(starting_id=0, increment=2)()
    for i in range(5):
        print(next(id_gen))

    choices = ['John', 'Sam', 'Lily', 'Rose']
    choice_gen = g.factory_choice_generator(choices)()
    for i in range(5):
        print(next(choice_gen))
