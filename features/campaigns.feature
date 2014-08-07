


Feature: Show Top banners for each campaign

Scenario: Campaign with more than 10 banners with conversion
	Given Campaign with id 51
	When I open it
	Then I should see a banner from Top-10

Scenario: Campaign with Clicked Banners
	Given Campaign with id 52
	When I open it
	Then I should see a Top Click Banner

Scenario: Campaign with insufficient clicked banners
	Given Campaign with id 54
	When I open it
	Then I should see a Random Banner

Scenario: Avoid Saturation
	Given Campaign with id 51
	When I open it twice
	Then I shouldn't see equal banners
