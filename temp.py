def analyze_string(input_string):
    letters = sum(c.isalpha() for c in input_string)
    digits = sum(c.isdigit() for c in input_string)
    others = len(input_string) - letters - digits
    return {"letters": letters, "digits": digits, "others": others}

# Пример использования
input_str = "Hello, 123!"
result = analyze_string(input_str)
print(result)
#2
def number_to_text(num):
    numbers = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    tens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    decades = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

    if 10 <= num <= 19:
        return tens[num - 10]
    else:
        return decades[num // 10] + " " + numbers[num % 10]

# Пример использования
num = 42
result = number_to_text(num)
print(result)
#3
def transform_string(input_string):
    result = ""
    for char in input_string:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        elif char.isdigit():
            result += "_"
        else:
            result += char
    return result

# Пример использования
input_str = "Hello, World 123!"
result = transform_string(input_str)
print(result)
#4
def css_to_camelcase(css_style):
    parts = css_style.split("-")
    camelcase = parts[0] + ''.join(word.title() for word in parts[1:])
    return camelcase

# Пример использования
css_style = "font-size"
result = css_to_camelcase(css_style)
print(result)
#5
def create_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

# Пример использования
phrase = "cascading style sheets"
result = create_acronym(phrase)
print(result)
#6
def combine_strings(*args):
    combined_string = ' '.join(args)
    return combined_string

# Пример использования
result = combine_strings("Hello", "World", "from", "Python")
print(result)
#7
def calculator(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except:
        return "Error: Invalid expression"

# Пример использования
expression = "10 + 5 * 2"
result = calculator(expression)
print(result)

from urllib.parse import urlparse
#8
def url_info(url):
    parsed_url = urlparse(url)
    return {
        "Scheme": parsed_url.scheme,
        "Netloc": parsed_url.netloc,
        "Path": parsed_url.path,
        "Params": parsed_url.params,
        "Query": parsed_url.query,
        "Fragment": parsed_url.fragment
    }

# Пример использования
url = "https://itstep.org/ua/about"
result = url_info(url)
print(result)
#9
def split_string(input_string, delimiter):
    substrings = []
    substring = ""
    for char in input_string:
        if char == delimiter:
            substrings.append(substring)
            substring = ""
        else:
            substring += char
    substrings.append(substring)
    return substrings

# Пример использования
input_str = "10/20/2020"
delimiter = "/"
result = split_string(input_str, delimiter)
print(result)