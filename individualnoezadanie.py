#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Название продукта: ")
            shop = input("Название магазина: ")
            price = float(input("Стоимость: "))

            product = {
                'name': name,
                'shop': shop,
                'price': price,
            }

            products.append(product)
            if len(products) > 1:
                products.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Продукт",
                    "Магазин",
                    "Цена"
                )
            )
            print(line)

            for idx, product in enumerate(products, 1):
                print(
                    '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                        idx,
                        product.get('name', ''),
                        product.get('shop', ''),
                        product.get('price', 0)
                )
            )
            print(line)

        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=1)
            productName = parts[1]

            count = 0

            for product in products:
                if productName == product.get('name', productName):
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, product.get('shop', ''))
                    )

                if count == 0:
                    print("Такой продукт не найден")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить продукт;")
            print("list - вывести список продуктов;")
            print("select <продукт> - запросить информацию о продукте;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
