import pytest
from selene import browser, be, have

expected_issue_name = 'Issue for homework tests'


def test_repo_issue_name_only_selene():
    browser.open('/')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('repo:A-d-am/qa_guru_7_3').press_enter()
    browser.element('#issues-tab').click()

    # вариант, когда мы знаем айди issue
    browser.element('#issue_4_link').should(have.text(expected_issue_name)).should(be.visible)

    # вариант, когда мы НЕ знаем айди issue

    # browser.all('[aria-label="Issues"]').element_by(have.text(expected_issue_name)).should(be.visible)
