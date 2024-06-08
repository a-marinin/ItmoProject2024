import requests
from bs4 import BeautifulSoup

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square = Rectangle.square(self, width, height)
        self.perimeter = Rectangle.perimeter(self, width, height)

    def square(self, width, height):
        square = width * height
        # return square
        return "The square of the rectangle ({}x{}) is {}.".format(width, height, square)

    def perimeter(self, width, height):
        perimeter = (width + height) * 2
        # return perimeter
        return "The perimetr of the rectangle ({}x{}) is {}.".format(width, height, perimeter)


# rectangle_1 = Rectangle(2, 3)
# rectangle_2 = Rectangle(5, 9)
# rectangle_3 = Rectangle(77, 99)
#
# print('1st rectangle ----> ', rectangle_1.square, rectangle_1.perimeter)
# print('2nd rectangle ----> ', rectangle_2.square, rectangle_2.perimeter)
# print('3rd rectangle ----> ', rectangle_3.square, rectangle_3.perimeter)


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.addition = Math.addition(self, a, b)
        self.multiplication = Math.multiplication(self, a, b)
        self.division = Math.division(self, a, b)
        self.subtraction = Math.subtraction(self, a, b)

    def addition(self, a, b):
        addition = a + b
        return "The addition of 2 numbers ({} and {}) is equal to {}".format(a, b, addition)

    def multiplication(self, a, b):
        multiplication = a * b
        return "The multiplication of 2 numbers ({} and {}) is equal to {}".format(a, b, multiplication)

    def division(self, a, b):
        division = a / b
        return "The division of 2 numbers ({} and {}) is equal to {}".format(a, b, division)

    def subtraction(self, a, b):
        subtraction = a - b
        return "The subtraction of 2 numbers ({} and {}) is equal to {}".format(a, b, subtraction)


# test = Math(25, 5)
# print(test.addition)
# print(test.multiplication)
# print(test.division)
# print(test.subtraction)


class Webpage:
    def __init__(self):
        self.url = "https://demoqa.com/text-box"
        # HTML structure copied from DevTools (because requests doesn't parse the demoqa.com site).
        self.test_html = '<html><head></head>' + '<ul class="menu-list"><li class="btn btn-light active" id="item-0"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M145.2 96l66 746.6L512 928l299.6-85.4L878.9 96H145.2zm595 177.1l-4.8 47.2-1.7 19.5H382.3l8.2 94.2h335.1l-3.3 24.3-21.2 242.2-1.7 16.2-187 51.6v.3h-1.2l-.3.1v-.1h-.1l-188.6-52L310.8 572h91.1l6.5 73.2 102.4 27.7h.4l102-27.6 11.4-118.6H510.9v-.1H306l-22.8-253.5-1.7-24.3h460.3l-1.6 24.3z"></path></svg><span class="text">Text Box</span></li><li class="btn btn-light" id="item-1"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M145.2 96l66 746.6L512 928l299.6-85.4L878.9 96H145.2zm595 177.1l-4.8 47.2-1.7 19.5H382.3l8.2 94.2h335.1l-3.3 24.3-21.2 242.2-1.7 16.2-187 51.6v.3h-1.2l-.3.1v-.1h-.1l-188.6-52L310.8 572h91.1l6.5 73.2 102.4 27.7h.4l102-27.6 11.4-118.6H510.9v-.1H306l-22.8-253.5-1.7-24.3h460.3l-1.6 24.3z"></path></svg><span class="text">Check Box</span></li><li class="btn btn-light" id="item-2"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M145.2 96l66 746.6L512 928l299.6-85.4L878.9 96H145.2zm595 177.1l-4.8 47.2-1.7 19.5H382.3l8.2 94.2h335.1l-3.3 24.3-21.2 242.2-1.7 16.2-187 51.6v.3h-1.2l-.3.1v-.1h-.1l-188.6-52L310.8 572h91.1l6.5 73.2 102.4 27.7h.4l102-27.6 11.4-118.6H510.9v-.1H306l-22.8-253.5-1.7-24.3h460.3l-1.6 24.3z"></path></svg><span class="text">Radio Button</span></li><li class="btn btn-light" id="item-3"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M145.2 96l66 746.6L512 928l299.6-85.4L878.9 96H145.2zm595 177.1l-4.8 47.2-1.7 19.5H382.3l8.2 94.2h335.1l-3.3 24.3-21.2 242.2-1.7 16.2-187 51.6v.3h-1.2l-.3.1v-.1h-.1l-188.6-52L310.8 572h91.1l6.5 73.2 102.4 27.7h.4l102-27.6 11.4-118.6H510.9v-.1H306l-22.8-253.5-1.7-24.3h460.3l-1.6 24.3z"></path></svg><span class="text">Web Tables</span></li><li class="btn btn-light" id="item-4"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M145.2 96l66 746.6L512 928l299.6-85.4L878.9 96H145.2zm595 177.1l-4.8 47.2-1.7 19.5H382.3l8.2 94.2h335.1l-3.3 24.3-21.2 242.2-1.7 16.2-187 51.6v.3h-1.2l-.3.1v-.1h-.1l-188.6-52L310.8 572h91.1l6.5 73.2 102.4 27.7h.4l102-27.6 11.4-118.6H510.9v-.1H306l-22.8-253.5-1.7-24.3h460.3l-1.6 24.3z"></path></svg><span class="text">Buttons</span></li><li class="btn btn-light" id="item-5"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M145.2 96l66 746.6L512 928l299.6-85.4L878.9 96H145.2zm595 177.1l-4.8 47.2-1.7 19.5H382.3l8.2 94.2h335.1l-3.3 24.3-21.2 242.2-1.7 16.2-187 51.6v.3h-1.2l-.3.1v-.1h-.1l-188.6-52L310.8 572h91.1l6.5 73.2 102.4 27.7h.4l102-27.6 11.4-118.6H510.9v-.1H306l-22.8-253.5-1.7-24.3h460.3l-1.6 24.3z"></path></svg><span class="text">Links</span></li><li class="btn btn-light" id="item-6"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M145.2 96l66 746.6L512 928l299.6-85.4L878.9 96H145.2zm595 177.1l-4.8 47.2-1.7 19.5H382.3l8.2 94.2h335.1l-3.3 24.3-21.2 242.2-1.7 16.2-187 51.6v.3h-1.2l-.3.1v-.1h-.1l-188.6-52L310.8 572h91.1l6.5 73.2 102.4 27.7h.4l102-27.6 11.4-118.6H510.9v-.1H306l-22.8-253.5-1.7-24.3h460.3l-1.6 24.3z"></path></svg><span class="text">Broken Links - Images</span></li><li class="btn btn-light" id="item-7"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M145.2 96l66 746.6L512 928l299.6-85.4L878.9 96H145.2zm595 177.1l-4.8 47.2-1.7 19.5H382.3l8.2 94.2h335.1l-3.3 24.3-21.2 242.2-1.7 16.2-187 51.6v.3h-1.2l-.3.1v-.1h-.1l-188.6-52L310.8 572h91.1l6.5 73.2 102.4 27.7h.4l102-27.6 11.4-118.6H510.9v-.1H306l-22.8-253.5-1.7-24.3h460.3l-1.6 24.3z"></path></svg><span class="text">Upload and Download</span></li><li class="btn btn-light" id="item-8"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 1024 1024" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M145.2 96l66 746.6L512 928l299.6-85.4L878.9 96H145.2zm595 177.1l-4.8 47.2-1.7 19.5H382.3l8.2 94.2h335.1l-3.3 24.3-21.2 242.2-1.7 16.2-187 51.6v.3h-1.2l-.3.1v-.1h-.1l-188.6-52L310.8 572h91.1l6.5 73.2 102.4 27.7h.4l102-27.6 11.4-118.6H510.9v-.1H306l-22.8-253.5-1.7-24.3h460.3l-1.6 24.3z"></path></svg><span class="text">Dynamic Properties</span></li></ul>' + '</body></html>'

    def open_web_page(self, url) -> str:  # Opens the web-page with requests lib
        r = requests.get(url).text
        # print(r)  # Prints the content of the web-site, from the passed URL
        return r

    def parse_web_page(self, url):  # Parse the web-page with BeautifulSoup lib
        # soup = self.open_web_page(url)
        soup = BeautifulSoup(self.test_html, 'html.parser')
        texts = soup.findAll(string=True)
        # print(texts)  # Prints all text from buttons


test = Webpage()
# test.open_web_page(url='https://demoqa.com/text-box')
# test.parse_web_page(url='https://demoqa.com/text-box')
test.parse_web_page(url='')


class Button:
    def __init__(self, name):
        self.name = name
        self.type = 'Кнопка'
        self.locator = ''

    def print_button_name(self) -> None:
        return self.name

    def click_button(self) -> str:
        return 'Клик по кнопке {}'.format(self.name)


b1 = Button('Text Box')
b2 = Button('Check Box')
b3 = Button('Radio Button')
b4 = Button('Web Tables')
b5 = Button('Buttons')
b6 = Button('Links')
b7 = Button('Broken Links - Images')
b8 = Button('Upload and Download')
b9 = Button('Dynamic Properties')

# print('Это кнопка "{}". Сейчас мы по ней кликнем: {}'.format(b1.print_button_name(), b1.click_button()))

l = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
for i in range(9):
    print('Это кнопка "{}". Сейчас мы по ней кликнем: {}'.format(l[i].print_button_name(), l[i].click_button()))
