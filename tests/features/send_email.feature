Feature: Sending email
  As a user I want to be able to send an email to the Passion Tea Company

  Scenario: filling out form correctly

    Given Let's talk tea page
    When The user is trying to send and email with valid credentials: (name: "Greg", email: "greg@gmail.com", subject: "Tea", message: "Hi I like your tea")
    Then Email is sent

  Scenario: filling out form with incorrect email address

    Given Let's talk tea page
    When The user is trying to send and email with valid credentials: (name: "Greg", email: "Greg", subject: "Tea", message: "Hi I like your tea")
    Then An error message shows up

  Scenario Outline: not filling in all fields

    Given Let's talk tea page
    When The user is trying to send and email with valid credentials: (name: "<name>", email: "<email>", subject: "<subject>", message: "<message>")
    Then An error message shows up

    Examples:
    | name |  email           | subject | message            |
    |      |  greg@gmail.com  |   Tea   | Hi I like your tea |
    | Greg |                  |   Tea   | Hi I like your tea |
    | Greg |  greg@gmail.com  |         | Hi I like your tea |
    | Greg |  greg@gmail.com  |   Tea   |                    |