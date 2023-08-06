@echo off

set /p message="Commit message: "
set message=%message:-=Update%

python templates.py
git add .
git commit -m "%message%"
git push

echo.
echo Update complete!
