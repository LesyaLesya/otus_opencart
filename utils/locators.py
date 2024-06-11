"""Модуль с локаторами элементов."""


class AlertsLocators:
    """Локаторы алертов."""

    LINK_LOGIN_ALERT = ("css selector", 'i + a')
    LINK_ALERT = ("css selector", 'a + a')
    DANGER_ALERT = ("css selector", '.alert.alert-danger.alert-dismissible')
    SUCCESS_ALERT = ("css selector", 'div.alert-success')


class HeaderPageLocators:
    """Локаторы для Шапки сайта."""

    SEARCH_INPUT = ("name", 'search')
    SEARCH_BUTTON = ("css selector", '.btn.btn-default.btn-lg')
    LOGO = ("css selector", '#logo > a')
    MENU = ("css selector", '.navbar-collapse')
    CART_BUTTON = ("css selector", '#cart > button.btn-block')
    TOP_LINKS = ("id", 'top-links')
    SEARCH_FIELD = ("id", 'search')
    MY_ACCOUNT_LINK = ("xpath", '//a[@title = "My Account"]')
    LOGIN_LINK = ("xpath", '//a[text() = "Login"]')
    CURRENCY_DROP_DOWN_BUTTON = ("css selector", '.pull-left button.dropdown-toggle')
    CURRENCY_VALUES_BUTTONS = ("css selector", '.pull-left button.dropdown-toggle + ul > li > button')
    CURRENCY_DROP_DONW = ("css selector", '.pull-left button.dropdown-toggle + ul')
    DROPDOWN_FOR_DESKTOPS = ("xpath", '//a[text()="Desktops"]//following-sibling::div')
    COMPONENTS_FOR_DROPDOWN = ("xpath", '//a[text()="Components"]//following-sibling::div')
    LAPTOPS_FOR_DROPDOWN = ("xpath", '//a[text()="Laptops & Notebooks"]//following-sibling::div')
    DESKTOPS_IN_MENU = ("xpath", '//a[text()="Desktops"]')
    COMPONENTS_IN_MENU = ("xpath", '//a[text()="Components"]')
    LAPTOPS_IN_MENU = ("xpath", '//a[text()="Laptops & Notebooks"]')
    SHOPPING_CART_TOP_LINK = ("css selector", 'a[title="Shopping Cart"]')
    WISH_LIST_LINK = ("css selector", '#wishlist-total')
    BREADCRUMB = ("class name", 'breadcrumb')


class MainPageLocators:
    """Локаторы для Главной страницы."""

    BANNER = ("css selector", '#content .swiper-viewport:nth-child(1)')
    BANNER_PAGINATION_BULLETS = (
        "css selector", '.swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets')
    HEADER_FEATURED = ("tag name", 'h3')
    CAROUSEL_BRAND = ("css selector", '#carousel0.swiper-container-horizontal')
    CAROUSEL_PAGINATION_BULLETS = (
        "css selector", '.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets')
    CAROUSEL_PAGINATION_BULLET = (
        "css selector", '.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets > .swiper-pagination-bullet')
    BANNER_MACBOOK = ("xpath", '//div[contains(@class, "swiper-slide-active")]/img[@alt="MacBookAir"]')
    BANNER_IPHONE = ("xpath", '//div[contains(@class, "swiper-slide-active")]/a/img[@alt="iPhone 6"]')
    BANNER_BULLET = ("css selector", 'div.slideshow0 > span.swiper-pagination-bullet')
    FEATURED_PRODUCT_LINK = ("css selector", 'h3 + div.row > div > div > div.image > a')
    FEATURED_PRODUCT_NAME = ("css selector", 'h3 + div.row > div > div > div.image +  div.caption > h4 > a')
    BRAND_IMAGE_IN_CAROUSEL = ("css selector", '#carousel0 .swiper-slide')


class ProductPageLocators:
    """Локаторы для страницы Товара."""

    PRODUCT_HEADER = ("css selector", '.btn-group + h1')
    BUTTON_CART = ("css selector", '#product > div > #button-cart')
    IMAGES_BLOCK = ("class name", 'thumbnails')
    RATING_BLOCK = ("class name", 'rating')
    PRODUCT_DESCRIPTION = ("css selector", '#tab-description > p')
    MAIN_PRODUCT_IMAGE = ("xpath", '//ul[@class="thumbnails"]/li[1]')
    PRODUCT_IMAGE_IN_WINDOW = ("css selector", '.mfp-figure')
    TAB_CLASS = ("xpath", '//ul[@class="nav nav-tabs"]/li')
    TAB_DESCRIPTION_LINK = ("xpath", '//a[@href="#tab-description"]')
    TAB_SPECIFICATION_LINK = ("xpath", '//a[@href="#tab-specification"]')
    TAB_REVIEWS_LINK = ("xpath", '//a[@href="#tab-review"]')
    WISH_LIST_BUTTON = ("xpath", '//button[@data-original-title="Add to Wish List"]')
    COMPARE_BUTTON = ("xpath", '//div[@class="btn-group"]/button[@data-original-title="Compare this Product"]')
    WRITE_REVIEW_BUTTON = ("xpath", '//a[text()="Write a review"]')
    REVIEW_NAME_FIELD = ("id", 'input-name')
    REVIEW_FIELD = ("id", 'input-review')
    RATING_RADIO_BUTTON = ("name", 'rating')
    REVIEW_BUTTON = ("css selector", 'div.pull-right > #button-review')
    RIGHT_BLOCK_INFO = ("xpath", '//div[@class="col-sm-4"]/ul[@class="list-unstyled"]')
    ELEMENTS_OF_RIGHT_BLOCK_INFO_FIRST = ("xpath", '//div[@class="col-sm-4"]/ul[@class="list-unstyled"][1]/li')
    ELEMENTS_OF_RIGHT_BLOCK_INFO_SECOND = ("xpath", '//div[@class="col-sm-4"]/ul[@class="list-unstyled"][2]/li')
    PRODUCT_PRICE = ("xpath", '//div[@class="col-sm-4"]/ul[@class="list-unstyled"][2]/li/h2')


class CataloguePageLocators:
    """Локаторы для страницы Каталога."""

    CATALOGUE_HEADER = ("tag name", 'h2')
    CATALOGUE_IMAGE = ("class name", 'img-thumbnail')
    LEFT_MENU = ("id", 'column-left')
    BANNER_UNDER_LEFT_MENU = ("id", 'banner0')
    COMPARE_BUTTON = (
        "xpath", '//button[@data-original-title="Compare this Product"]')
    COMPARE_LINK = ("id", 'compare-total')
    SELECT_SORT = ("id", 'input-sort')
    ITEM_NAME = ("css selector", '.caption > h4 > a')
    ITEM_PRICE = ("css selector", '.caption > h4 + p + p.price')
    WISH_LIST_BUTTON = ("xpath", '//button[@data-original-title="Add to Wish List"]')
    ITEM_CART = ("css selector", 'div.row > div.product-layout')
    LIST_VIEW_BUTTON = ("id", 'list-view')
    GRID_VIEW_BUTTON = ("id", 'grid-view')
    ADD_TO_CART_BUTTON = ("xpath", '//div[@class="button-group"]/button[1]')
    DESKTOPS_IN_LEFT_MENU = ("partial link text", 'Desktops (')
    LAPTOPS_IN_LEFT_MENU = ("partial link text", 'Laptops & Notebooks (')
    COMPONENTS_IN_LEFT_MENU = ("partial link text", 'Components (')
    TABLETS_IN_LEFT_MENU = ("partial link text", 'Tablets (')
    SOFTWARE_IN_LEFT_MENU = ("partial link text", 'Software (')
    PHONES_IN_LEFT_MENU = ("partial link text", 'Phones & PDAs (')
    CAMERAS_IN_LEFT_MENU = ("partial link text", 'Cameras (')
    MP3_IN_LEFT_MENU = ("partial link text", 'MP3 Players (')


class LoginPageLocators:
    """Локаторы для страницы Логина."""

    NEW_CUSTOMER_FORM = (
        "css selector", '#content > .row > .col-sm-6:first-child >.well')
    OLD_CUSTOMER_FORM = (
        "css selector", '#content > .row > .col-sm-6:last-child >.well')
    CONTINUE_BUTTON = ("css selector", 'a.btn.btn-primary')
    EMAIL_INPUT = ("id", 'input-email')
    PASSWORD_INPUT = ("id", 'input-password')
    LOGIN_BUTTON = ("xpath", '//input[@value="Login"]')


class RegisterPageLocators:
    """Локаторы для страницы Регистрации."""

    HEADER = ("css selector", 'div#content > h1')
    TEXT_FOR_LOGIN = ("css selector", 'div#content > p')
    FIRST_NAME_FIELD = ("css selector", 'input#input-firstname')
    LAST_NAME_FIELD = ("css selector", 'input#input-lastname')
    EMAIL_FIELD = ("css selector", 'input#input-email')
    TEL_FIELD = ("css selector", 'input#input-telephone')
    PASSW_FIELD = ("css selector", 'input#input-password')
    CONFIRM_FIELD = ("css selector", 'input#input-confirm')
    SUBSCRIBE_RADIO = ("css selector", '[name="newsletter"]')
    PRIVACY_POLICY = ("css selector", '.buttons > .pull-right')
    CONTINUE_BUTTON = ("css selector", '[type="submit"]')
    RIGHT_MENU = ("css selector", 'div.list-group')
    AGREE_CHECKBOX = ("css selector", '[name="agree"]')
    FIRST_NAME_ERROR = ("css selector", '#input-firstname + .text-danger')
    LAST_NAME_ERROR = ("css selector", '#input-lastname + .text-danger')
    EMAIL_ERROR = ("css selector", '#input-email + .text-danger')
    TEL_ERROR = ("css selector", '#input-telephone + .text-danger')
    PASSWORD_ERROR = ("css selector", '#input-password + .text-danger')
    CONFIRM_ERROR = ("css selector", '#input-confirm + .text-danger')


class AdminPageLocators:
    """Локаторы для Администраторской страницы."""

    PANEL_HEADING = ("class name", 'panel-heading')
    USERNAME_INPUT = ("id", 'input-username')
    PASSWORD_INPUT = ("id", 'input-password')
    LOGIN_BUTTON = ("css selector", 'button.btn.btn-primary')
    HELP_BLOCK = ("class name", 'help-block')
    NEED_LOGIN_TEXT = ("xpath", '//h1[contains(text(), "enter your login")]')
    LOGOUT_BUTTON = ("css selector", '.nav > li:nth-child(2) > a')
    LEFT_MENU_CATALOGUE = ("css selector", '#menu-catalog > a')
    LEFT_MENU_PRODUCTS = ("css selector", '#collapse1 > li:nth-child(2) > a')
    PRODUCTS_TABLE = ("css selector", '.table-responsive')


class SearchPageLocators:
    """Локаторы для страницы Поиска."""

    SEARCH_INPUT = ("id", 'input-search')
    SEARCH_BUTTON = ("id", 'button-search')
    SELECT_CATEGORY = ("css selector", 'select.form-control')
    CHECKBOX_CATEGORY = ("xpath", '//input[@name="sub_category"]')
    CHECKBOX_DESCRIPTION = ("id", 'description')
    PRODUCT_NAME = ("css selector", '.product-thumb > .image + div > .caption > h4 > a')
    EMPTY_RESULT = ("css selector", 'h2 + p')


class AccountRightBlockLocators:
    """Локаторы для правого блока страницы аккаунта."""

    LOGIN_RIGHT_BLOCK = ("xpath", '//div[@class="list-group"]/a[contains(text(), "Login")]')
    REGISTER_RIGHT_BLOCK = ("xpath", '//div[@class="list-group"]/a[contains(text(), "Register")]')
    LOGOUT_RIGHT_BLOCK = ("xpath", '//div[@class="list-group"]/a[contains(text(), "Logout")]')
    EDIT_ACCOUNT_RIGHT_BLOCK = ("xpath", '//div[@class="list-group"]/a[contains(text(), "Edit Account")]')
    MY_ACCOUNT_RIGHT_BLOCK = ("xpath", '//div[@class="list-group"]/a[contains(text(), "My Account")]')
    RIGHT_LIST_MENU = ("class name", 'list-group')


class LogoutPageLocators:
    """Локаторы для страницы логаута аккаунта пользователя."""

    TEXT_AFTER_LOGOUT = ("css selector", 'h1 + p')


class WishlistPageLocators:
    """Локаторы для страницы вишлиста аккаунта пользователя."""

    ITEM_NAMES = ("css selector", '#content > div > table > tbody > tr >td.text-left > a')
    EMPTY_WISHLIST_TEXT = ("css selector", 'h2 + p')
    REMOVE_BUTTON = ("css selector", 'a.btn-danger')


class EditAccountPageLocators:
    """Локаторы для страницы редактирования аккаунта пользователя."""

    SUBMIT_BUTTON = ("css selector", 'input[type="submit"]')
    FIRSTNAME_FIELD = ("css selector", '#input-firstname')
    LASTNAME_FIELD = ("css selector", '#input-lastname')
    EMAIL_INPUT = ("css selector", '#input-email')
    TELEPHONE_INPUT = ("css selector", '#input-telephone')
    BACK_BUTTON = ("css selector", 'a.btn-default')


class ComparePageLocators:
    """Локаторы для страницы сравнения."""

    ITEM_NAMES = ("css selector", 'h1 + table > tbody > tr > td > a > strong')
    REMOVE_BUTTON = ("css selector", 'a.btn-danger')
    TEXT_FOR_EMTY_COMPARE = ("css selector", '#content > h1 + p')
    ADD_TO_CART_BUTTON = ("css selector", 'input[value="Add to Cart"]')


class CartPageLocators:
    """Локаторы для страницы корзины."""

    ITEM_NAMES = ("css selector", 'form > div.table-responsive > table > tbody > tr >td.text-left > a')
    REMOVE_BUTTONS = ("xpath", '//button[@data-original-title="Remove"]')
    TEXT_EMPTY_CART = ("css selector", 'h1 + p')
    QUANTITY_INPUT = ("css selector", 'div.btn-block > input.form-control')
    QUANTITY_REFRESH_BUTTON = ("xpath", '//button[@data-original-title="Update"]')
    UNIT_PRICE = ("css selector", 'form > div.table-responsive > table > tbody > tr > td:nth-child(5)')
    TOTAL_PRICE = ("css selector", 'form > div.table-responsive > table > tbody > tr > td:nth-child(6)')
    CONTINUE_SHOPPING_BUTTON = ("css selector", 'div.pull-left > a.btn.btn-default')


class FooterPageLocators:
    """Локаторы для подвала."""

    LINKS = ("css selector", 'footer div.col-sm-3 > ul.list-unstyled > li > a')
