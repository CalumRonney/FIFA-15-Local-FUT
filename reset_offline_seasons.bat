@echo off
setlocal
set "PORT=8199"
set "URL=http://127.0.0.1:%PORT%/ut/game/fifa15/season/offline/reset?divisionId=10"

echo ============================================
echo FIFA 15 Local FUT - Reset Offline Seasons
echo ============================================
echo.
echo This resets ONLY the current offline Seasons progress:
echo   Division 10, 0 points, 0 games, 0 W/D/L, 0 goals.
echo It does NOT reset your club, players, coins, or all-time record.
echo.
pause

REM Prefer the server's own reset endpoint when the server is running.
where curl.exe >nul 2>&1
if %errorlevel%==0 (
    curl.exe --fail --silent --show-error --max-time 5 "%URL%" > "%TEMP%\fifa15_seasons_reset_response.txt" 2>nul
    if %errorlevel%==0 (
        echo.
        echo Offline Seasons reset successfully through the running server.
        type "%TEMP%\fifa15_seasons_reset_response.txt"
        del "%TEMP%\fifa15_seasons_reset_response.txt" >nul 2>&1
        echo.
        pause
        exit /b 0
    )
)

REM If the server is not running, reset the same SQLite keys directly.
REM Make a backup first so the save can be restored if needed.
set "DB=%LOCALAPPDATA%\FIFA15LocalFUT\fut15-local.sqlite3"
if not exist "%DB%" set "DB=%USERPROFILE%\AppData\Local\FIFA15LocalFUT\fut15-local.sqlite3"

if not exist "%DB%" (
    echo ERROR: Could not find the FIFA 15 Local FUT database.
    echo Expected: "%DB%"
    echo.
    pause
    exit /b 1
)

copy /Y "%DB%" "%DB%.bak" >nul
if errorlevel 1 (
    echo ERROR: Could not create database backup.
    pause
    exit /b 1
)

echo.
echo Server endpoint was not available; resetting the SQLite save directly...

python -c "import sqlite3,json,sys; db=r'%DB%'; c=sqlite3.connect(db); keys={'offline_season_division':10,'offline_season_points':0,'offline_season_round':0,'offline_season_wins':0,'offline_season_draws':0,'offline_season_losses':0,'offline_season_goals_for':0,'offline_season_goals_against':0,'offline_season_active':False,'offline_season_wire_round':1,'offline_season_wire_data':'','offline_season_wire_progress_data':'','awaiting_post_match_season_save':False,'offline_match_pending':False,'last_match_end_response':{}}; c.executemany('INSERT INTO kv(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',[(k,json.dumps(v)) for k,v in keys.items()]); c.commit(); c.close(); print('Reset complete: Division 10, 0 points, 0 games, 0 W/D/L, 0 goals.')"
if errorlevel 1 (
    echo.
    echo ERROR: The SQLite reset failed. Your original database is still backed up at:
    echo "%DB%.bak"
    pause
    exit /b 1
)

echo.
echo Offline Seasons reset successfully.
echo Backup created at:
echo "%DB%.bak"
echo.
pause
exit /b 0
