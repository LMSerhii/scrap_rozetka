import csv
import json

import requests

from headers_and_cookies import headers, cookies


def get_data():
    """ """
    with open("data/data.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "Бренд",
                "Категорія",
                "Назва",
                "id",
                "Прайс USD",
                "Прайс UAH",
                "Прайс зі знижкою ",
                "Опис",
                "Посилання на карточку товару",
                "Посилання на зображення",
                "Посилання на відео",
            )
        )

    params = {
        'front-type': 'xl',
        'country': 'UA',
        'lang': 'ua',
        'producer': 'goodluck',
        'owox_id': '120941',
        'name': 'instrumentfree',
    }

    response = requests.get('https://search.rozetka.com.ua/ua/seller/api/v6/', params=params, cookies=cookies,
                            headers=headers).json()

    total_products = response['data']['quantities']['goods_quantity_total_found']
    category_name = [category['option_value_name'] for category in response['data']['options'][0]['option_values']]

    data = {}
    products = []
    count_items = 0
    count_images = 0
    count_videos = 0

    for category in category_name[:1]:

        params = {
            'front-type': 'xl',
            'country': 'UA',
            'lang': 'ua',
            'producer': category,
            'owox_id': '120941',
            'name': 'instrumentfree',
        }

        response = requests.get('https://search.rozetka.com.ua/ua/seller/api/v6/', params=params, cookies=cookies,
                                headers=headers).json()

        goods = response['data']['goods']
        for good in goods:
            id = good['id']

            params = {
                'front-type': 'xl',
                'country': 'UA',
                'lang': 'ua',
                'goodsId': id,
            }

            response = requests.get('https://rozetka.com.ua/api/product-api/v4/goods/get-main', params=params,
                                    cookies=cookies,
                                    headers=headers).json()

            id = response.get("data").get("id")
            title = response.get("data").get("title")
            price = response.get("data").get("price")
            old_price = response.get("data").get("old_price")
            price_pcs = response.get("data").get("price_pcs")
            href = response.get("data").get("href")
            brand = response.get("data").get("brand")
            last_category = response.get("data").get("last_category").get("title")
            images = [image.get("original").get("url") for image in response.get("data").get("images")]
            videos = response.get("data").get("videos")
            description = response.get("data").get("description").get("text")

            products.append(
                {
                    "Бренд": brand,
                    "Категорія": last_category,
                    "Назва": title,
                    "id": id,
                    "Прайс USD": price_pcs,
                    "Прайс UAH": old_price,
                    "Прайс зі знижкою ": price,
                    "Опис": description,
                    "Посилання на карточку товару": href,
                    "Посилання на зображення": images,
                    "Посилання на відео": videos,
                }
            )

            with open("data/data.csv", "a", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        brand,
                        last_category,
                        title,
                        id,
                        price_pcs,
                        old_price,
                        price,
                        description,
                        href,
                        images,
                        videos
                    )
                )
            count_items += 1
            count_images += 1
            count_videos += 1

            print(f"{count_items}/{total_products}")

    data["products"] = products
    data["count_items"] = count_items
    data["count_images"] = count_images
    data["count_videos"] = count_videos

    with open("data/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    get_data()


if __name__ == '__main__':
    main()