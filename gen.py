import string
from random import choice


def pass_gen(length: int, *dic_param: int) -> str:
    """make password

    :param length: length of pass
    :param dic_param: args separated by commas : 0 - ascii_lowercase, 1 - ascii_uppercase, 2 - digits, 3 - punctuation, 4 - space
    :return:
        out (str): str of characters from the specified dictionary
    """

    # generating a dictionary for creating a password
    dic = []
    strings = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation,
               ' ']
    for i in set(dic_param):
        dic.extend(strings[i])

    # password generation
    out = ""
    for i in range(length):
        char = choice(dic)
        out = out + char
        # print(f'{char=}')
    return out


def pass_check(pw: str) -> int:
    """check password strength

    :param: pw (str) password
    :return: strength (int): strength of password
    """

    strength = 0

    with open('common.txt', 'r') as f:
        common = f.read().splitlines()
    if pw in common:
        return 0  # pw was found in common passwords

    lowercase = any([1 for i in pw if i in string.ascii_lowercase])
    uppercase = any([1 for i in pw if i in string.ascii_uppercase])
    digits = any([1 for i in pw if i in string.digits])
    punctuation = any([1 for i in pw if i in string.punctuation])
    space = any([1 for i in pw if i == ' '])

    char = [lowercase, uppercase, digits, punctuation, space]

    pw_length = len(pw)
    char_length = char.count(True)
    strength += (pw_length - 1) // 4
    strength += char_length - 1
    # print(f'{pw_length= } \n{char_length= } \n{char= }')

    return strength


if __name__ == '__main__':
    print('ss')
    pw = pass_gen(100, 0, 1, 2, 3, 4)
    print(f'{pw=}')
    print(pass_check(pw))
