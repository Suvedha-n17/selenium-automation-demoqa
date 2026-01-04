Feature: Dynamic properties validation

  Background:
    Given User launches the application
    And the user navigate to "Elements" section
    Then expand "Elements" card
    Then verify user is navigated to "elements" page
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

  Scenario: TC003_Verify button becomes visible after 5 seconds
    Then verify user is navigated to "dynamic properties" page
    Then the user waits until the button labeled "Visible After 5 Seconds" is displayed
    And all dynamic property buttons should be present on the page
      | Options                 |
      | Will enable 5 seconds   |
      | Color Change            |
      | Visible After 5 Seconds |

  Scenario Outline:TC004_Verify delayed color transition for dynamic buttons
    Then verify user is navigated to "dynamic properties" page
    Given the initial "color" of the "<button_name>" button is recorded by the user
    And the user waits for the "<button_name>" button color transition
    And the user captures the modified "color" value for the "<button_name>" button
    Then the updated color should not match the original

    Examples:
      | button_name  |
      | Color Change |
