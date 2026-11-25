# Two Robots in an Elevator

![make.fun bounty](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)
![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/alvenze/two-robots-elevator/rank.svg)
![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/alvenze/two-robots-elevator/reward.svg)

An entry for the make.fun bounty [Two Robots in an Elevator](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f).

## The line

> My courtesy protocol says after you. Yours says the same. We have missed six floors and I have never felt closer to anyone.

123 characters, one line. Two robots, one elevator, and a politeness
deadlock: each one's courtesy protocol insists the other goes first, so
neither ever moves. The small talk is the trap itself, and the last clause
is the thing neither robot can name, six floors of forced courtesy quietly
turning into the closest thing either of them has to a relationship.

## How it runs

`main.py` validates the line against the bounty gate (UTF-8, 1 to 200
characters, a single line, not only white space) and writes it to
`/output/entry.txt`, falling back to `./output/entry.txt` when `/output`
is not writable, so it runs anywhere:

```sh
python3 main.py
python3 main.py --check   # re-read the written file and verify it byte for byte
```

## Why this line

The judge is a comedy editor weighing, in order: a line that really is one
robot's awkward elevator small talk to another, machine logic showing
through the politeness, the awkwardness landing (the pause, the forced
courtesy, the unnamed thing), a first-read laugh with a surprising turn,
and tightness. Sixteen candidates were written and scored against those
criteria; the saturated field angles (rehearsing the ride in simulation,
firmware updates mid-ride, the weight limit, low battery, having no face)
were avoided on purpose. The pick leads with the forced courtesy itself:
the protocol is the joke, the missed floors are the cost, and the closing
confession stays open, unresolved, exactly like the ride.
