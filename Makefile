# Release build excludes debug/; dev build adds it and enables SugarCube test mode.
.PHONY: build dev watch lint test

build: lint
	mkdir -p dist && tweego -o dist/index.html src

dev:
	mkdir -p dist && tweego -t -o dist/dev.html src debug

watch:
	mkdir -p dist && tweego -t -w -o dist/dev.html src debug

lint:
	python3 scripts/lint.py src debug

test:
	python3 scripts/test_lint.py
