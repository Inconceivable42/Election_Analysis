# Election_Analysis

## Project Overview
Module 3 Python
Simulated Colorado Board of Elections election audit of a local congressional election. Goal is to complete the following tasks:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who eceived votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the peracentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

### Resources
- Data Source: election_results.csv
- Software: Python 3.9.7, Visual Studio Code, 1.66.2

### Candidate Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates receiving votes were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes. 
- The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892 votes.

## Challenge Overview
After submission of the candidate analysis, further analysis of the local congressional election was requested by the Colorado Board of Elections employee.

1. Create a list of counties where voting took place.
2. Calculate the number of votes cast in each county.
3. Determine the county where most votes were cast.
4. Calculate the percentage of votes cast in each county as part of all votes.

### Resources
- Data Source: election_results.csv
- Software: Python 3.9.7, Visual Studio Code, 1.66.2

### County Summary
The further analysis of the election shows that:
- As stated above, 369,711 votes were cast in this congressional election. 
- The congressional precinct included:
    - Arapahoe County
    - Denver County
    - Jefferson County
- The proportions of votes across counties were:
    - 10.5% of the votes occurred in Jefferson County with 38,855 votes.
    - 82.8% of the votes occurred in Denver County with 306,055 votes.
    - 6.7% of the votes occurred in Arapahoe County with 24,801 votes.
- Denver County was the county where most votes were cast.

## Challenge Summary
Firstly, we would like to thank the Board of Elections for providing us with extremely clean data. We offer data cleaning when the client is not able to provide such usable data. 

With some changes to the programming script used in this analysis, we could analyze election data from local elections all the way up to presidential elections. For instance, county data can scaled up or down to represent precints or states. By adding voter registration statistics in place of total votes, we can add the percentage of voters in the precinct who voted. Each county could be treated as it's own election, using the script to calculate the percentage of votes in that county going to each candidate. 