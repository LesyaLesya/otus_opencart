import pytest
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.comparison_page import ComparisonPage
from pages.catalogue_page import CataloguePage
from pages.cart_page import CartPage
from pages.admin_page import AdminPage
from pages.account_page import AccountPage, EditAccountPage, LoginPage, LogoutPage, RegisterPage, WishlistPage
from pages.common.footer import Footer
from pages.common.header import Header
from pages.common.alert import Alert
from utils.db.db_helper import DBHelper


class BaseTest:
    search_page: SearchPage
    product_page: ProductPage
    main_page: MainPage
    comparison_page: ComparisonPage
    catalogue_page: CataloguePage
    cart_page: CartPage
    admin_page: AdminPage
    login_page: LoginPage
    account_page: AccountPage
    logout_page: LogoutPage
    register_page: RegisterPage
    wishlist_page: WishlistPage
    edit_account_page: EditAccountPage
    footer: Footer
    header: Header
    alert: Alert
    db: DBHelper

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        # request.cls.browser = browser
        # request.cls.db_connection = db_connection

        request.cls.db = DBHelper

        request.cls.search_page = SearchPage(browser)
        request.cls.product_page = ProductPage(browser)
        request.cls.main_page = MainPage(browser)
        request.cls.comparison_page = ComparisonPage(browser)
        request.cls.catalogue_page = CataloguePage(browser)
        request.cls.cart_page = CartPage(browser)
        request.cls.admin_page = AdminPage(browser)
        request.cls.login_page = LoginPage(browser)
        request.cls.account_page = AccountPage(browser)
        request.cls.logout_page = LogoutPage(browser)
        request.cls.register_page = RegisterPage(browser)
        request.cls.wishlist_page = WishlistPage(browser)
        request.cls.edit_account_page = EditAccountPage(browser)
        request.cls.footer = Footer(browser)
        request.cls.header = Header(browser)
        request.cls.alert = Alert(browser)
