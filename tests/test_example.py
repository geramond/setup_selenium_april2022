def test_first(driver):
    # Перейти к приложению opencart
    driver.get("http://192.168.0.15:8081/")
    # Проверить заголовок
    assert "Your Store" == driver.title

