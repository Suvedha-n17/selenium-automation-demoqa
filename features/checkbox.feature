Feature: Checkbox Tree Validation

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
    Then the user selects "Check Box" section under "Elements"
    Then the "Home" checkbox should be displayed

    Scenario: TC001_Dynamically expand the tree at all levels
    Then the user expands the tree at all levels using "Expand all"
    Then all nodes below should be displayed
      | Options        |
      | Desktop        |
      | Notes          |
      | Commands       |
      | Documents      |
      | WorkSpace      |
      | React          |
      | Angular        |
      | Veu            |
      | Office         |
      | Public         |
      | Private        |
      | Classified     |
      | General        |
      | Downloads      |
      | Word File.doc  |
      | Excel File.doc |

  Scenario: TC002_Validate checkbox selection for parent node with child hierarchy
    Then the user expands the tree at all levels using "Expand all"
    Given the user selects the "Home" node in the checkbox tree
    Then all child node under "Home" should be checked
    Then the user de-selects the "Home" node in the checkbox tree
    Then the node "Home" and all its children should be unchecked
    Given the user selects the "WorkSpace" node in the checkbox tree
    Then all child node under "WorkSpace" should be checked
    And all ancestor nodes of "WorkSpace" should be in half-checked state






