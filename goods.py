def correctly_print(count: int) -> str:
    a: str = 'товар'
    b: str = 'товара'
    c: str = 'товаров'
    if count == 0:
        return f'{count} {c}'
    elif count % 10 == 1 and count % 100 != 11:
        return f'{count} {a}'
    elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 > 20):
        return f'{count} {b}'
    else:
        return f'{count} {c}'


print(correctly_print(22))
