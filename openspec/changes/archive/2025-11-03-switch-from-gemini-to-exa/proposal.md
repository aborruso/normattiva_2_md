## Why
The current implementation uses Gemini CLI for natural language search of legal documents. While functional, switching to Exa AI would provide better search capabilities specifically designed for web search and research tasks. Exa offers more comprehensive and accurate results for finding legal documents on normattiva.it.

## What Changes
- Replace Gemini CLI integration with Exa AI API
- Update the natural language search functionality to use Exa's search capabilities
- Maintain the same CLI interface and user experience
- **BREAKING**: Changes dependency from Gemini CLI to Exa API

## Impact
- Affected specs: url-lookup capability (modify existing implementation)
- Affected code: lookup_normattiva_url() function and related search logic
- New dependency: Exa API instead of Gemini CLI
- User experience: Same interface, potentially improved search accuracy