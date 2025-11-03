## 1. Research and Planning
- [ ] Research Exa AI API documentation and authentication requirements
- [ ] Analyze current Gemini integration in convert_akomantoso.py
- [ ] Determine Exa API integration approach (direct API calls vs CLI)

## 2. Implementation
- [ ] Add Exa API dependency to setup.py/pyproject.toml
- [ ] Create Exa API client module
- [ ] Replace Gemini CLI calls with Exa API calls in lookup_normattiva_url()
- [ ] Update error handling for Exa API responses
- [ ] Test Exa search functionality with sample queries

## 3. Testing and Validation
- [ ] Update unit tests to mock Exa API instead of Gemini CLI
- [ ] Test end-to-end functionality with real Exa API calls
- [ ] Verify search accuracy and URL extraction
- [ ] Ensure backward compatibility with existing CLI interface

## 4. Documentation and Cleanup
- [ ] Update README.md to reflect Exa dependency instead of Gemini
- [ ] Update installation instructions
- [ ] Remove Gemini-specific documentation
- [ ] Update help text and error messages