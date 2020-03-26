from dictionaries import *


def translate_char(char, dictionary):
    upper_case = (char != char.lower())
    char = char.lower()
    if dictionary.get(char):
        if upper_case:
            return dictionary[char].upper()
        else:
            return dictionary[char]
    else:
        return char


def choose_dictionary(input_lang, output_lang):
    if input_lang == 'rus':
        if output_lang == 'eng':
            return rus2eng_letters
        elif output_lang == 'arm':
            return rus2arm_letters

    elif input_lang == 'eng':
        if output_lang == 'rus':
            return eng2rus_letters
        elif output_lang == 'arm':
            return eng2arm_letters

    elif input_lang == 'arm':
        if output_lang == 'eng':
            return arm2eng_letters
        elif output_lang == 'rus':
            return arm2rus_letters

    else:
        return None


def identify_char_lang(char):
    char = char.lower()
    if 97 <= ord(char) <= 122:  # a - z interval
        return 'eng'
    if 1072 <= ord(char) <= 1103:  # а - я interval
        return 'rus'
    if 1340 <= ord(char) <= 1395:  # armenian interval
        return 'arm'
    else:
        return None


def identify_string_lang(string=None, idx=0):
    letter = string[idx]
    if idx >= len(string):
        return None
    if ord(letter) < 97:
        return identify_string_lang(string, idx + 1)
    if 97 <= ord(letter) <= 122:  # a - z interval
        return 'eng'
    if 1072 <= ord(letter) <= 1103:  # а - я interval
        return 'rus'
    if 1340 <= ord(letter) <= 1395:  # armenian interval
        return 'arm'


def change_keyboard(string: str, output_keyboard_lang: str, input_keyboard_lang=''):
    lang_list = ['rus', 'eng', 'arm']

    if not input_keyboard_lang:
        detected_lang = identify_string_lang(string)

        if not detected_lang:
            raise ValueError('Unidentified language')
        else:
            input_keyboard_lang = detected_lang

    if input_keyboard_lang == output_keyboard_lang:
        raise ValueError('Input and output languages must be different')

    if (input_keyboard_lang and not (input_keyboard_lang in lang_list)) or (not (output_keyboard_lang in lang_list)):
        raise ValueError(
            f"Input and output languages must be 'rus' (russian), 'eng' (english), or 'arm' (armenian), "
            f"not '{input_keyboard_lang}' and '{output_keyboard_lang}'")

    result = ''
    for char in string:
        dictionary = choose_dictionary(input_keyboard_lang, output_keyboard_lang)
        if not dictionary:
            raise ValueError('Unidentified language')
        translated_char = translate_char(char, dictionary)
        result += translated_char
    return result


def reverse_keyboard(string: str, keyboard_lang_1, keyboard_lang_2):
    if keyboard_lang_1 == keyboard_lang_2:
        raise ValueError('keyboard_lang_1 and keyboard_lang_2 languages must be different')

    result = ''
    for char in string:
        char_lang = identify_char_lang(char)
        if not char_lang:
            result += char
        else:
            if char_lang == keyboard_lang_1:
                dictionary = choose_dictionary(keyboard_lang_1, keyboard_lang_2)
            elif char_lang == keyboard_lang_2:
                dictionary = choose_dictionary(keyboard_lang_2, keyboard_lang_1)
            else:
                raise ValueError(
                    f"keyboard_lang_1 and keyboard_lang_2 must be 'rus' (russian), 'eng' (english), "
                    f"or 'arm' (armenian), not '{keyboard_lang_1}' and '{keyboard_lang_2}'")
            translated_char = translate_char(char, dictionary)
            result += translated_char
    return result
