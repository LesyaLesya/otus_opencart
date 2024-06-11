"""Модуль с путями страниц."""

import os
from dotenv import load_dotenv

load_dotenv()


class Links:
    HOST = f'http://{os.getenv("HOST")}'
    SEARCH_PAGE = f'{HOST}/index.php?route=product/search'
    PRODUCT_PAGE = lambda self, path=None: f'{Links.HOST}{path}' if path else f'{Links.HOST}/index.php?route=product/product&path=18&product_id=47'
    LOGIN_PAGE = f'{HOST}/index.php?route=account/login'
    CATALOGUE_PAGE = f'{HOST}/index.php?route=product/category&path=18'
    ADMIN_PAGE = f'{HOST}/admin/'
    REGISTER_PAGE = f'{HOST}/index.php?route=account/register'
    CART_PAGE = f'{HOST}/index.php?route=checkout/cart'
    LOGOUT_PAGE = f'{HOST}/index.php?route=account/logout'
    EDIT_ACCOUNT_PAGE = f'{HOST}/index.php?route=account/edit'
