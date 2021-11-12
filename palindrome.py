import re


def palindrome(txt):
    """ Check if txt is palindrome.
        Return true if text is palindrome else false.
    """
    txt = re.sub(r'[^А-яA-z]', '', txt).lower()
    return txt == txt[::-1]


if __name__ == '__main__':
    text1, text2 = 'Да, гневен гад', 'Привет, друг!'
    print(f'text1: {text1} - {palindrome(text1)}')
    print(f'text2: {text2} - {palindrome(text2)}')
