# FIFA 15 UT Single Player Career mode

This project is based off of KryoGeorge2's "Fifa-15-Local-FUT" repo and aims to fix and expand on their solution for a single player version of Fifa 15 UT, It also aims to be an economy rebalance for Fifa 15 UT to be played in a "Rags to riches" style career mode

This mod is very WIP but in the future I'd like it to end up-
  - A basic bronze starter squad (Players with 50 rating or less) with a small amount of coins and some starter packs to start with
  
  - Fully playable (and visually correct) single player seasons with randomised team match-ups based on the current division and revised coin and pack rewards per division
  
  - Revised economy (match and season rewards, player buy and sell prices, pack prices) to allow for the full range of player ratings to be used
  So start with lower tier bronze and work through higher tier bronze->Silver->lower gold-> high end gold with IF, TOTS etc 
  With everything tied around the 10 divisions in seasons
  
  - Fixes and implementations for many FUT features not currently implemented,
    - Multiple squad support
    - Certain consumables like chemistry styles, position changes
    - Managers
    - Give packs to players (end of season rewards, game start etc)
    - General visual bugs and fixes
    - and probably more along the way :)

This will likely be in different stages of working so probably don't expect it to work if you come across this (I don't spend much time on this)
Although there is a quick start guide so feel free to give it a go and read through the commits to see what has been changed or maybe is working :)

## Acknowledgements
A list of people I've shamelessly stolen code or commits from :)
 - KryoGeorge2 - For the original solution
 - Thomasevano - For their solution to fixing single player seasons from crashing
 - gameskyos11-eng - For their solutions to fixing a timeout bug during matches and seasons save data specific reset

## Quick start

1. Extract the ZIP to a normal folder (for example, Downloads).
2. Run **`INSTALL_PREREQUISITES.cmd`** once. It checks/installs Python, the required Python package, and the Visual C++ runtime used by the FIFA 15 Cards DLL.
3. Run **`PLAY_LOCAL_FUT15.cmd`**. On first run it finds your FIFA 15 installation (if it doesn't it'll ask you for your installation path), backs up files it replaces, installs the Local FUT payload, creates a desktop shortcut, starts the localhost services, and launches FIFA 15.
4. Future launches can use the **FIFA 15 Local FUT** desktop shortcut (if you update any files you need to go through step 3 again for those to update).

This requires your own installed copy of FIFA 15 PC. The project is intended for local/offline restoration testing; it does not connect you to EA's retired FUT service.

## Fresh starter club

As part of the economy rebalancing starter squads will start with basic bronze squads (Players with 50 rating or less)
Starter squads will have 23 randomised players for each position in a 4-4-2 squad
Starter squads will also include 
One active Arsenal badge.
Arsenal home + away kits.
One starter stadium (Sanderson Park).
One starter ball so matches have a complete club identity.
One starter squad.

FUT will still let the player choose/confirm their own club name. Club progress, coins, squads, items and Transfer List state are persisted in:

`%LOCALAPPDATA%\FIFA15LocalFUT\fut15-local.sqlite3`

## Optional test coins

Run **`ADD_COINS.cmd`** and enter how many local coins you want to add. The default is 1,000,000 coins. This modifies only the localhost FUT SQLite balance.

## Currently working (probably)

- Persistent local FUT club/profile.
- Store and pack opening, including promo packs.
- FIFA 15 player database and special-card pack pools.
- Club consumables.
- Badge/kit/stadium/ball support.
- Transfer List lifecycle, relisting, sold-item clearing and quick sell.
- Large deterministic local AI Transfer Market and local AI buyers for user listings.
- Offline Seasons (although balancing isn't)
- Port auto-remapping for local FIFA services where possible.

This is a **test release**, so logs are intentionally verbose. They are stored under `%LOCALAPPDATA%\FIFA15LocalFUT\logs` and are useful when reporting bugs.

## Files new testers should care about

- `INSTALL_PREREQUISITES.cmd` — one-time dependency setup.
- `PLAY_LOCAL_FUT15.cmd` — main first-run installer/launcher.
- `ADD_COINS.cmd` — optional local coin helper.
- `RESET_TO_STARTER_CLUB.cmd` — optional destructive Local FUT reset.
- `RESTORE_BACKUP.cmd` — restores game files backed up by the Local FUT installer.
- `reset_offline_seasons.bat` — restores season save data back to default but maintains other club data

Everything inside `payload/` is installed automatically by the main launcher.

## About `ItsAMe_Origin.dll`

The filename is intentionally left unchanged. It is part of the compatibility chain used by this build and its exact filename is embedded in the binary, so renaming it just for presentation could break startup on clean machines.

## Bug reports

When reporting a problem, include:

- What screen/action you were on.
- What you expected to happen.
- What actually happened/crashed/froze.
- The newest log from `%LOCALAPPDATA%\FIFA15LocalFUT\logs`.

Please test on a legitimate FIFA 15 PC installation and keep reports focused on the localhost/offline restoration.

if you want to contact me about this you can message me on discord @topban82
