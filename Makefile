# Release build excludes debug/; dev build adds it and enables SugarCube test mode.
# Playtest build has no debug panel, but prints the run numbers at every ending.
.PHONY: build dev watch playtest package lint test

build: lint
	mkdir -p dist && tweego -o dist/index.html src

dev:
	mkdir -p dist && tweego -t -o dist/dev.html src debug

watch:
	mkdir -p dist && tweego -t -w -o dist/dev.html src debug

playtest: lint
	mkdir -p dist && tweego -o dist/playtest.html src playtest

# itch.io wants a zip with index.html at its root. Upload dist/book-of-answers.zip.
package: build
	rm -rf build && mkdir -p build && cp dist/index.html build/
	cd build && zip -q -X ../dist/book-of-answers.zip index.html

lint:
	python3 scripts/lint.py src debug playtest

test:
	python3 scripts/test_lint.py
