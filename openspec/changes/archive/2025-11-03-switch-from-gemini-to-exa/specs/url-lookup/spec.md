## MODIFIED Requirements
### Requirement: Natural Language URL Lookup
The system SHALL accept natural language strings describing legal documents and use Exa AI API to find corresponding normattiva.it URLs for conversion.

#### Scenario: Successful URL Resolution
- **WHEN** user provides a natural language string like "legge stanca"
- **THEN** the system SHALL call Exa AI API with appropriate search query
- **AND** extract the found normattiva.it URL
- **AND** proceed with conversion using the resolved URL

#### Scenario: No URL Found
- **WHEN** Exa AI API cannot find a matching URL
- **THEN** the system SHALL display an informative error message
- **AND** exit without attempting conversion

#### Scenario: Exa API Unavailable
- **WHEN** Exa API is not accessible or authentication fails
- **THEN** the system SHALL display configuration guidance
- **AND** exit with appropriate error code

#### Scenario: Multiple URL Matches
- **WHEN** Exa returns multiple potential URLs
- **THEN** the system SHALL use the most relevant match
- **OR** prompt user to choose if interactive mode is available