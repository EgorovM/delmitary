# Goods

Ручка товаров магазинов

-----


## Ручка списка товаров /

Параметры запроса:

- :param shop: идентификатор магазина, для которого произойдет поиск по товарам
- :param page: номер страницы для пагинации


Тело ответа:
```
HTTP 200 OK
{
    count*	integer
    next	string($uri)
    previous	string($uri)
    results*	[{
        id	integer
        shop*	integer
        name*	string
        icon	string($uri)
        price*	integer
    }]
}
```

## Ручка товара /shop_id

Тело ответа:
```
{
    id	integer
    shop*	integer
    name*	string
    description*	string
    icon	string($uri)
    price*	integer
}
```

