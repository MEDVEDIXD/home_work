def big_line(line):
    """Принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return str(line).upper()


def two_big_letters(line):
    """Делает заглавными первые буквы каждого слова в строке, поступившей на вход функции"""
    words = str(line).split()
    new_line = []
    for word in words:
        new_line.append(word[:2].upper() + word[2:])
    return ' '.join(new_line)
