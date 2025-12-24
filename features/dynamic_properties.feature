Feature: Dynamic properties validation

  Background:
    Given User launches the application
    And the user navigate to "Elements" section
    Then expand "Elements" card
    Then verify user is navigated to "https://demoqa.com/elements" page
    Then expand "Elements" card
    Then all options should be displayed under "Elements"
      | Items                 |
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
    Then the user should fluently wait until the button with text "Visible After 5 Seconds" becomes visible

    Scenario: TC004_Load the page and verify that the second button changes color after some time
    Given the user fetches initial "color" of the button
    And the user fluently wait until the button color changes
    And the user fetches the changed "color" of the button
    Then user asserts if the color of the button has been changed