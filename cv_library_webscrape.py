"""
Created -- 01/01/2023 03:48am
---By-----
Jeff David
"""


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

no_of_pages = 39 #39 max - 40pages is max on website
jobs = []


for page in range(no_of_pages):

    #re-initiating first page - then subsequently the current page being parsed
    url = 'https://www.cv-library.co.uk/data-analyst-jobs-in-united-kingdom?page='+ str(page+1)
    
    #webpage with job details
    webpage = requests.get(url)
    
    #scraping the web content from the webpage
    #can use html.parser or lxml
    soup = BeautifulSoup(webpage.content, 'html.parser')

    #Outer Most Entry Point of HTML:
    outer_most_point = soup.find('ol', attrs={'class':'results'})
    #print(outer_most_point)
    
    for i in outer_most_point:
        #print(i)
    
        #Job Title
        if i.find('a') != None:
            j_data = str(i.find('a'))
            j_title = 'data-job-title="(.*?)" data-open-js='
            job_title = re.findall(j_title, j_data)
            #print(job_title)
        
        #Job Profile Link - For Job Description
        if i.find('a') != None:
            l_data = str(i.find('a'))
            j_link = ' href="(.*?)" rel='
            job_link = re.findall(j_link, l_data)
            #print(job_link)     
        
        #Company, Company Link and Date Posted
        if i.find('p') != None:
            comp_lnk_dt = str(i.find('p'))
            company_link_date = list(comp_lnk_dt.split('>'))
            #print(company_link_date)

        #Salary, location and Contract type
        if i.find('dl') != None:
            sal_loc_type = str(i.find('dl'))
            salary_location_type = list(sal_loc_type.split('>'))
            #print(salary_location_type)


        jobs.append({'Job Title':job_title,
                     'Job Profile Link':job_link,
                     'Company, Company Link and Date Posted':company_link_date,
                     'Salary, location and Contract type':salary_location_type})
    print("Page "+str(page+1)+" Completed")
    
    
df = pd.DataFrame(jobs)
df.to_csv('jobs_cv_library.csv')
#print(df)
print("Your Data Has Successfully been parsed")   

    
    
    
        
    
   


