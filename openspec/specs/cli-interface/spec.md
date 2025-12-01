# cli-interface Specification

## Purpose
Define command-line interface behavior and entry points for the normattiva2md tool, providing both backward compatibility and clear naming for Italian legal document conversion.

## Requirements
### Requirement: Dual CLI Entry Points
The system SHALL provide both legacy and new command names to ensure backward compatibility while transitioning to more descriptive naming.

#### Scenario: Legacy Command Support
- **WHEN** user runs `akoma2md` command
- **THEN** system SHALL execute the same conversion functionality as `normattiva2md`
- **AND** maintain full feature parity
- **AND** provide identical help text and behavior

#### Scenario: New Preferred Command
- **WHEN** user runs `normattiva2md` command
- **THEN** system SHALL execute conversion functionality
- **AND** this SHALL be the recommended command name
- **AND** all documentation SHALL reference this name

#### Scenario: Package Installation
- **WHEN** user installs package via pip
- **THEN** both `akoma2md` and `normattiva2md` commands SHALL be available
- **AND** both SHALL point to the same main function
- **AND** installation SHALL not require additional configuration

#### Scenario: Help and Version Display
- **WHEN** user runs either command with `--help` or `--version`
- **THEN** system SHALL display appropriate information
- **AND** command name in help SHALL reflect the actual command used
- **AND** version information SHALL be identical for both commands

### Requirement: Command Name Detection
The system SHALL detect the actual command name used to invoke the tool for appropriate display in help and error messages.

#### Scenario: Script Execution
- **WHEN** user runs `python convert_akomantoso.py`
- **THEN** system SHALL display help using `normattiva2md` as command name
- **AND** error messages SHALL reference `normattiva2md`

#### Scenario: Installed Command Execution
- **WHEN** user runs `akoma2md` or `normattiva2md`
- **THEN** system SHALL use the actual command name in output
- **AND** help text SHALL reflect the specific command invoked

#### Scenario: PyInstaller Binary
- **WHEN** user runs standalone binary
- **THEN** system SHALL detect binary name appropriately
- **AND** display correct command name in help and error messages