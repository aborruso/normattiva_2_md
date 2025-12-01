# url-lookup Specification

## Purpose
Enable natural language search for Italian legal documents using Exa AI API to automatically find and resolve normattiva.it URLs for conversion.
## Requirements
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
- **THEN** system SHALL use the most relevant match
- **OR** prompt user to choose if interactive mode is available

### Requirement: Exa API Key Configuration
The system SHALL support multiple methods for configuring Exa API key to provide flexibility for different usage patterns.

#### Scenario: CLI Parameter Configuration
- **WHEN** user provides `--exa-api-key` parameter
- **THEN** system SHALL use the provided API key for Exa API calls
- **AND** override any environment variable setting

#### Scenario: Environment Variable Configuration
- **WHEN** EXA_API_KEY environment variable is set
- **THEN** system SHALL use the environment variable for Exa API calls
- **AND** this SHALL be the default configuration method

#### Scenario: Configuration Priority
- **WHEN** both CLI parameter and environment variable are provided
- **THEN** system SHALL prioritize CLI parameter over environment variable
- **AND** provide clear error messages if neither is available

#### Scenario: Missing API Key
- **WHEN** no API key is provided via CLI or environment
- **THEN** system SHALL display informative error message
- **AND** guide user to configure API key using either method

