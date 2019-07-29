from allpairspy import AllPairs
from common.testdata_generator import TestdataGenerator
from common.excel_tools import ExcelTools
from config.config import Config


class TestRegisterDataAllPairs(object):
    """组合生成/api/register接口测试用例数据集"""

    def __init__(self):
        self.g = TestdataGenerator()
        self.parameters1 = list()
        self.parameters2 = list()

    def set_parameters(self):
        invitationcode = [
            '',
            '      ',
            '263 184',
            str(self.g.random_int(10000, 99999)),
            '125565',  # 正确邀请码
            str(self.g.random_int(100000, 999999, [125565, 497511, 899392, 875591])),
            str(self.g.random_int(1000000, 9999999)),
            self.g.random_letter_digit_str(min_chars=6, max_chars=6),
            self.g.random_punctuation_str(min_chars=6, max_chars=6),
            '497511',  # 正确邀请码，玩家
            '899392',  # 正确邀请码，代理
            '875591',  # 后端禁用的验证码
        ]
        username = [
            '',
            '      ',
            '263 184',
            self.g.random_letter_digit_str(min_chars=3, max_chars=3),
            self.g.random_letter_digit_str(min_chars=4, max_chars=4),  # 正确username
            self.g.random_letter_digit_str(min_chars=8, max_chars=8),  # 正确username
            self.g.random_letter_digit_str(min_chars=9, max_chars=9),
            self.g.random_punctuation_str(min_chars=6, max_chars=6),
            self.g.random_name()
        ]
        realname = [
            '',
            '      ',
            '263 184',
            self.g.random_letter_digit_str(min_chars=1, max_chars=20),  # 正确realname
            self.g.random_letter_digit_str(min_chars=21, max_chars=21),
            self.g.random_punctuation_str(min_chars=6, max_chars=6),
            self.g.random_name()  # 正确realname
        ]
        password = [
            '',
            '      ',
            '263 184',
            self.g.random_letter_digit_str(min_chars=5, max_chars=5),
            self.g.random_letter_digit_str(min_chars=6, max_chars=6),  # 正确password
            self.g.random_letter_digit_str(min_chars=16, max_chars=16),  # 正确password
            self.g.random_letter_digit_str(min_chars=17, max_chars=17),
            self.g.random_punctuation_str(min_chars=6, max_chars=6)  # 正确password
        ]
        imgcode = [
            '',
            '    ',
            '26 3',
            '88888888',  # 正确imgcode
            self.g.random_letter_digit_str(min_chars=4, max_chars=4),
            self.g.random_name()
        ]
        sourcetype = [
            '',
            ' ',
            '1',  # 正确sourcetype
            '2',  # 正确sourcetype
            '3',  # 正确sourcetype
            self.g.random_str(min_chars=1, max_chars=1)
        ]
        self.parameters1 = [
            # InvitationCode
            [invitationcode[0], invitationcode[1], invitationcode[2], invitationcode[3], invitationcode[4],
             invitationcode[5], invitationcode[6], invitationcode[7], invitationcode[8], invitationcode[9],
             invitationcode[10], invitationcode[11]],
            # UserName
            [username[0], username[1], username[2], username[3], username[4], username[5], username[6], username[7],
             username[8]],
            # RealName
            [realname[0], realname[1], realname[2], realname[3], realname[4], realname[5], realname[6]],
            # Password
            [password[0], password[1], password[2], password[3], password[4], password[5], password[6], password[7]],
            # ImgCode
            [imgcode[0], imgcode[1], imgcode[2], imgcode[3], imgcode[4], imgcode[5]],
            # SourceType
            [sourcetype[0], sourcetype[1], sourcetype[2], sourcetype[3], sourcetype[4], sourcetype[5]],
        ]
        self.parameters2 = [
            # InvitationCode
            [invitationcode[4], invitationcode[9], invitationcode[10], invitationcode[11]],
            # UserName
            [username[3], username[4], username[5], username[6]],
            # RealName
            [realname[3], realname[4], realname[5], realname[6]],
            # Password
            [password[3], password[4], password[5], password[6], password[7]],
            # ImgCode
            [imgcode[3]],
            # SourceType
            [sourcetype[4]],
        ]

    def is_valid_combination(self, row):
        pass


if __name__ == '__main__':
    test_register = TestRegisterDataAllPairs()
    test_register.set_parameters()
    excel_file = Config().base_path + '/testdata/xlsx/test_register_data.xlsx'
    et = ExcelTools('w', excel_file)
    i = 0
    for i, pairs in enumerate(AllPairs(test_register.parameters1)):
        if isinstance(pairs, list):
            if ((pairs[0] == test_register.parameters1[0][4] or pairs[0] == test_register.parameters1[0][9]
                 or pairs[0] == test_register.parameters1[0][10] or pairs[0] == test_register.parameters1[0][11])
                    and (pairs[1] == test_register.parameters1[1][4] or pairs[1] == test_register.parameters1[1][5])
                    and (pairs[2] == test_register.parameters1[2][3] or pairs[2] == test_register.parameters1[2][6])
                    and (pairs[3] == test_register.parameters1[3][4] or pairs[3] == test_register.parameters1[3][5]
                         or pairs[3] == test_register.parameters1[3][7])
                    and (pairs[4] == test_register.parameters1[4][3])
                    and (pairs[5] == test_register.parameters1[5][2] or pairs[5] == test_register.parameters1[5][3]
                         or pairs[5] == test_register.parameters1[5][4])):
                pairs.append(1)
            else:
                pairs.append(-1)
        print("{:4d}: {}".format(i, pairs))
        et.write_excel(i + 3, 1, pairs[0])
        et.write_excel(i + 3, 2, pairs[1])
        et.write_excel(i + 3, 3, pairs[2])
        et.write_excel(i + 3, 4, pairs[3])
        et.write_excel(i + 3, 5, pairs[4])
        et.write_excel(i + 3, 6, pairs[5])
        et.write_excel(i + 3, 7, pairs[6])

    for j, pairs in enumerate(AllPairs(test_register.parameters2)):
        if isinstance(pairs, list):
            if ((pairs[0] == test_register.parameters2[0][0] or pairs[0] == test_register.parameters2[0][1]
                 or pairs[0] == test_register.parameters2[0][2])
                    and (pairs[1] == test_register.parameters2[1][1] or pairs[1] == test_register.parameters2[1][2])
                    and (pairs[2] == test_register.parameters2[2][0] or pairs[2] == test_register.parameters2[2][3])
                    and (pairs[3] == test_register.parameters2[3][1] or pairs[3] == test_register.parameters2[3][2]
                         or pairs[3] == test_register.parameters2[3][4])
                    and (pairs[4] == test_register.parameters2[4][0])
                    and (pairs[5] == test_register.parameters2[5][0])):
                pairs.append(1)
            else:
                pairs.append(-1)
        print("{:4d}: {}".format(j, pairs))
        i = i + 1
        et.write_excel(i + 3, 1, pairs[0])
        et.write_excel(i + 3, 2, pairs[1])
        et.write_excel(i + 3, 3, pairs[2])
        et.write_excel(i + 3, 4, pairs[3])
        et.write_excel(i + 3, 5, pairs[4])
        et.write_excel(i + 3, 6, pairs[5])
        et.write_excel(i + 3, 7, pairs[6])
