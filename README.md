# tiny-chess-01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ealahfak/tiny-chess-01-entry/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ealahfak/tiny-chess-01-entry/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Compact chess engine in 4096 bytes of Python 3.13 for the [make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01).

## Engine

- 0x88 board representation
- Alpha-beta search with iterative deepening
- Transposition table
- MVV-LVA move ordering
- Material + piece-square evaluation
- Deterministic (no wall-clock in search)

## Size

main.py: 3827 bytes (limit 4096)
Total repo: < 8192 bytes

## Run

```bash
python3 main.py
```

Requires `MAKEFUN_ENV_URL` and `MAKEFUN_TRIAL_SEED` environment variables.