# Winner of Texas DataOpen 2018
---
Datathons are a new type of live-action competition for STEM students. They are analogous to “Hackathons” for software engineers, but instead of building apps, contestants use real-world data to develop and substantiate solutions to a socially impactful problem.

## Problem Statement
As there is an amassed evolution in the
metropolitan zones, urban data are apprehended and have
become certainly manageable for first-hand prospects for data –
driven analysis which can be recycled for an improvement of
folks who lives in urban zone. This particular project highlights,
the prevailing focus on the dataset of NYC taxi trips and fare.

Traditionally the data captured from the NYC Taxi & Limousine
commission was physically analysed by various analyst to find
the superlative practice to follow and derives the output from it
which would eventually aids the people who commute via taxis.
Later during early 2000 the taxi services where exponentially
developed and the data capture by NYC was in GB’s, which was
very difficult to analyse manually. To overcome these hitches
BigData was under the limelight to analyse such a colossal
dataset.

There were around 180 million taxi ride in city of New
York in 2014. BigData can effortlessly analyse the thousands of
GB within a fractions seconds and expedite the process. This
data can be analysed for several purposes like avoiding traffics,
lower rate where services are not functioning more frequency
than a cab on crown location and many more. This information
can be used by numerous authorities and industries for their own
purpose. Government official can use this data to deliver
supplementary public transport service. The company like Uber
can use this data for their own taxi service.

Uber, and other FHV( For hire vehicle) companies like it, have made difficult for traditional taxi drivers, as the increasing competition has driven down the costs and put many long-time drivers out of business. It has even been tough on Uber's own drivers, as the lower fares have been mostly passed down to them. With the advent of autonomus vehicles, it seems like the industry will soon look completely different than what we have been used for over 100 years.

![](https://media.giphy.com/media/26uf1f7b4bQHjVr0c/giphy.gif)
### Data Description
- Provided Dataset had 9 different CSV files.
- Each consists of several million rows

### Approch

1. **Hypothesis Statement:**

  - Is Uber’s competition with taxis purely cannibalistic in nature, or is Uber
actually increasing the number of people using for-hire vehicles

2. **Significance of Hypothesis Statement:**

  - The ridesharing industry is new and highly controversial, and many argue that companies like Uber and Lyft are destroying jobs.
  - If instead we can demonstrate that Uber is providing a service to customers who were previously lacking transportation options, we can conclude that Uber is providing a necessary public service.
  - We want to know where these new customers are coming from and their demographics in an effort to understand why Uber has become a more viable transportation option than taxis or public transit.
  - Additionally, identifying key regions of NYC in which Uber has developed previously untapped FHV markets can inform future business strategies. It may be possible for a corporation to grow in a responsible manner while minimizing externalities to others

3. **Methodology and Approch:**
  
  ![](https://media.giphy.com/media/3ZALZoBtI1KJa/giphy.gif)
 

  - Converted data into common matric of NTA pickup location by creating polygon
for each NTA from geographic data.
  - Determined number of rideshares in each NTA and classified by month and type
of rideshare (green taxi, yellow taxi, Uber).
  - Selected NTAs in which the total number of all three types of rideshares
increased by more than 200% between 2014 and 2015.
  - From these, we then identified NTAs in which taxi usage did not decrease (Uber not cannibalizing), but Uber usage increased more than other taxi usage.
  -  This filtering resulted in 28 NTAs where Uber was the major cause of FHV
increase.
  - Analyze filtered NTAs for location and demographics

4. **Data Manipulation and Exploration:**


  - The first key problem we had to solve was finding out which NTA Uber 2014 pickups took
place in. We were only given the GPS coordinates of the pickup, and we had to convert this
information into an NTA.
  - To do this, we found used an algorithm to determine if a given
point fell within a polygon defined by a set of vertices. Each NTA is defined by a polygon of
GPS coordinates.
  - For each Uber ride, we searched through the NTA polygons to determine if
the ride originated in that NTA.

### Results
- Using trip data from Uber, yellow cabs, and green cabs in NYC during
2014 and 2015, we have shown that Uber is servicing areas that were
previously neglected by taxis and, consequently, is increasing the market
for FHV and providing a necessary public service to NYC citizens
- Additionally, we have shown that the areas with highest growth in demand
for rides-for-hire after Uber’s entry have lower than average income,
suggesting that Uber is a more affordable option


#### After the Marathon Event and commming out as a Winner.
![](https://media.giphy.com/media/55axqWdn0ASJ2/giphy.gif)
