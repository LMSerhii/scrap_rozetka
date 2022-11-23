import json

import requests


def get_data():
    """ """
    import requests

    cookies = {
        'ab_language': 'new',
        'slang': 'ua',
        'uid': 'Cgo8kGNZb9o1OnVN5+DbAg==',
        'delivery': 'new',
        'uss_evoid_cascade': 'yes',
        'ab-catalog-backend': 'old',
        'cart-modal': 'cart-page',
        'ab-auto-portal': 'old',
        'filter-tabs': 'old',
        'ab-catalog-delivery-terms': 'old',
        'ab-catalog-selection-filters': 'old',
        'promo-horizontal-filters': 'splitFilters',
        'ab-catalog-tile-description': 'old',
        'ab-catalog-filter-result-quantity': 'old',
        'ab-kt-action': 'super-offer',
        'fingerprint': 'off',
        'skip-add-phone': 'off',
        'xab_segment': '148',
        '_uss-csrf': 'qOgS7G6XmbsRWyta4Yf6uHt+b0pE8URxjxvSc5ii57y8YFYQ',
        'ussapp': '-jnO_-JA_3j_4auwe_ddB11RnXcVXsOC_eFtZ6nz',
        'visitor_city': '1',
        '_gcl_au': '1.1.82716467.1666805727',
        '_ga': 'GA1.3.1649475729.1666805727',
        'afclid': '7558957401666805727',
        '_fbp': 'fb.2.1666805727628.99665783',
        '__exponea_etc__': 'bc3d4da0-3fd5-4476-a2ce-3a3e2f43486a',
        'social-auth': 'old',
        'fit-size': 'new',
        'ab-catalog-filters-index': 'off',
        'af_source': 'adwords',
        'af_sources': '{"adwords":["1669196740","0"]}',
        'ussat_exp': '1669239941',
        'ussajwt': 'eyJhbGciOiJSUzI1NiIsImtpZCI6InVzc2F0LnYwIiwidHlwIjoiSldUIn0.eyJkZXRhaWxzIjoiYzk1OGM3YzQwZWFhMTlkNjgyMTk2MGIyY2YyOTk2MTg3ZjFhN2U4Yjc3Y2RhYTY4M2JkNThiYjBlZmZlYmY1NzA3MTgwNTFmYTE4MTc0MzU1MThiZDFhYjM5NmJhZGY1NzVkYTMzYjYyMmM0ZTk2NWQ1ZThmODUxMWUzZDliZTYzYmY2NjY0ZGIwN2EyM2JjNWFkMDU2ZDU4OGZjNGM0YjllNjZkZTc0ZWI3YWEwZDc0YTBhNWFiMDAzMGM2ZTQ0MmI4YzMzMjRiNjc4Y2YwZjg5MjE5ZjgyMDg0OWJhNmM1OTg2NjY5MDIzNTFiYjFiYTg0N2ZlYjQwMmVkNWQxMSIsImV4cCI6IjE2NjkyMzk5NDEiLCJ1c3NhdCI6ImFhMWUxYmM1NDljZDQ2ZDUzMzZhZTY4MDU1MjE3Zjk3LnVhLWU2OGRiOTIzZDQxYWViMGRlMjBmODJlY2E3MDM2YTRiLjE2NjkyMzk5NDEifQ.S7Xc0BtKK8OZSUEZmt_4D93EorFVknkkvFNWfx0X8_eZMFpNFNBFXvup5RIIr2tvcxfqPDVsDPWdvmgPo389VKKwk18WV2_9WmY-sLnueibhXhtUiqf9chtGIWEa7Ho_fKerBFbChlhrCc6q30UMB5eDUZ163Cnptk4T7fK-h7kUiAwaNlED7dOGQZuBg6JMWgM5fnBZFEdZmmJF2Qtn8r7rSmYGzU8yuzfOJ0Yx_-UUUroaWLxpQ0GNiLXy9HLWqvAZdxboXt2g1lATdDicTkpXYrxAURysDN6zRwf3fM1PqDxttz2MbTIBTyj6fL0ZesjPg2TAelvaKUkZkhthbA',
        'ussat': 'aa1e1bc549cd46d5336ae68055217f97.ua-e68db923d41aeb0de20f82eca7036a4b.1669239941',
        'ussrt': '38d6a33c0c8777c7d0f860a9b828f539.ua-e68db923d41aeb0de20f82eca7036a4b.1671788741',
        '_gcl_aw': 'GCL.1669189545.CjwKCAiApvebBhAvEiwAe7mHSJzugRq0z8TuD5_gLbIAa2I43ZF7S8um0eNjY4bOUJsas66_6_GhERoCPSsQAvD_BwE',
        '__utmz_gtm': 'utmcsr=google|utmccn=adwords|utmcmd=cpc',
        '_gid': 'GA1.3.2120376417.1669189545',
        '_gac_UA-203518-6': '1.1669189545.CjwKCAiApvebBhAvEiwAe7mHSJzugRq0z8TuD5_gLbIAa2I43ZF7S8um0eNjY4bOUJsas66_6_GhERoCPSsQAvD_BwE',
        '__exponea_time2__': '7200.225232839584',
        'utm_source': 'adwords',
        '_dc_gtm_UA-203518-6': '1',
        '__cf_bm': 'kKTnbO7I810oHXBrnyeYA5yA0QqgG6TY9ptu9EPhtEQ-1669198315-0-AVceCDMaiGbNK3zKCLpd4jPRymykqHGskJ8NmGfvrv7S1Nr31U6uWu5Aw5NC0dV6jKsKpf73zuv+7JV0FovJ6C0=',
    }

    headers = {
        'authority': 'search.rozetka.com.ua',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,zh;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'ab_language=new; slang=ua; uid=Cgo8kGNZb9o1OnVN5+DbAg==; delivery=new; uss_evoid_cascade=yes; ab-catalog-backend=old; cart-modal=cart-page; ab-auto-portal=old; filter-tabs=old; ab-catalog-delivery-terms=old; ab-catalog-selection-filters=old; promo-horizontal-filters=splitFilters; ab-catalog-tile-description=old; ab-catalog-filter-result-quantity=old; ab-kt-action=super-offer; fingerprint=off; skip-add-phone=off; xab_segment=148; _uss-csrf=qOgS7G6XmbsRWyta4Yf6uHt+b0pE8URxjxvSc5ii57y8YFYQ; ussapp=-jnO_-JA_3j_4auwe_ddB11RnXcVXsOC_eFtZ6nz; visitor_city=1; _gcl_au=1.1.82716467.1666805727; _ga=GA1.3.1649475729.1666805727; afclid=7558957401666805727; _fbp=fb.2.1666805727628.99665783; __exponea_etc__=bc3d4da0-3fd5-4476-a2ce-3a3e2f43486a; social-auth=old; fit-size=new; ab-catalog-filters-index=off; af_source=adwords; af_sources={"adwords":["1669196740","0"]}; ussat_exp=1669239941; ussajwt=eyJhbGciOiJSUzI1NiIsImtpZCI6InVzc2F0LnYwIiwidHlwIjoiSldUIn0.eyJkZXRhaWxzIjoiYzk1OGM3YzQwZWFhMTlkNjgyMTk2MGIyY2YyOTk2MTg3ZjFhN2U4Yjc3Y2RhYTY4M2JkNThiYjBlZmZlYmY1NzA3MTgwNTFmYTE4MTc0MzU1MThiZDFhYjM5NmJhZGY1NzVkYTMzYjYyMmM0ZTk2NWQ1ZThmODUxMWUzZDliZTYzYmY2NjY0ZGIwN2EyM2JjNWFkMDU2ZDU4OGZjNGM0YjllNjZkZTc0ZWI3YWEwZDc0YTBhNWFiMDAzMGM2ZTQ0MmI4YzMzMjRiNjc4Y2YwZjg5MjE5ZjgyMDg0OWJhNmM1OTg2NjY5MDIzNTFiYjFiYTg0N2ZlYjQwMmVkNWQxMSIsImV4cCI6IjE2NjkyMzk5NDEiLCJ1c3NhdCI6ImFhMWUxYmM1NDljZDQ2ZDUzMzZhZTY4MDU1MjE3Zjk3LnVhLWU2OGRiOTIzZDQxYWViMGRlMjBmODJlY2E3MDM2YTRiLjE2NjkyMzk5NDEifQ.S7Xc0BtKK8OZSUEZmt_4D93EorFVknkkvFNWfx0X8_eZMFpNFNBFXvup5RIIr2tvcxfqPDVsDPWdvmgPo389VKKwk18WV2_9WmY-sLnueibhXhtUiqf9chtGIWEa7Ho_fKerBFbChlhrCc6q30UMB5eDUZ163Cnptk4T7fK-h7kUiAwaNlED7dOGQZuBg6JMWgM5fnBZFEdZmmJF2Qtn8r7rSmYGzU8yuzfOJ0Yx_-UUUroaWLxpQ0GNiLXy9HLWqvAZdxboXt2g1lATdDicTkpXYrxAURysDN6zRwf3fM1PqDxttz2MbTIBTyj6fL0ZesjPg2TAelvaKUkZkhthbA; ussat=aa1e1bc549cd46d5336ae68055217f97.ua-e68db923d41aeb0de20f82eca7036a4b.1669239941; ussrt=38d6a33c0c8777c7d0f860a9b828f539.ua-e68db923d41aeb0de20f82eca7036a4b.1671788741; _gcl_aw=GCL.1669189545.CjwKCAiApvebBhAvEiwAe7mHSJzugRq0z8TuD5_gLbIAa2I43ZF7S8um0eNjY4bOUJsas66_6_GhERoCPSsQAvD_BwE; __utmz_gtm=utmcsr=google|utmccn=adwords|utmcmd=cpc; _gid=GA1.3.2120376417.1669189545; _gac_UA-203518-6=1.1669189545.CjwKCAiApvebBhAvEiwAe7mHSJzugRq0z8TuD5_gLbIAa2I43ZF7S8um0eNjY4bOUJsas66_6_GhERoCPSsQAvD_BwE; __exponea_time2__=7200.225232839584; utm_source=adwords; _dc_gtm_UA-203518-6=1; __cf_bm=kKTnbO7I810oHXBrnyeYA5yA0QqgG6TY9ptu9EPhtEQ-1669198315-0-AVceCDMaiGbNK3zKCLpd4jPRymykqHGskJ8NmGfvrv7S1Nr31U6uWu5Aw5NC0dV6jKsKpf73zuv+7JV0FovJ6C0=',
        'origin': 'https://rozetka.com.ua',
        'referer': 'https://rozetka.com.ua/ua/seller/instrumentfree/goods/',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

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
    total_pages = response['data']['pagination']['total_pages']
    page_size = response['data']['pagination']['page_size']
    category_name = [category['option_value_name'] for category in response['data']['options'][0]['option_values']]

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

        with open("procraft.json", "w", encoding="utf-8") as file:
            json.dump(response, file, indent=4, ensure_ascii=False)

def main():
    get_data()


if __name__ == '__main__':
    main()