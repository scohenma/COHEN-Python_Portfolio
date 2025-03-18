# Tidy Data Project - 2008 Olympic Medalists Analysis

## Project Overview
The purpose of this project is to use **tidy data principles** learned during _Elements of Computing_class to analyze the **2008 Olympic medalists dataset**. The goal is to **clean, reshape, and explore the data** to identify patterns in medal distribution and gender representation across Olympic sports. Using Python, I transformed the dataset into a **tidy format**, allowing for the user to understand data better and learn more aboout a special event like the 2008 Summer Olympics. 

The tidy-data principles that were followed were that: 
- **Each variable is in its own column.**
- **Each observation forms its own row.**
- **Each type of observational unit forms its own table.**

## Instructions to Run Notebook 
1- Clone the Repository 
  * Download the project from Github. The name of the repository is Tidy-Data Project. 
2- Install Required Dependencies
  * Once you are sure that Python is installed, import pandas, matplotlib, and seaborn libraries so that the         code can run properly 
3- Open the Jupyter Notebook 
4- Follow the step by step instructions and guidance in the markdown cells in the notebook 
  * Inside the notebook, there are comments about the code and the analysis.


## Dataset Description 
* This dataset includes information on Olympic medalists from the 2008 Summer Olympics. It has 1875 rows and 71 columns, including vital information:
    ** Medalist Names - Name of the athletes.
    ** Sport - The sport or event in which the athlete competed during the Olympics.
    ** Gender - The gender of the athlete.
    ** Medal - Type of medal won (Gold, Silver, Bronze).
  
### Pre-Processing Steps:
1. Reshaping Data. 
  * Using pd.melt(), convert wide-format data (with separate columns for each male and female sport) into long-      format. 
  * This created two new columns: ‘Category’ and ‘Medal.
2. Split Combined Variables. 
  * The ‘Category’ column contained both gender and sport. The function str.split() was used to separate gender      and sport into two different unique columns. 
3. Clean and Format 
  * Renamed columns for clarity, and capitalized names using str.title()
4. Removing Unecessary and Missing Data
  * Used drop.na() to remove rows where no rows were awarded.
  * Dropped the ‘Category’ column now that new columns have been created with same values. 
5. Created pivot tables for analysis
  * Aggregate data to explore medal distribution and gender representation.


## References
[Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
[Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf)
[Britannica](https://www.britannica.com/sports/boxing/Women-in-boxing)

## Insights and Analysis 
### Top 10 Sports with the Most & Least Medals Awarded
* Athletics and Swimming awarded the highest number of medals, likely because they contain multiple event     categories.
* Team sports like Basketball and Volleyball also awarded more medals, as multiple athletes receive medals per team.
* On the other hand, other sports like Modern Pentathlon and Shooting had much fewer medals awarded, proving that some sports have fewer events or a more selective qualification process.

This is evidence that not every sport has the same level of opportunity or competitiveness: 
![Top 10 Sports with Most Medals awarded](/top_10_total)

### Gender Representation in Olympic Sports
This analysis also aimed to to explore medal distribution based on gender in the 2008 Olympics.
* Male-Exclusive Sports:
  * Greco-Roman Wrestling, Baseball, and Boxing had 0% female representation in 2008, meaning women were not         allowed to compete.
  * Women’s Boxing was introduced in 2012, showing progress, but Greco-Roman Wrestling remains male-only today.
  * Baseball had Softball as the women's equivalent sport, which explains why women did not participate in           baseball itself.

Sports with High Female Representation
* The sports where women won the highest percentage of medals were mostly female-only (Rhythmic Gymnastics, Synchronized Swimming, Softball).
* This high representation is not due to equal participation across genders but rather the exclusion of men from these events.
* Only a few mixed gender sports exceeded 50% female participation, suggesting that women’s dominance was mostly in gender-segregated events.

![Top 10 Sports with High Female Representation](/top_10_high)



Sports with Low Female Representation
* Apart from male-exclusive sports, many mixed-gender sports still had far less than 50% female representation, suggesting that even in mixed gender sports, there were fewer women winning Olympic medals. 

![Top 10 Sports with High Female Representation](/top_10_low)


* This project was a great opportunity to not only learn more about the 2008 Olympics, but also put what I have learned in class into real life practice. I am looking forward to working on more projects to continue developing my skills! 










