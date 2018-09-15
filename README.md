# disco

Automated musical analysis for party lighting.

## Overview
- After finding the BPM and beat track, we segment the song into measures.
- For each measure, we compute the dominant frequencies, average/min/max power and count the number of onsets.
- We emit a variable number of transitions for each measures (affected primarly by the relative number of onsets), and sync the transitions to said onsets.
- In general, we map power to luminosity, dominant frequencies to color and onset counts to bursts.
