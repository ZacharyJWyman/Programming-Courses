# Finding the Best Online Programming Courses
Web Scraper used for collecting data to determine the best programming courses on https://www.classcentral.com/

## To view notebook code:

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
With online education increasing every year, it is getting harder to determine the best online course to take. There are so many courses and youw ant to make sure that you are getting the best bang for your buck. This project webscrapes data from multiple domains on https://classcentral.com and determines the best programming courses with the most reviews. 

## Libraries
* Pandas, matplotlib, seaborn, beautifulsoup, requests

## Findings
Through this project I was initially able to create a webscraper for a single page using beautifulsoup. However, I wanted to increase the efficiency and capcability of the project and be able to cycle through each page that contained results on the domain I was interested in. I spent some time cleaning the code and created functions that can quickly gather any data from the site using beautifulsoup and requests. The only input you need is the amount of results and the url of the first page for that domain. From the website I gathered informaton about the best courses in the following domains: Programming, Python, Machine Learning, Data Science, CS, Stats & Probability, Artifical Intelligence, and Data Analysis. To follow up I wanted to determine the best provider to take each course through. This was accompished using matplotlib and seaborn to create subplots to look at the courses available. Coursera, edX, and Udacity were the most represented. 

Insert image here


## Conclusion
* 

## Author
Created by *Zachary Wyman*  
Contact: zack.wyman1@gmail.com   
