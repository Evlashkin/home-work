import shop.sql
#/* my request SQL */

/* Выведите имена и email тех пользователей, которые:
- заказывали продукты, название которых начинается с «Гватемала»;
- имеют почтовый домен верхнего уровня, отличный от ru и su, и при этом имеют упакованный заказ;
- заказывали товары из категории «Кофе без кофеина». */

SELECT
	`user`.name,
    `user`.email
FROM `user`
JOIN `order` ON `order`.`user_id` = user.id
JOIN `order2good` ON `order2good`.order_id = `order`.id
JOIN `good` ON `good`.id = `order2good`.good_id
WHERE `good`.name LIKE 'Гватемала%'
UNION
SELECT
	`user`.name,
    `user`.email
FROM `user`
JOIN `order` ON `order`.user_id = `user`.`id`
JOIN `order_status` ON `order_status`.`id` = `order`.`status_id`
WHERE (`user`.`email` NOT LIKE '%su' OR `user`.`email` NOT LIKE '%ru') AND `order_status`.`name`= 'Упакован'
UNION
SELECT
	`user`.`name`,
    `user`.`email`
FROM `user`
JOIN `order` ON `order`.`user_id` = `user`.id
JOIN `order2good` ON `order2good`.`order_id` = `order`.id
JOIN `good` ON `good`.id = `order2good`.`good_id`
JOIN `good_category` ON `good_category`.`id` = `good`.category_id
WHERE good_category.name = 'Кофе без кофеина'


________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________
/* Task 3.15 */

/* В этом задании вам необходимо выполнить несколько SQL-запросов к базе данных shop.sql:

1. Добавьте при помощи INSERT-запросов четыре новых товара в таблицу `good` с ценами выше 1000 рублей
и ненулевым количеством. Убедитесь, что товары добавлены в таблицу и стали самыми дорогими в этой таблице.

INSERT INTO `good`(`category_id`, `name`, `count`, `price`)
VALUES
(1, "Иван-чай Путятинский", 22, 1001),
(1, "Крапивный сбор Путятинский", 8, 1002),
(1, "Гвоздика-ежевика Путятинская", 12, 1003),
(1, "Прополис Путятинский", 33, 2001)


2. Обнулите количество товаров, цена которых выше 1000 рублей, используя один UPDATE-запрос. В результате выполнения
запроса количество каждого из добавленных вами четырёх товаров должно стать равным нулю.

UPDATE `good`
SET `count`=10
WHERE `price`>1000


3. Повысьте в три раза цену у всех товаров, которые дороже 1000 рублей, используя один UPDATE-запрос. В результате
выполнения запроса у добавленных вами товаров цены, которые были выше 1000 рублей, должны увеличиться в три раза.

UPDATE `good`
SET `price` = `price`*3
WHERE `price`>1000


4. Удалите добавленные вами товары, используя один DELETE-запрос и условие «дороже 1000 рублей». В результате выполнения
запроса все добавленные вами товары должны удалиться. Если вы случайно испортили изначальные данные в таблице, то
можете сначала очистить базу от таблиц и затем заново импортировать в базу исходный дамп, как описано в материале
«Удаление таблиц в phpMyAdmin».*/

DELETE
FROM `good`
WHERE `price`>1000


________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________
/* Task 4.4 */
1. Выведите родительскую категорию, количество элементов в такой категории и столбец со значением «чётное» или «нечётное»
для количества таких элементов.

SELECT
	`category_id`,
    COUNT(*),

    IF(
        COUNT(*) % 2 = 0,
        'EVEN',
        'NOT EVEN'
        ) AS `even`
FROM `good`
GROUP BY `category_id`


2. Выведите идентификатор категории, имя, количество и «статус» товаров, общая стоимость которых не менее 390 000 рублей,
двумя способами: с IF и с CASE.
Определим «статус» как величину, зависящую от самого товара:
Если товар не принадлежит к корневой категории чая, то его статус ‘NOT TEA’.
Если это чай и его более 500 штук, то статус ‘ENOUGH’.
В противном случае ‘NOT ENOUGH’.
2.1
SELECT
	gc.parent_id,
    g.name,
    g.count,
    IF(
        gc.parent_id <> 1,
        "NOT TEA",
        IF(
            gc.parent_id = 1 AND g.count > 500,
            'ENOUGH',
            'NOT ENOUGH'
            )
        ) 'ENOUGH'
FROM `good` g
JOIN `good_category` gc ON gc.id = g.category_id
WHERE g.count * g.price > 39000
GROUP BY gc.id


2.2
SELECT
	gc.parent_id,
    g.name,
    g.count,
    CASE
        WHEN gc.parent_id != 1 THEN 'NOT TEA'
        WHEN gc.parent_id = 1 AND g.count > 500 THEN 'ENOUGH'
        ELSE 'NOT ENOUGH'
    END stat
FROM `good` g
JOIN `good_category` gc ON gc.id = g.category_id
WHERE g.count * g.price > 39000
GROUP BY gc.id




________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________
/* Task 4.6 */
1. Выведите все уникальные почтовые домены верхнего уровня длиной в три символа.

SELECT DISTINCT
	IF(
        CHAR_LENGTH(REPLACE(SUBSTRING(`email`, -3, 3), '.', '')) = 3,
        REPLACE(SUBSTRING(`email`, -3, 3), '.', ''),
        'none'
        ) AS `domain`
FROM `user`



SELECT DISTINCT
	CASE
        WHEN CHAR_LENGTH(REPLACE(SUBSTRING(`email`, -3, 3), '.', '')) = 3
        THEN REPLACE(SUBSTRING(`email`, -3, 3), '.', '')
     END AS `domain`
FROM `user`



SELECT DISTINCT
	REPLACE(SUBSTRING(`email`, -3, 3), '.', '') `domain`
FROM `user`
WHERE CHAR_LENGTH(REPLACE(SUBSTRING(`email`, -3, 3), '.', '')) = 3
ORDER BY `domain`


2. Выведите родительские категории и все товары, входящие в них, а также их количество.
/* Select всех товаров*/
SELECT DISTINCT
	gc2.id,
    gc2.name,
    GROUP_CONCAT(good.name SEPARATOR ', ') `names_of_goods`,
    COUNT(good.name)
FROM good_category
JOIN good_category gc2 ON gc2.id = good_category.parent_id
JOIN good ON good.category_id = good_category.id
GROUP BY gc2.id

/* Select всех категорий товаров*/
SELECT DISTINCT
	gc2.id,
    gc2.name,
    GROUP_CONCAT(good_category.name SEPARATOR ', ') `names_of_categories`,
    COUNT(good_category.name)
FROM good_category
JOIN good_category gc2 ON gc2.id = good_category.parent_id
GROUP BY gc2.id


3. Если вам захочется больше практики, то мы подготовили дополнительную задачу повышенной сложности:
Выведите строки формата ‘Статус заказа номер <order id> пользователя “<user name>” изменился <дата без времени> с
<src status code> на <dst status code>’ для заказов, которые переходили со статусов «Доставлен» на «Оплачен»
и созданных 25 мая 2015 года.

SELECT
	CONCAT(
        'Статус заказа номер ',
        `order`.`id`,
        ' пользователя "'
        `user`.`name`,
        '" изменился ',
        SUBSTRING(`order_status_change`.`time`, 1, 10),
        ' c ',
        `order_status_change`.`src_status_id`,
        ' на ',
        `order_status_change`.`dst_status_id`
        )
FROM `user`
JOIN `order` ON `user`.`id` = `order`.`user_id`
JOIN `order_status_change` ON `order_status_change`.`order_id` = `order`.`id`
JOIN order_status ON `order_status`.`id` = order_status_change.src_status_id
JOIN order_status ON `order_status`.`id` = order_status_change.dst_status_id

WHERE
`order_status_change`.`src_status_id` = 6 AND
`order_status_change`.`dst_status_id` = 7 AND
`order`.`creation_date` >= '2015-05-25' AND
`order`.`creation_date` < '2015-05-26'