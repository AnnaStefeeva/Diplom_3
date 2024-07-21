from pages.base_page import BasePage
import locators.password_recovery_page_locators as locators
import allure


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получение текста заголовка страницы')
    def get_title_text(self):
        return self.get_text_from_element(locators.PASSWORD_RECOVERY_TITLE)
