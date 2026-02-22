@CC-547 @gui @duckduckgo
Feature: DuckDuckGo Search Functionality

  Background:
    Given I navigate to the dashboard at "https://duckduckgo.com"
    And the "duckduckgo_home" page is displayed
    Then the URL should contain "duckduckgo"

  @CC-548 @smoke
  Scenario: Basic Search Verification
    # Handle optional consent if needed (CI depends on IP location)
    And I handle the consent popup

    # Perform Search
    When I type "Selenium" into the "search_input"
    And I press the "ENTER" key on the element "search_input"
    
    # Validation
    Then I should see the "results_container"
    And I wait until the text "Selenium" is visible
    And I should see the "first_result"
    And I should see the text "Selenium"
