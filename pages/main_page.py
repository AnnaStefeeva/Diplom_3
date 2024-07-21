from pages.base_page import BasePage
import allure
import locators.main_page_locators as locators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получение текста заголовка страницы')
    def get_title_text(self):
        return self.get_text_from_element(locators.CONSTRUCTOR_TITLE)

