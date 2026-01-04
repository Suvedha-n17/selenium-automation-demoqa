Feature: Validate book store module

  Background:
    Given User launches the application
    And the user navigate to "Book Store Application" section
    Then expand "Book Store Application" card
    Then all options should be displayed under "Book Store Application"
      | Options        |
      | Login          |
      | Book Store     |
      | Profile        |
      | Book Store API |

  Scenario: TC008_Validate book list displayed in UI against API
    Then the user selects "Book Store" section under "Book Store Application"
    Then verify user is navigated to "books" page
    When the user retrieves the list of books displayed in the UI
    When the Book Store API should be available
    And the user retrieves the list of books available in the API
    Then the list of books in the UI should match the API response accordingly