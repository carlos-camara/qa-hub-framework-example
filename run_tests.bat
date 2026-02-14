@echo off
echo [QA Hub] Running DuckDuckGo GUI Tests...
python -m qa_framework.cli run --path features/duckduckgo/gui/duckduckgo_interaction.feature --tags @smoke --no-capture

echo.
echo [QA Hub] Running DuckDuckGo API Tests...
python -m qa_framework.cli run --path features/duckduckgo/api/duckduckgo_api.feature --tags @smoke --no-capture

pause
