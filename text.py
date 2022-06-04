#  Шифр Цезаря

RU_LOWER: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
RU_UPPER: str = RU_LOWER.upper()


def crypt(text: str, key: int, encrypted: bool) -> str:
    def make_shift(alphabet: str, symbol: str, key: int):
        if encrypted:
            shifted_index = (alphabet.index(symbol) + key) % len(alphabet)
        else:
            shifted_index = (alphabet.index(symbol) - key) % len(alphabet)
        return alphabet[shifted_index]

    symbols_list: list[str] = []

    for symbol in text:
        if symbol in RU_LOWER:
            symbol = make_shift(RU_LOWER, symbol, key)
        elif symbol in RU_UPPER:
            symbol = make_shift(RU_UPPER, symbol, key)

        symbols_list.append(symbol)

    return ''.join(symbols_list)


def crypt_file(file_name: str) -> None:
    with open(file_name, encoding="utf-8") as file:
        text = file.read()
        new_text = crypt(text, 10, encrypted=True)

    with open("text_encrypted.txt", 'w', encoding="utf-8") as f:
        f.write(new_text)


def decrypt_file(file_name: str) -> None:
    with open(file_name, encoding="utf-8") as file:
        text = file.read()
        new_text = crypt(text, 10, encrypted=False)

    with open("text_decrypted.txt", 'w', encoding="utf-8") as file:
        file.write(new_text)


crypt_file("Text.txt")
decrypt_file("text_encrypted.txt")
