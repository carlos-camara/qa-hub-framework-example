@gui @duckduckgo
Feature: DuckDuckGo Search Functionality

  Background:
    Given I navigate to the dashboard at "https://duckduckgo.com"
    And the "duckduckgo_home" page is displayed
    Then the URL should contain "duckduckgo"

  @smoke
  Scenario: Basic Search Verification
    # Perform Search
    When I type "QA Hub Framework" into the "search_input"
    And I press the "ENTER" key on the element "search_input"
    
    # Validation
    Then I wait for "2" seconds
    And I should see the text "QA Hub Framework"
