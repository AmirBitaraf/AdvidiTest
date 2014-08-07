


Feature: Show Top banners for each campaign
Scenario: Campaign with more than 10 banners with conversion
	Given Campaign with id 51
	When I open it
	Then I should see Top-10 Banners


Scenario: Campaign with 7 banners with conversion
	Given Campaign with id 52
	When I open it
	Then I should see Top-7 Banners
Scenario: Campaign with 4 banners with conversion
	Given Campaign with id 53
	When I open it
	Then I should see Top-4 Banners
	Then I should see Top Click Banner
Scenario: Campaign with insufficient clicked banners
	Given Campaign with id 54
	When I open it
	Then I should see a Random Banner
Scenario: Avoid Saturation
	Given Campaign with id 51
	When I open it twice
	Then I shouldn't see equal sequences
