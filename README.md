# Election Analysis

## Overview of Election Audit
It is our job to help Steve determine the results from a recent local congressional election. Our tasks include calculating the total number of votes cast, finding and listing the candidates in the election, which is three in this case, calculating the number of votes and percentage of votes each candidate received, and finally, determining the winner based on the popular vote. An additional task is to break down the election results by the three counties, calculating the number of votes coming from each county and finding which county had the largest turnout of voters.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election show that:

- There were 369,711 total votes cast in the election.
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - 10.5% of voters were from Jefferson county with 38,855 voters
  - 82.8% of voters were from Denver county with 306,055 voters
  - 6.7% of voters were from Arapahoe county with 24,801 voters
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 of votes
  - Diana DeGette received 73.8% of the vote and 272,892 of votes
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 of votes
- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote and 272,892 votes
  
  ![Screen Shot 2022-10-22 at 7 45 04 AM](https://user-images.githubusercontent.com/112633146/197337174-c296e891-761e-43bc-8a18-77e5aecac316.png)


## Election Audit Summary
The amazing thing about programming is that once there is a general design for the code, it can be applied to almost anything with a likewise structure. In this case, our election analysis program would work for any other election, with a few modifications.

During the pandemic, there was much controversy over voting in person versus mailing in ballots. If someone wanted to calculate the number and percentage of votes that were in person or mailed in, a similar format with coding would be followed. A list, dictionary, string variable, and an integer variable must be made first. Then, we would have to go through the data row by row to collect the "in person" data from the appropriate column, just like our other analyses. Then, we would begin adding to our list the information from the "in person" variable data. For either the "in person" or "mailed in" option of our data, we would add a vote count for that specific item. We could then calculate the number and percentages of votes that were in person and mailed in.

There are many other demographics regarding elections that we could analyze using this structure. If we wanted to observe data from a federal election, we could easily find the number and percentage of votes that came from each state. This is very similar to the "county" calculation that we found in our local election analysis, so simply changing the variable names to match states would suffice. Instead of just looking at the highest state turnout in regards to number of votes, we could also look at the lowest turnout, which might be interesting to see.
