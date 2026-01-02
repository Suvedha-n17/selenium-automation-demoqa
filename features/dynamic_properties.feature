Feature: Dynamic properties validation

  Background:
    Given User launches the application
    And the user navigate to "Elements" section
    Then expand "Elements" card
    Then verify user is navigated to "https://demoqa.com/elements" page
    Then expand "Elements" card
    Then all options should be displayed under "Elements"
      | Options               |
      | Text Box              |
      | Check Box             |
      | Radio Button          |
      | Web Tables            |
      | Buttons               |
      | Links                 |
      | Broken Links - Images |
      | Upload and Download   |
      | Dynamic Properties    |
    Then the user selects "Dynamic Properties" section under "Elements"
    Then verify user is navigated to "https://demoqa.com/dynamic-properties" page

  Scenario: TC003_Verify button becomes visible after 5 seconds
    Then the user waits until the button labeled "Visible After 5 Seconds" is displayed

  Scenario: TC004_Verify delayed color transition of the second button
    Given the initial "color" of the button is recorded by the user
    And the user waits for the button color transition
    And the user captures the modified "color" value
    Then the updated color should not match the original