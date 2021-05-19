"""Модуль с локаторами элементов."""

from selenium.webdriver.common.by import By


class HeaderPageLocators:
    """Локаторы для Шапки сайта."""

    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn.btn-default.btn-lg")
    LOGO = (By.CSS_SELECTOR, "#logo > h1 > a")
    MENU = (By.CSS_SELECTOR, ".navbar-collapse")
    CART_BUTTON = (By.ID, "cart")
    TOP_LINKS = (By.ID, "top-links")
    SEARCH_FIELD = (By.ID, "search")
    MY_ACCOUNT_LINK = (By.XPATH, '//a[@title = "My Account"]')
    LOGIN_LINK = (By.XPATH, '//a[text() = "Login"]')


class MainPageLocators:
    """Локаторы для Главной страницы."""

    BANNER = (By.CSS_SELECTOR, "#content .swiper-viewport:nth-child(1)")
    BANNER_PAGINATION_BULLETS = (By.CSS_SELECTOR,
                                 ".swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets")
    HEADER_FEATURED = (By.TAG_NAME, "h3")
    CAROUSEL_BRAND = (By.CSS_SELECTOR, "#carousel0.swiper-container-horizontal")
    CAROUSEL_PAGINATION_BULLETS = (By.CSS_SELECTOR,
                                   ".swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets")
    CAROUSEL_PAGINATION_BULLET = (By.CSS_SELECTOR,
                                  '.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets > .swiper-pagination-bullet')
    BANNER_MACBOOK = (By.XPATH, "//div[contains(@class, 'swiper-slide-active')]/img[@alt='MacBookAir']")
    BANNER_IPHONE = (By.XPATH, "//div[contains(@class, 'swiper-slide-active')]/a/img[@alt='iPhone 6']")
    BANNER_BULLET = (By.CSS_SELECTOR, "div.slideshow0 > span.swiper-pagination-bullet")
    FEATURED_PRODUCT_LINK = (By.CSS_SELECTOR, 'h3 + div.row > div > div > div.image > a')
    FEATURED_PRODUCT_NAME = (By.CSS_SELECTOR, 'h3 + div.row > div > div > div.image +  div.caption > h4 > a')
    BRAND_IMAGE_IN_CAROUSEL = (By.CSS_SELECTOR, '#carousel0 .swiper-slide')


class ProductPageLocators:
    """Локаторы для страницы Товара."""

    PRODUCT_HEADER = (By.CSS_SELECTOR, ".btn-group + h1")
    BUTTON_CART = (By.CSS_SELECTOR, "#product > div > #button-cart")
    IMAGES_BLOCK = (By.CLASS_NAME, "thumbnails")
    RATING_BLOCK = (By.CLASS_NAME, "rating")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#tab-description > p")
    MAIN_PRODUCT_IMAGE = (By.XPATH, '//ul[@class="thumbnails"]/li[1]')
    PRODUCT_IMAGE_IN_WINDOW = (By.CSS_SELECTOR, ".mfp-figure")
    TAB_CLASS = (By.XPATH, '//ul[@class="nav nav-tabs"]/li')
    TAB_DESCRIPTION_LINK = (By.XPATH, '//a[@href="#tab-description"]')
    TAB_SPECIFICATION_LINK = (By.XPATH, '//a[@href="#tab-specification"]')
    TAB_REVIEWS_LINK = (By.XPATH, '//a[@href="#tab-review"]')
    ITEM_TITLE = (By.CSS_SELECTOR, ".col-sm-4 > .btn-group + h1")
    LINK_LOGIN_ALERT = (By.CSS_SELECTOR, 'div.alert-success > i + a')
    WISH_LIST_BUTTON = (By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    COMPARE_BUTTON = (By.XPATH, '//div[@class="btn-group"]/button[@data-original-title="Compare this Product"]')
    LINK_COMPARE_ALERT = (By.CSS_SELECTOR, 'div.alert-success > a + a')
    LINK_CART_ALERT = (By.CSS_SELECTOR, 'div.alert-success > a + a')


class CataloguePageLocators:
    """Локаторы для страницы Каталога."""

    BREADCRUMB = (By.CLASS_NAME, "breadcrumb")
    CATALOGUE_HEADER = (By.TAG_NAME, "h2")
    CATALOGUE_IMAGE = (By.CLASS_NAME, "img-thumbnail")
    LEFT_MENU = (By.ID, "column-left")
    BANNER_UNDER_LEFT_MENU = (By.ID, "banner0")
    COMPARE_BUTTON = (By.XPATH,
                      '//button[@data-original-title="Compare this Product"]')
    ALERT_SUCCESS_COMPARE = (By.CSS_SELECTOR, ".alert-success")
    COMPARE_LINK = (By.ID, "compare-total")
    SELECT_SORT = (By.ID, "input-sort")
    ITEM_NAME = (By.CSS_SELECTOR, '.caption > h4 > a')
    ITEM_PRICE = (By.CSS_SELECTOR, '.caption > h4 + p + p.price')
    LOGIN_LINK_IN_ALERT = (By.CSS_SELECTOR, 'div.alert-success > i + a')
    WISH_LIST_BUTTON = (By.XPATH, '//button[@data-original-title="Add to Wish List"]')


class LoginPageLocators:
    """Локаторы для страницы Логина."""

    NEW_CUSTOMER_FORM = (By.CSS_SELECTOR,
                         "#content > .row > .col-sm-6:first-child >.well")
    OLD_CUSTOMER_FORM = (By.CSS_SELECTOR,
                         "#content > .row > .col-sm-6:last-child >.well")
    RIGHT_LIST_MENU = (By.CLASS_NAME, "list-group")
    BUTTON_FOR_NEW_CUSTOMER = (By.CSS_SELECTOR, "a.btn.btn-primary")
    BUTTON_FOR_OLD_CUSTOMER = (By.CSS_SELECTOR, "input.btn.btn-primary")
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, '//input[@value="Login"]')
    FAIL_LOGIN_ALERT = (By.CSS_SELECTOR, "i.fa-exclamation-circle")


class AdminPageLocators:
    """Локаторы для Администраторской страницы."""

    PANEL_HEADING = (By.CLASS_NAME, "panel-heading")
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")
    HELP_BLOCK = (By.CLASS_NAME, "help-block")
    NEED_LOGIN_TEXT = (By.XPATH, "//h1[contains(text(), 'enter your login')]")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".nav > li:nth-child(2) > a")
    LEFT_MENU_CATALOGUE = (By.CSS_SELECTOR, "#menu-catalog > a")
    LEFT_MENU_PRODUCTS = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    PRODUCTS_TABLE = (By.CSS_SELECTOR, ".table-responsive")
    FAIL_LOGIN_ALERT = (By.CSS_SELECTOR, '.alert-danger')


class SearchPageLocators:
    """Локаторы для страницы Поиска."""

    SEARCH_INPUT = (By.ID, "input-search")
    SEARCH_BUTTON = (By.ID, "button-search")
    SELECT_CATEGORY = (By.CSS_SELECTOR, "select.form-control")
    CHECKBOX_CATEGORY = (By.XPATH, "//input[@name='sub_category']")
    CHECKBOX_DESCRIPTION = (By.ID, "description")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-thumb > .image + div > .caption > h4 > a")
    EMPTY_RESULT = (By.CSS_SELECTOR, "h2 + p")


class AccountPageLocators:
    """Локаторы для страницы аккаунта пользователя."""

    WISH_LIST_LINK = (By.XPATH, '//div[@id="content"]/ul[1]/li[4]/a')
    ITEM_NAMES = (By.CSS_SELECTOR, '#content > div > table > tbody > tr >td.text-left > a')


class ComparePageLocators:
    """Локаторы для страницы сравнения."""

    ITEM_NAMES = (By.CSS_SELECTOR, 'h1 + table > tbody > tr > td > a > strong')


class CartPageLocators:
    """Локаторы для страницы корзины."""

    ITEM_NAMES = (By.CSS_SELECTOR, 'form > div.table-responsive > table > tbody > tr >td.text-left > a')
    REMOVE_BUTTONS = (By.XPATH, '//button[@data-original-title="Remove"]')
    TEXT_EMPTY_CART = (By.CSS_SELECTOR, 'h1 + p')
    QUANTITY_INPUT = (By.CSS_SELECTOR, 'div.btn-block > input.form-control')
    QUANTITY_REFRESH_BUTTON = (By.XPATH, '//button[@data-original-title="Update"]')
    UNIT_PRICE = (By.CSS_SELECTOR, 'form > div.table-responsive > table > tbody > tr > td:nth-child(5)')
    TOTAL_PRICE = (By.CSS_SELECTOR, 'form > div.table-responsive > table > tbody > tr > td:nth-child(6)')
