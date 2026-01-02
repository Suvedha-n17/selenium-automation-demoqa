Feature: Validate fields in forms

  Background:
    Given User launches the application
    And the user navigate to "Forms" section
    Then expand "Forms" card
    Then all options should be displayed under "Forms"
      | Options       |
      | Practice Form |
    Then the user selects "Practice Form" section under "Forms"
    Then verify user is navigated to "https://demoqa.com/automation-practice-form" page

  Scenario: TC005_Validate mandatory fields on empty submission
    When the user "submit" the form
    Then the below fields should indicate invalid state
      | FieldName  |
      | firstName  |
      | lastName   |
      | userNumber |

  Scenario Outline: TC006_Validate email and mobile number with invalid format
    When the user provides "<FirstName>" in the "firstName" field
    And the user provides "<LastName>" in the "lastName" field
    And the user provides "<Email>" in the "userEmail" field
    And the user provides "<Mobile>" in the "userNumber" field
    And the user selects Gender as "Male"
    When the user "submit" the form
    Then the below fields should indicate invalid state
      | FieldName  |
      | userEmail  |
      | userNumber |

    Examples:
      | FirstName | LastName | Email             | Mobile     |
      | John      | Doe      | john.doe@invalid  | 1234567    |
      | Alice     | Smith    | alice.smith@.com  | 98765      |
      | Bob       | Brown    | bob.browntest.com | abc1234567 |
      | Eve       | Johnson  | eve@domain        | 12345      |
      | Max       | White    | max@.com          | 0000000    |

  Scenario: TC007_User submits the form successfully with all valid details
    When the user provides "John" in the "firstName" field
    And the user provides "Doe" in the "lastName" field
    And the user provides "john.doe@test.com" in the "userEmail" field
    And the user selects Gender as "Male"
    And the user provides "1234567890" in the "userNumber" field
    And the user provides "Chennai" in the "currentAddress" field
    And the user "submit" the form
    Then a confirmation modal titled "Thanks for submitting the form" should appear
    Then the submission summary should display the following information
      | Label         | Value             |
      | Student Name  | John Doe          |
      | Student Email | john.doe@test.com |
      | Gender        | Male              |
      | Mobile        | 1234567890        |
      | Address       | Chennai           |


