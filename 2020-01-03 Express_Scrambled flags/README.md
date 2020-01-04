### Solution to 03/01/2020 Riddler Express

[Question](https://fivethirtyeight.com/features/can-you-solve-the-vexing-vexillology/): _Each of the images below is a different nation’s flag in which the pixels have been randomly rearranged. Can you figure out which flag is which?_

This uses Python to:

1. Scrape all country flags from the [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/docs/flagsoftheworld.html)
2. Decompose each flag into a colour breakdown, using a [k-d tree approach](https://stackoverflow.com/a/50545735)
3. Compare the decompositions for the flags and the scrambled images.
4. Output the matching flags.

Results:

Scrambled | Cleaned up
--------- | ----------
![Flag 1](https://raw.githubusercontent.com/setalyas/Riddler/master/2020-01-03%20Express_Scrambled%20flags/Outputs/1.png) | ![French flag](https://raw.githubusercontent.com/setalyas/Riddler/master/2020-01-03%20Express_Scrambled%20flags/Outputs/1FR.gif)
![Flag 2](https://raw.githubusercontent.com/setalyas/Riddler/master/2020-01-03%20Express_Scrambled%20flags/Outputs/2.png) | ![Brazil flag](https://raw.githubusercontent.com/setalyas/Riddler/master/2020-01-03%20Express_Scrambled%20flags/Outputs/2BR.gif)
![Flag 3](https://raw.githubusercontent.com/setalyas/Riddler/master/2020-01-03%20Express_Scrambled%20flags/Outputs/3.png) | ![Namibia flag](https://raw.githubusercontent.com/setalyas/Riddler/master/2020-01-03%20Express_Scrambled%20flags/Outputs/3WA.gif)
