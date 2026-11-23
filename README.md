# tiny-chess-01 entry

Compact chess engine in 4096 bytes of Python 3.13.

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