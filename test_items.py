def test_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_element_by_css_selector(" .btn-add-to-basket")

    assert button.is_displayed(), "Кнопка отсутствует"
    assert button.is_enabled(), "Кнопка неактивна"

