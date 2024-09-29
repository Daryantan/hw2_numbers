# hw_12.1
# Очистити текст від html-тегів
# Ваше завдання написати функцію, яка прочитає заданий файл,
# очистить текст від html-тегів і запише цей текст в інший файл.
# html-тег завжди починається з "<" і закінчується на ">" тобто. потрібно видалити ці символи та все, що між ними.
# Функція отримує на вхід два параметри – ім'я файлу, який потрібно очистити, та ім'я файлу,
# куди потрібно записати очищений текст. Ім'я файлу, куди потрібно писати, можна задати за замовчуванням.
# Приклади файлів у вкладенні – файл який потрібно очистити (draft.html) та приклад файлу, який може вийти на виході
# з очищеним текстом (cleaned.txt). Файл draft.html необхідно скачати і покласти поряд з файлом,
# де буде вирішення цієї домашки.
# Додаткове завдання для тих, хто захоче ускладнити рішення - спробуйте прибрати рядки, в яких немає інформації.
# import codecs
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#       with codecs.open(html_file, 'r', 'utf-8') as file:
#            html = file.read()
#####
# import codecs
# import re
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#       with codecs.open(html_file, 'r', 'utf-8') as file:
#            html = file.read()
#            cleaned_text = re.sub(r'<[^>]*>', '', html)
#            cleaned_lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]
#       with codecs.open(result_file, 'w', 'utf-8') as output_file:
#            output_file.write("\n".join(cleaned_lines))
# delete_html_tags('draft.html')



# hw_12.2
# Корзина для покупок
# Створіть клас для опису товару (припустимо, це заділ для інтернет-магазину).
# Як поля товару можете використовувати значення ціни, опис, габарити товару.
# Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# Створіть клас "Покупець". Як поля можна використовувати прізвище,
# ім'я, по батькові, мобільний телефон і т.д.
# Створіть клас "Замовлення". Замовлення може містити кілька товарів,
# причому кількість кожного з товарів може бути різною.
# Замовлення має бути "підв'язане" до користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного виведення інформації про це замовлення.

class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname} "


buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        all_products = ""
        for product, count in self.products.items():
            all_products += f"\n{product.name}: {count} pcs."
        return f"User: {self.user}\nItems:{all_products}\n"

    def get_total(self):
        summ = 0
        for product, count in self.products.items():
            summ += (product.price * count)
        return summ




cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
