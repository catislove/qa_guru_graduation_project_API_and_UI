from selene import browser


def login():
    browser.open("/parabank/index.htm?ConnType=JDBC")
    browser.element('input[name="username"]').type('john')
    browser.element('input[name="password"]').type('demo')
    browser.element('input[value="Log In"]').click()

def logout():
    browser.element('a[href="/parabank/logout.htm"]').click()