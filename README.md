# DataScience_Python_R_Brazilian_Health_System
This Repository presents my data science project on the Brazilian Health Public System.  
I created it for data science popularization purpose, as part of my LinkedIn article, available on:  https://www.linkedin.com/pulse/analisando-dados-de-exames-preventivos-do-sus-com-r-e-amanda/

The chosen dataset presents the Papanicolau test examinations for each Brazilian city. This test is the main screening strategy for cervical cancer, the 3rd most common type of cancer in women. The Brazilian Health Public System is widely spread and used all over the country. Therefore, this publicly available dataset can be used to investigate the relations between the regional aspects and the Papanicolau test distribution effectiveness.

The following graph presents the Papanicolau test examinations averages in each Brazilian State, and the dashed line is the country average.  Notably, some states present a large deviation from the country average, even considering states in the same region (MG and RJ). For those who are not familiar with the Brazilian regions, a brief explanation: Brazil is divided into five big regions,  groups of states possessing some geographical similarities. 

graph1

The large variation in the same region is interesting and could be associated with relevant indicators, for example, the population density, the median wage, the amount of public health system centers per area, etc... Even though RJ and MG are placed in the same region, they present greatly different population densities. The RJ state is 10 times more populous than MG, and from the first graph in notable that RJ has low effectiveness on Papanicolau test distribution in comparison to MG. Therefore, one hypothesis arises in this context: is the relation between the population density and the Papanicolau test distribution effectiveness an inverse relationship? 

The dispersion plot was constructed in orded to test this hypothesis. The four circled points were considered outliers.

graph2

Following the investigation, a regression model was constructed. The shadow zone presents the 95% confidence interval. As only 7 states are placed in this zone, the hypothesis is not validated. Thus, other indicators should be considered to adequately explain the strong disparities visualized on the first graph. 

graph3 

------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is still an incipient project, and the main goal is to train my skills in data mining, analysis, Python, and R development. Some of the performed programming tasks are:

->The creation of Python scripts to process and join two datasets: the Papanicolau test dataset and the population density dataset. The primary key in the first dataset (sate abbreviation of two characters) was linked to the primary key in the second dataset (complete state names, variable size of string vector).  

->The creation of R plots and linear regression using ggplot2 library.






