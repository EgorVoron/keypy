# keypy
Small python library for changing keyboard layout (english, russian and armenian)

### Dependencies
* Python3 >= 3.4

### Example
```
from keypy import change_keyboard, reverse_keyboard

print(reverse_keyboard('Ghbvth bcgjkmpjdfybz лунзн',
                       keyboard_lang_1='eng',
                       keyboard_lang_2='rus'))  # Пример использования keypy 

print(change_keyboard('Туц дшикфкн',
                      input_keyboard_lang='rus',
                      output_keyboard_lang='eng'))  # New library

print(change_keyboard('կէեպե ւիտհ արմէնիան լաեոըտ', 
                      output_keyboard_lang='eng'))  # keypy with armenian layout

```
