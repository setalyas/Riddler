### Solution to 03/01/2020 Riddler Express

[Question](https://fivethirtyeight.com/features/can-you-solve-the-vexing-vexillology/): _Each of the images below is a different nation’s flag in which the pixels have been randomly rearranged. Can you figure out which flag is which?_

This uses Python to:

1. Scrape all country flags from the [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/docs/flagsoftheworld.html)
2. Decompose each flag into a colour breakdown.
3. Compare the decompositions for the flags and the scrambled images.
4. Output the matching flags.