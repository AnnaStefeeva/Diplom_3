from selenium.webdriver.common.by import By


# Заголовок "Соберите бургер"
CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

# Ингредиент "Флюоресцентная булка R2-D3"
INGREDIENT_ELEM = (By.XPATH, ".//a[@href='/ingredient/{}']")

# Каунтер ингредиента
INGREDIENT_ELEM_COUNTER = (By.XPATH, ".//a[@href='/ingredient/{}']/div[contains(@class, 'counter_counter')]/p")

# Заголовок диалога с деталями об ингредиенте
DETAILS_DIALOG_TITLE = (By.XPATH, './/h2[text()="Детали ингредиента"]')

# Крестик диалога с деталями об ингредиенте
DETAILS_DIALOG_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")

# Корзина для верхней булки
ORDER_BASKET = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")
