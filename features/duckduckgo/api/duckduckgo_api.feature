@CC-545 @api @duckduckgo
Feature: DuckDuckGo API Availability

  Background:
    Given the API base URL is "https://duckduckgo.com"

  @CC-546 @smoke
  Scenario: Verify DuckDuckGo connectivity
    When I send a "GET" request to "/"
    Then the response status code should be 200
    And the response time should be less than 2000 ms
    And the response header "Content-Type" should contain "text/html"
