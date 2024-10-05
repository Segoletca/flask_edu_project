# Flask & HTMX

Этап 1:
- Инициализация Flask приложения

Этап 2:
- Установка HTMX

Этап 3:
- Ping
  - On click
  - On shift + click
- Hover
- HTMX:
  - `hx-swap="outerHTML"`
  - `hx-trigger="mouseenter"`
  - `hx-trigger="click[shiftKey]"`

Этап 4:
- Кликер на htmx

Этап 5:
- Встроили кликер на главную страницу

Этап 6:
- Обработка HTMX boosts

Этап 7:
- Список товаров
- Создание товаров через форму

Этап 8:
- Создание через HTMX форму + подгрузка списка
- Добавление через `hx-swap="beforeend"`
- Обработка out of band элементов
- Использование `hx-swap="none"`
- Возвращение нескольких кусков для замены: форма и oob-item

Этап 9:
- Добавление CSRF (из Flask-WTF) защиты
- Обработка формы Flask-WTF для обновления товара

Этап 10:
- Добавление заголовков `hx-headers`
- CSRF exempt

Этап 11:
- Удаление товара 
- Выбор цели:
  - по ближайшему тегу: `hx-target="closest li"`
  - по ближайшему классу: `hx-target="closest .product-item"`