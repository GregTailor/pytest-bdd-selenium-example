from pytest_bdd import scenarios, given, when, then, parsers
from hamcrest import assert_that, equal_to, is_

from pages.welcome_page import WelcomePage
from pages.lets_talk_tea_page import LetsTalkTeaPage

scenarios('../features/send_email.feature')


@given("Let's talk tea page", target_fixture="lets_talk_tea_page")
def lets_talk_tea_page(browser):
    browser.maximize_window()
    page = WelcomePage(browser)
    page.navigate_to_lets_talk_tea_page()
    return LetsTalkTeaPage(browser)


@when(
    parsers.parse(
        'The user is trying to send and email with valid credentials: '
        '(name: "{name}", email: "{email}", subject: "{subject}", message: "{message}")'
    )
)
@when('The user is trying to send and email with valid credentials: '
      '(name: "<name>", email: "<email>", subject: "<subject>", message: "<message>")')
def sending_email(lets_talk_tea_page, name, email, subject, message):
    lets_talk_tea_page.fill_name(name)
    lets_talk_tea_page.fill_email(email)
    lets_talk_tea_page.fill_subject(subject)
    lets_talk_tea_page.fill_message(message)
    lets_talk_tea_page.click_submit()


@then('An error message shows up')
def validate_error_message(lets_talk_tea_page):
    error_message = lets_talk_tea_page.form_error
    assert_that(error_message, is_(equal_to("Error.")))


@then("Email is sent")
def email_is_sent(lets_talk_tea_page):
    error_message = lets_talk_tea_page.email_is_sent_message
    assert_that(error_message, is_(equal_to("Email is sent.")))
