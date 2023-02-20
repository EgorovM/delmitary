# Delmitary

Cервис доставки/заказа товаров для жителей общежитий

То есть клиенты смогут договориться с сожителями общежития привезти товар/еду из ближайших магазинов за символическую плату прямо до двери команты.

Есть несколько ролей: курьер, заказчик, администратор сайта. Заказчики имеют доступ к списку магазинов и их товаров, могут добавлять их в корзину. После набора корзины клиент оставляет запрос.

Курьерам предоствляется доступ к списку заказов c именами/телефонами/описаниями/корзинами, где они смогут решить какой заказ брать или не брать вообще

Наполнением и актуализацией информации занимаются администраторы сервиса

У всех ролей есть возможность редактировать личную информацию, помимо этого у курьеров есть график работы (смены) доставки товаров. Администратор может уточнять и редактировать информацию курьеров/клиентов.

## Как мы работаем?

1. Сначала берем задачку из пула задач (Not Started), нужно отметить себя как Engineers, переводим в работу (In Progress)
2. Отводим свою ветку в гитхабе (Если мы были в другой ветке, то не забываем сначала перейти на main ветку)

```bash
git checkout -b <branch_name>
```

1. Делаем свои дела, добавляем измененные файлы и коммитим

```bash
git add .
git commit -m "сообщение"
git push
```

1. Создаем новый PR (Pull Request), чтобы коллега посмотрел на изменения и, если что вернул обратно в работу, или отметил, что ревью пройдено
2. Затем если нужно проводится тестирование решения, после этого можно заливать в главную ветку
