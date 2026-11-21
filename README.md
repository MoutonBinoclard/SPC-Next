# SPC Next
A complete rewrite of Super Python Calculator, aiming for better performance and consistency


# Dictionary formatting

## `rounds`

```python
[
    {
        "53F9EFB9912B04AE": {
            "pID": 1,
            "Player": "Mouton Binoclard on TTV",
            "SquadID": -1,
            "TeamID": -1,
            "Kills": 0,
            "Placement": 21,
            "TrueScore": 21
        },
    }
]
```

`rounds` is a list containing one dictionary per round. Each round dictionary uses
the player's PlayFab ID as its key and contains:

- `pID`: The player's numeric ID.
- `Player`: The player's display name.
- `SquadID`: The squad ID, or `-1` when squads are not used.
- `TeamID`: The team ID, or `-1` when teams are not used.
- `Kills`: The number of kills in that round.
- `Placement`: The player's placement in that round.
- `TrueScore`: The score calculated for that round.