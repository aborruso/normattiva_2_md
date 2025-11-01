# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Akoma2MD** is a CLI tool that converts XML documents in Akoma Ntoso format (legal documents from normattiva.it) to readable Markdown. The tool is designed to produce LLM-friendly output for building legal AI bots.

## Core Architecture

### Main Components

- `convert_akomantoso.py`: Core converter (Akoma Ntoso XML → Markdown)
  - Uses only Python standard library (no external deps)
  - Entry point: `main()` function
  - Key function: `convert_akomantoso_to_markdown_improved(xml_path, md_path)`
  - Text extraction: `clean_text_content(element)` handles inline formatting, refs, and modifications
  - Article processing: `process_article(article_element, markdown_list, ns)` handles paragraphs and lists

- `fetch_from_url.py`: **Recommended** URL-based fetcher (requires `requests`)
  - Downloads documents directly from normattiva.it page URLs
  - Extracts parameters from HTML (dataGU, codiceRedaz, dataVigenza)
  - Uses session-based requests to maintain cookies
  - Downloads Akoma Ntoso XML and converts to Markdown
  - Entry point: `main()` with argparse CLI

- `fetch_normattiva.py`: Alternative fetcher (requires `tulit` library)
  - Downloads documents from normattiva.it API
  - Requires specific parameters (not URL-based)
  - Converts to Markdown or JSON
  - Entry point: `main()` with argparse CLI

- `setup.py`: Package configuration for PyPI distribution

### XML Processing

The converter handles Akoma Ntoso 3.0 namespace: `http://docs.oasis-open.org/legaldocml/ns/akn/3.0`

Document structure extraction:

- Title: `//akn:docTitle`
- Preamble: `//akn:preamble`
- Body: `//akn:body` → chapters → sections → articles → paragraphs → lists
- Articles: `//akn:article` with `akn:num` (number) and `akn:heading` (title)
- Legislative modifications: wrapped in `(( ))` from `<ins>` and `<del>` tags

## Common Development Tasks

### Running the converter from URL (recommended)

```bash
# Convert directly from normattiva.it URL
python fetch_from_url.py "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2022;53" -o output.md

# Download XML only
python fetch_from_url.py "URL" --xml-only -o document.xml

# Keep XML after conversion
python fetch_from_url.py "URL" -o output.md --keep-xml
```

### Running the converter from local XML

```bash
# Direct Python execution
python convert_akomantoso.py input.xml output.md

# Using installed package
akoma2md input.xml output.md

# With named arguments
akoma2md -i input.xml -o output.md
```

### Alternative: Fetching with specific parameters

```bash
# Requires: pip install tulit
python fetch_normattiva.py --dataGU YYYYMMDD --codiceRedaz CODE --dataVigenza YYYYMMDD --output file.md --format markdown
```

### Testing

```bash
# Basic test with sample data
python convert_akomantoso.py test_data/20050516_005G0104_VIGENZA_20250130.xml test_output.md
```

### Building executable

```bash
pip install pyinstaller
pyinstaller --onefile --name akoma2md convert_akomantoso.py
```

### Package installation

```bash
# CLI tool installation (recommended)
uv tool install .

# Development mode (requires venv)
pip install -e .

# From source (requires venv)
pip install .
```

## Key Design Decisions

### Markdown Output Format

- Articles: `# Art. X - Title`
- Chapters: `## Chapter Title`
- Sections: `### Section Title`
- Numbered paragraphs: `1. Text content`
- Lists: Markdown bullet lists with `- a) item text`
- Legislative changes: Wrapped in `((modified text))`

### Text Cleaning

- Removes excessive whitespace and indentation
- Preserves inline formatting (bold, emphasis)
- Extracts text from `<ref>` tags
- Prevents double-wrapping of `(( ))` in modifications
- Filters out horizontal separator lines (`----`)

## Project Constraints

- **Zero external dependencies** for core converter (convert_akomantoso.py)
- Python 3.7+ compatibility
- CLI must support both positional and named arguments
- Output must be LLM-friendly Markdown
