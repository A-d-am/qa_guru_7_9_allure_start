import allure
import pytest
from selene import browser, be, have

expected_issue_name = 'Issue for homework tests'
repo_name = 'repo:A-d-am/qa_guru_7_3'

def test_repo_issue_name_only_selene():
    browser.open('/')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo_name).press_enter()
    browser.element('#issues-tab').click()

    # вариант, когда мы знаем айди issue
    browser.element('#issue_4_link').should(have.text(expected_issue_name)).should(be.visible)

    # вариант, когда мы НЕ знаем айди issue

    # browser.all('[aria-label="Issues"]').element_by(have.text(expected_issue_name)).should(be.visible)


def test_repo_issue_name_with_allure_steps():
    with allure.step('Открываем браузер'):
        browser.open('/')

    with allure.step('Нажимаем на поле поиска'):
        browser.element('.header-search-button').click()

    with allure.step('Осуществляем поиск по названию репозитория'):
        browser.element('#query-builder-test').type(repo_name).press_enter()

    with allure.step('Переходим во вкладку Issues'):
        browser.element('#issues-tab').click()

    with allure.step(f'Проверяем, что issue с названием {expected_issue_name} есть в списке'):
        browser.element('#issue_4_link').should(have.text(expected_issue_name)).should(be.visible)


def test_repo_issue_name_with_allure_decorator():
    pass
