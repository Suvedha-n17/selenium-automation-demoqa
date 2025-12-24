Feature: Validate fields in forms

  Background:
    Given User launches the application
    And the user navigate to "Forms" section
    Then expand "Forms" card
    Then all options should be displayed under "Forms"
      | Items         |
      | Practice Form |
    Then the user selects "Practice Form" section under "Forms"
    Then verify user is navigated to "https://demoqa.com/automation-practice-form" page

  Scenario: TC005_Validate mandatory fields on empty submission
    When the user clicks on the "submit" button
    Then the "firstName" field should be highlighted as invalid
    And the "lastName" field should be highlighted as invalid
    And the "userNumber" field should be highlighted as invalid

  Scenario: TC006_Validate email and mobile number field with invalid format
    When the user enters "John" in the "firstName" field
    And the user enters "Doe" in the "lastName" field
    And the user enters "john.doe@invalid" in the "userEmail" field
    And the user selects Gender as "Male"
    And the user enters "1234" in the "userNumber" field
    When the user clicks on the "submit" button
    Then the "userEmail" field should be highlighted as invalid
    And the "userNumber" field should be highlighted as invalid

  Scenario: TC007_User submits the form successfully with all valid details
    When the user enters "John" in the "firstName" field
    And the user enters "Doe" in the "lastName" field
    And the user enters "john.doe@test.com" in the "userEmail" field
    And the user selects Gender as "Male"
    And the user enters "1234567890" in the "userNumber" field
    And the user enters "Chennai" in the "currentAddress" field
    And the user clicks on the "submit" button
    Then a modal with title "Thanks for submitting the form" should be displayed
    Then upon submission modal window should display the following data
      | Label         | Value             |
      | Student Name  | John Doe          |
      | Student Email | john.doe@test.com |
      | Gender        | Male              |
      | Mobile        | 1234567890        |
      | Address       | Chennai           |


