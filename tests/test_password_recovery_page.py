import data
import allure


@allure.suite('Тесты страницы восстановления пароля')
class TestTransitions:
    @allure.title('Переход в раздел "Восстановление пароля"')
    @allure.description('Переходим в личный кабинет, из него переходим на страницу восстановления пароля, '
                        'проверяем успешность перехода')
    def test_go_to_password_recovery(self, header_page, account_page, password_recovery_page):
        header_page.move_to_account()
        assert account_page.get_login_form_text() == data.LOGIN_FORM_TITLE

        account_page.go_to_password_recovery()
        assert password_recovery_page.get_title_text() == data.PASSWORD_RECOVERY_HEADER_TEXT