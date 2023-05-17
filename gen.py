import string
from random import choices


def pass_gen(length: int, *dic_param: int) -> str:
    """make password

    :param length: length of pass
    :param dic_param: args separated by commas : 0 - ascii_lowercase, 1 - ascii_uppercase, 2 - digits, 3 - punctuation, 4 - space
    :return: out (str): str of characters from the specified dictionary
    """

    # generating a dictionary for creating a password
    dic = []
    strings = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation, ' ']
    for i in set(dic_param):
        dic.extend(strings[i])

    # password generation
    out = "".join(choices(dic, k=length))
    return out


def is_common(password: str) -> int:
    """password check for simplicity

    :param password: the string that contains the password
    :return: return 0 if the password in the list of popular passwords
    """
    try:
        file = open('common.txt', 'r')
    except OSError:
        return 0

    with file as f:
        common = f.read().splitlines()
        if password in common:
            return 1  # pw was found in common passwords


def pass_check(password: str) -> int:
    """check password strength

    if password in common passwords return 0

    :param: pw (str) password
    :return: strength (int): strength of password
    """

    # if password in common passwords return 0
    if is_common(password):
        return 0

    strength = 0

    lowercase = any([1 for i in password if i.islower()])
    uppercase = any([1 for i in password if i.isupper()])
    digits = any([1 for i in password if i.isdigit()])
    punctuation = any(
        [1 for i in password if i in string.punctuation])  # the str class doesn't have a built-in ispunctuation method
    space = any([1 for i in password if i.isspace()])

    char = [lowercase, uppercase, digits, punctuation, space]

    pw_length = len(password)
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
