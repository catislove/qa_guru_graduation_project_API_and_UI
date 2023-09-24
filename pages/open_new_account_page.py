from selene import browser, have, command


class OpenNewAccountPage:

    def open_new_account_page(self):
        browser.open('/parabank/openaccount.htm')
        browser.element('a[href="/parabank/openaccount.htm"]').click()

    def select_account_type(self):
        browser.element('#type').click()
        browser.element('option[value = "1"]').click()

    def select_the_first_existing_account(self):
        browser.element('#fromAccountId').click()
        browser.element('option:nth-child(1)').click()

    def click_open_new_account_button(self):
        browser.element('input[type = "submit"]').click()
        browser.all('.title').element_by(have.exact_text("Congratulations, your account is now open."))