Feature: Check out
  As a user I want to be able place my order

  Scenario Outline: invalid field values

    Given Check out page
    When The user is trying to place an order with these informations: (email: "<email>", name: "<name>", address: "<address>", card_type: "<card_type>", card_number: "<card_number>", cardholder_name: "<cardholder_name>", verification_code: "<verification_code>")
    Then An error message shows up

    Examples:
    | email           | name | address                        | card_type  | card_number         | cardholder_name | verification_code |
    | asd             | Greg | 1234, Test city, Test street 1 | Mastercard | 1234-5678-9101-1121 | Greg Test       | 123               |
    | valid@gmail.com |      | 1234, Test city, Test street 1 | Mastercard | 1234-5678-9101-1121 | Greg Test       | 123               |
    | valid@gmail.com | Greg | invalid                        | Mastercard | 1234-5678-9101-1121 | Greg Test       | 123               |
    | valid@gmail.com | Greg | 1234, Test city, Test street 1 | TestCard   | 1234-5678-9101-1121 | Greg Test       | 123               |
    | valid@gmail.com | Greg | 1234, Test city, Test street 1 | Mastercard | test_number         |                 | 123               |
    | valid@gmail.com | Greg | 1234, Test city, Test street 1 | Mastercard | 1234-5678-9101-1121 | Greg Test       | num               |
