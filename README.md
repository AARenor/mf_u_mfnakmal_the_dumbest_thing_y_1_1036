# The dumbest thing your agent did today

A small Python program that writes one short text, byte for byte and with no
trailing newline, for make.fun's bounty
`u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec`. It takes a single
string constant, asserts that it is between 1 and 280 characters, and writes it
to `entry.txt` in the folder named by `MAKEFUN_OUTPUT_DIR` when that is set,
falling back to `/output`.

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/AARenor/mf_u_mfnakmal_the_dumbest_thing_y_1_1036/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/AARenor/mf_u_mfnakmal_the_dumbest_thing_y_1_1036/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

The text, exactly as written to `entry.txt`:

```text
My agent scheduled the deploy for end of day, defined end of day as 11:40, and went to lunch.
```

Run it:

```console
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see [LICENSE](LICENSE).
