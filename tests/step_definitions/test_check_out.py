from pytest_bdd import scenarios, given, when, then
from hamcrest import assert_that, equal_to, is_

from pages.welcome_page import WelcomePage
from pages.check_out_page import CheckOutPage
scenarios('../features/check_out.feature')


@given("Check out page", target_fixture="check_out_page")
def check_out_page(browser):
    browser.maximize_window()
    page = WelcomePage(browser)
    page.navigate_to_check_out_page()
    return CheckOutPage(browser)


@when('The user is trying to place an order with these informations: '
      '(email: "<email>", name: "<name>", address: "<address>", card_type: "<card_type>", card_number: "<card_number>", cardholder_name: "<cardholder_name>", verification_code: "<verification_code>")')
def sending_email(check_out_page, email, name, address, card_type, card_number, cardholder_name, verification_code):
    check_out_page.fill_email(email)
    check_out_page.fill_name(name)
    check_out_page.fill_address(address)
    check_out_page.select_card_type(card_type)
    check_out_page.fill_card_number(card_number)
    check_out_page.fill_cardholder_name(cardholder_name)
    check_out_page.fill_verification_code(verification_code)


@then('An error message shows up')
def validate_error_message(check_out_page):
    error_message = check_out_page.form_error
    assert_that(error_message, is_(equal_to("Error.")))
