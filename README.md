# capstone 1

## Introduction 
The recent Covid crisis has not only created a health crisis, but also an economic one. Rising unemployment and concurrent supply and demand shocks has put a strain on the US economy and financial system. The US Federal Reserve periodically does stress testing on banks twice a year to ensure their stability largely in part due to the 2008 crisis fallout. Regional banks with holdings 100 billion to 250 billion have been given an exemption for 2021.  

The goal of this study is to examine the filings of Texas Capital One Bank (TCBI) and its quarterly/annual filings in an effort to understand their current stress levels and weaknesses.  Texas Capital One Bank was chosen because of its location.  Due to the shale industry in the permian basin being particularly affected by Covid, and more recently a weather freeze incapacitating a large portion of Texas' energy grid, a close examination of one of the largest banks in Texas was chosen. 

## Methods
Holding companies with assets greather than $10 Billion USD are required to file reports with the Federal Reservere and those reports are posted quarterly on the [Federal Financial Institutions Examination Council](https://www.ffiec.gov/)  Analysis was done on the csv file posted on the FFIEC website with code found in SRC folder.

## Results

[Figure1.1]
    <div align="center">
      <img src="images/TCBI_net_income.png">
    </div>

<br>
Dramatic drop off in Net Income for 2020 

[Figure1.2]
    <div align="center">
      <img src="images/TCBI_PG_assets_by_percent.png">
    </div>

<br>

Loan Portfolio (Assets) of Texas Capital One

[Figure1.3]
    <div align="center">
      <img src="images/TCBI_net_income_per_average_asset.png">
    </div>

<br>

Income per Asset. This indicates that large assets are producing small quantities of income relative to other Banks

[Figure1.4]
    <div align="center">
      <img src="images/Loan_loss_provision_loan_loss.png">
    </div>

<br>
[Figure1.5]

<div class = 'row'>
    <div class = 'column'>
    <img src="images/Cap_one_provisions&_losses.png" width="250" height="200" >
    <img src="images/JPM_provisions&_losses.png" width="250" height="200">
    </div>
    <div class="column">
    </div>
    <div class="column">
        <img src="images/GS_provisions&_losses.png" width="250" height="200">
         <img src="images/citigroup_provisions&_losses.png" width="250" height="200">
    </div>
</div>

[Figure2.0]
    <div align="center">
      <img src="images/net_CI_loan_lo.png">
    </div>

<br>

[Figure2.1]
    <div align="center">
      <img src="images/CI_loans_30_89_late.png">
    </div>

<br>

Indicates that the TCBI has a larger portion of loans that are in early phases of non-performance

## Conclusions
It does seem that TCBI has been significantly less profitable in 2020, and their non-performing loans have grown relative to 2019, but they have also allocated a larger portion of their assets to loan loss provisions and short term highly-liquid positions.  Without a full test-suite and understanding of bank fundamentals, I believe the only thing we can say with some certainy is that TCBI is under a larger degress of financial stress than 2019.                   

This analysis does have the underpinnings of a proof of concept of a quarterly analysis and vizualizations of FFIEC filings. With the code in the SRC folder, it does seem possible to get a course view of the current state of a bank relative to its previous position and potentially its peer group.
  

## Future Directions
Ideally, a more comprehensive test and analysis of the filings would be made.  Also, I would like to automate the inputs to only have the csv file read in and the current quarter date as inputs and have the scripts run and return graphs and alaysis to make scalability and portability to other banks better.

## Acknowledgements
DSI Denver Immersive staff/cohort  
kayla Thomas  
Jess Curley  
Chris Reger  
Ian Hetterich  
Travis Koenigsknecht  
Scrum group 1  

  

## Sources 

https://www.ffiec.gov/npw/Institution/TopHoldings

https://www.americanbanker.com/news/fed-details-stress-test-scenarios-for-2021#:~:text=The%20Fed%20conducts%20two%20separate,do%20so%20by%20April%205.

https://www.dob.texas.gov/sites/default/files/files/Applications-Forms-Publications/Publications/Top-Banks/top0319.pdf

https://www.federalreserve.gov/boarddocs/supmanual/bhcpr/UsersGuide13/0313.pdf


 <!-- ![Capitol One](images/Cap_one_provisions&_losses.png ) -->
 <div class = 'row'>
    <div class = 'column'>
    <img src="images/Cap_one_provisions&_losses.png" width="250" height="200" >
    <img src="images/JPM_provisions&_losses.png" width="250" height="200">
    </div>
    <div class="column">
    </div>
    <div class="column">
        <img src="images/GS_provisions&_losses.png" width="250" height="200">
         <img src="images/citigroup_provisions&_losses.png" width="250" height="200">
    </div>
</div>

