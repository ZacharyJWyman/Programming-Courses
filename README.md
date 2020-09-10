# Finding the Best Online Programming Courses
Web Scraper used for collecting data to determine the best programming courses on https://www.classcentral.com/

## To view notebook code:
https://github.com/ZacharyJWyman/Programming-Courses/blob/master/notebooks/Webscraping%20Data%20to%20Determine%20Best%20Programming%20Courses%20.ipynb
  
## Table of Contents
* [Data](#Data)
* [About](#About)
* [Libraries](#Libraries)
* [Findings](#Findings)
* [Conclusion](#Conclusion)
* [Authors](#Authors)

## Data
* Data is gathered from https://www.classcentral.com/ using a webscraper that I created.

## About
With online education increasing every year, it is getting harder to determine the best online course to take. There are numerous courses available and you  want to make sure that you are getting the best bang for your buck. This project webscrapes data from multiple domains on https://classcentral.com and determines the best courses with the most reviews. 

## Libraries
* Pandas, matplotlib, seaborn, beautifulsoup, requests

## Findings
I was initially able to create a webscraper for a single page using beautifulsoup. However, I wanted to increase the efficiency and capability of the project and be able to cycle through each page that contained results on the domain I was interested in. I spent some time cleaning the code and created functions that can quickly gather any data from the site using beautifulsoup and requests. The only input you need is the amount of results and the url of the first page for that domain. Using my webscraper, I gathered informaton about the best courses in the following domains: Programming, Python, Machine Learning, Data Science, CS, Stats & Probability, Artifical Intelligence, and Data Analysis. To follow up I wanted to determine the best provider to take each course through. This was accompished using matplotlib and seaborn to create subplots to look at the courses available. Coursera, edX, and Udacity were the most represented. 
![webscrape](https://user-images.githubusercontent.com/64059855/92672007-8d886d80-f2cc-11ea-8bbb-ac0521398dbd.PNG)



## Conclusion
* Designed and implemented a web scraper that can gather data from various domains based off of input url and number of results.  
* Defined functions that a user can easily use to pull their own data from https://www.classcentral.com  
* Cleaned and processed data to determine the best programming courses to take online and which provider to take the course through. 

### What I learned:
In this project I gained familiarity working with beautifulsoup. Web scraping is such a powerul tool, opening up any source online as a potential data bank. To understand how each webpage was set up, I had to brush up on my knowledge of html script. Initially, the data was very messy and I had to spend a substantial amount of time putting it into a usable format for analysis. To finish the project off, I worked with matplotlib and seaborn to create subplots. This added to my knowledge in formatting adjustments to make my plots look more refined. 

## Author
Created by *Zachary Wyman*  
Contact: zack.wyman1@gmail.com   
