# Repository Guidelines

## Project Structure & Module Organization
- `convert_akomantoso.py` is the CLI and XML→Markdown pipeline; keep new parsing helpers near `process_article`.
- `resources/` and `test_data/` hold reference outputs and fixtures; stash oversized XMLs outside Git and log their source in `LOG.md`.
- Distribution artifacts live in `build/`, `dist/`, and `akoma2md.spec`; rebuild via the Makefile, never tweak binaries directly.
- `logs/`, `LOG.md`, and `VERIFICATION.md` capture experiments—update them whenever behaviour shifts.

## Build, Test, and Development Commands
- `python convert_akomantoso.py INPUT.xml OUTPUT.md` runs the converter directly; use it for quick iteration.
- `make build` performs a clean PyInstaller build into `dist/akoma2md`; rerun after packaging changes.
- `make install` installs the editable package (console script `akoma2md`) into the active virtualenv.
- `make test` runs smoke tests; ensure `20050516_005G0104_VIGENZA_20250130.xml` sits in the repo root.
- `./build_distribution.sh` chains clean, build, tests, and optional wheel creation for release candidates.

## Coding Style & Naming Conventions
- Follow PEP 8: 4-space indentation, snake_case for functions, UPPER_SNAKE_CASE for constants.
- Keep the converter dependency-free; add libraries only if justified in `setup.py`.
- Provide brief docstrings for shared helpers and explain non-obvious regexes or XPath selectors with inline comments.
- When adding CLI options, expose both positional and named flags through `argparse` to preserve compatibility.

## Testing Guidelines
- Add deterministic XML samples under `test_data/` and record their provenance; avoid bundling restricted texts.
- Extend `test_compatibility.sh` or build pytest cases that assert Markdown fragments for known inputs.
- Run `make test` before pushing and log intentional diffs in `VERIFICATION_TASKS.md`.

## Commit & Pull Request Guidelines
- History follows Conventional Commits (`feat:`, `chore:`); keep concise subjects and explain impacts in the body.
- Reference tickets in the PR, include before/after Markdown snippets, and list new fixtures or commands.
- Request review once `make test` passes; call out missing fixtures or skipped checks for reviewer parity.

## Data Handling & Security Notes
- Normattiva sources may expose sensitive annotations; scrub personal data before committing samples.
- Avoid hard-coding credentials or local paths; prefer environment variables and document new settings in `README.md`.
