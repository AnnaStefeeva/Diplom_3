import data
import allure


@allure.suite('Тесты главной страницы')
class TestsMainPage:
    @allure.title('Открытие окна информации об ингредиенте')
    @allure.description('Кликаем на ингредиенте, проверяем, что появилось окно с деталями')
    def test_open_ingredient_details_window(self, main_page):
        main_page.click_on_ingredient(data.INGREDIENT_HASH)

        assert main_page.get_ingredient_details_header() == data.INGREDIENT_DETAILS_HEADER_TEXT

    @allure.title('Закрытие окна информации об ингредиенте')
    @allure.description('Кликаем на ингредиенте, проверяем, что появилось окно с деталями, '
                        'закрываем окно: проверяем, что оно закрыто')
    def test_close_ingredient_details_window(self, main_page):
        main_page.click_on_ingredient(data.INGREDIENT_HASH)

        main_page.wait_ingredient_details_window()
        main_page.close_ingredient_details_window()

        assert main_page.wait_ingredient_details_window_is_closed()

    @allure.title('Увеличение счётчика ингредиента')
    @allure.description('Перетаскиваем ингредиент в корзину, проверяем, что увеличился счётчик данного ингредиента')
    def test_close_ingredient_details_window(self, main_page):
        counter = main_page.get_ingredient_counter_value(data.INGREDIENT_HASH)
        assert counter == 0

        main_page.add_ingredients_to_order(data.INGREDIENT_HASH)

        counter = main_page.get_ingredient_counter_value(data.INGREDIENT_HASH)
        assert counter == 2 # верх и низ бургера
