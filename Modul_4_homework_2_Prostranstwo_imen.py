a = 'Я вообще не в области видимости функции test_function'
def test_function():
    a = 'Я в области видимости функции test_function раз'
    def inner_function():
     #   a = 'Я не в области видимости функции test_function'
        print(a)

    inner_function()
a = 'Я в области видимости функции test_function два'
test_function()