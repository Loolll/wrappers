Создание дополнительных фильтров используемых в django templates:
    1)Создать дирректорию в папке любого приложения: templatetags
    2)Название фильтра должно совпадать с названием модуля 'somefilter.py'
        подключение в template:
            {% load 'somefilter' %}
        использовать:
            {% input|kwarg %}
        somefilter.py:
            from django import template
            register = template.Library()

            @register.filter
            def somefilter(input, kwarg):
                return something
    3)Пример в templatetags:
        Нахождение index'a элемента