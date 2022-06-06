#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Li-Ci(Lilian) Chuang
##### *Resume* 
''')

image = Image.open('Professional Photo_2.png')
st.image(image, width=150)

st.info('''
##### I am graduating in May 2022 and am open to full-time *Business Analyst*/ *Data Analyst*/ *Data Scientist* positions! 
''')

st.markdown('## About', unsafe_allow_html=True)
st.info('''
- Master's Degree in Business Analytics and Information Management at Purdue University.
- Analytics professional with 3-year work experiences in pharmaceutical and high-tech industry.
- Love digging deep into data and taking on challenges!
- With cross-function collaboration mindset and creative/ critical thinking.
- Core Competencies: Business Analytics, Statistics, Data Mining, Machine Learning, NLP, Database Management, Operation Management, Logistics, Marketing Analytics, A/B Test, Data Visualization, Written/Oral Communication, High Flexibility/Responsibility/Accountability.
''')


#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#resume">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#data-analytics-project">Data Analytics Project</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skill">Skill</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certificate">Certificate</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt5(a, b, c, d):
  col1, col2, col3, col4 = st.columns([1,2.5,4.5,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
  with col4:
    st.markdown(d)
    
#####################
st.markdown('''
## Education
''')

txt('**Purdue University**', 'WL, Indiana')
txt('*Master of Science*, Business Analytics and Information Management','2021-2022')
st.markdown('''
- Awarded a merit-based scholarship
- GPA: `3.60/4.00`
- Fall semester 2021 Academic Honors
''')

txt('**National Chengchi University**', 'Taipei, Taiwan')
txt('*Bachelor of Arts*, Economics', '2013-2017')
st.markdown('''
- GPA: `3.97/4.00`
- Securities Research Club.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Analyst Student, Spf.io**','Jan.2022 - Apr.2022')
txt('Industry Practicum, Purdue University', 'WL, Indiana')
st.markdown('''
- `Winner` in poster competition at 2022 INFORMS Business Analytics Conference
- Implemented adaptive machine translation (`AutoML`) experiments in `Google Cloud`, `Microsoft Azure` platform with data sampling and pre-processing, resulting in `8.9%` improvement in BLEU score (translation metric)
- Conducted model validation using `Python NLTK` libraries and a survey to demonstrate statistically significant differences in the models with Friedman Test
- Reduced editing cost by `90%` and time by `98%` by extending massive corpora to meet different domain needs
''')

txt('**Data Analyst Intern, Design Alternatives**','Nov.2021 - Dec.2021')
txt('Database Course, Purdue University', 'WL, Indiana')
st.markdown('''
- Designed, implemented, and optimized database management systems (`MySQL`) in accordance with customer’s needs.
- Helped production scheduling by executing data extraction, improving efficiency and accuracy.
- Automated project progress monitoring and checks tracking, reducing labor time by `30%`.
''')

txt('**Associate Sales Operations Specialist, Merck**','Aug.2020 - May.2021')
txt('Commercial Operations & Strategy, SFE team', 'Taipei, Taiwan')
st.markdown('''
- Built `dashboards` to visualize analytics for sales budget planning and monitoring, supporting decision-making processe with business intelligence solutions.
- Collected and cleaned `historical` and `real-time` data to forecast future demand, optimizing manufacturing plans
- Administered `Salesforce` CRM platform to organize events and maintain customer relationships.
- Administrated and managed system of `territory alignment` and `incentive plan`, to maintain `salesforce` database for `100+` sales representatives from `5` business units.
''')

txt('**Care Program Coordinator, Nokia**', 'Jul.2017 - Jul.2019')
txt('Global Service, Chunghwa Mobile Account', 'Taipei, Taiwan')
st.markdown('''
- Drafted and maintained app to increase fulfillment rate and minimize service impact.
- Analyzed and forecasted the replacement rate of 3G/ LTE installation bases to modify budget planning and reduce system downtime, including `8 teams` and `80+` type of products; ranked in top `5%` for care program (maintenance) internal audits in the Greater China region.
- Collaborated with vendors (`HP` and `Oracle`) to assess necessities of warranty contracts to reduce risk for business.
''')

txt('**Administrative Assistant Intern, Microsoft**', 'Jul.2016 - Jun.2017')
txt('Small and Mid-market Solutions and Partners', 'Taipei, Taiwan')
st.markdown('''
- Led `60` technical and sales trainings with `367 hrs`. in total, with an average satisfaction rating of `8.47/9.00`.
- Designed and maintained Partner@MS `app` with cross-functional teams and refined user experience.
- Organized an `Azure` solution training program, teaching `204` employees and `24` external partners to gain certificates.
''')

#####################
st.markdown('''
## Data Analytics Project
''')
txt5('Python', 'Does-Vaccination-Help-the-Economy?', 'Are vaccines absolutely, 100 percent the answer to economic challenges imposed by the pandemic? Analyzed the relationship between vaccination rate data and the unemployment rate data, which could be an index reflecting the prosperity of the economy.',
     'https://github.com/lilianchi/Does-Vaccination-Help-the-Economy')
txt5('R', 'College-Major-Recommender', 'Many high school students run into a dilemma upon graduation.They do not know where to begin when trying to select a college major or even had changed their major more than twice afterwards. The tool is to aid them in this decision making process.',
     'https://github.com/lilianchi/College-Major-Recommender')
txt5('SAS EM', 'Credit-Default-Prediction', 'Kaggle Competiton: Predicting credit default by developing a predictive model that utilizes historical payment status and certain demographical information to evaluate the likeliness of credit default.',
     'https://github.com/lilianchi/Credit-Default-Prediction')
txt5('Python', 'lost-or-found?','Improved the ad-viewers’ experience by analyzing Craigslist’s business model and process of the platform to find improvements and solutions for this proposal with a demo implementation.',
     'https://github.com/lilianchi/lost-or-found')
txt5('SQL', 'Database-Alternatives','Helped an interior design company to solve its timesheet calculation and checks tracking problem by building a database on SQL and executing data extraction',
     'https://github.com/lilianchi/Database-Alternatives')
txt5('SAS', 'SAS-Optimization-Challenge', 'Applied a time-series `random walk` forecast and an optimization model on SAS to optimize the resource allocation problem with minimized cost by `14.8%`',
     'https://github.com/lilianchi/SAS-Optimization-Challenge')

#####################
st.markdown('''
## Skill
''')
txt3('Programming', '`Python`, `SQL`, `R`, `SAS`, `SAS EM`')
txt3('Statistics', '`Minitab`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`Power BI`, `Tableau`, `matplotlib`, `seaborn`, `ggplot2`')
txt3('Machine Learning','`scipy`, `scikit-learn`')
txt3('Deep Learning', '`tensorFlow`,`Keras`')
txt3('Model deployment', '`streamlit`, `R Shiny`')

#####################
st.markdown('''
## Certificate
''')
txt5('Oracle SQL', 'Oracle Database 12c SQL Certified Associate 1Z0-071','DDL, DML, Aggregration, Join, Condition expressions, Subquery, Datetime, Sequences, Synonyms, Indexes, Views, User access','https://udemy-certificate.s3.amazonaws.com/pdf/UC-0a070e10-e731-4b9e-bf8d-716ebb08745d.pdf')
txt5('Python', 'Python Fundamentals Track', 'Advanced level in assessment','https://www.datacamp.com/statement-of-accomplishment/track/4a3acb93fce85aabfd09390230585a217c9932dc')
txt5('Python', 'Data Manipulation with Python Track', 'Data manipulation, Join data, Database in Python','https://www.datacamp.com/statement-of-accomplishment/track/ecc0df4491f3f40f4e2b5e6a9396660b1f0dd179')
txt5('Python', 'Data Analyst Track', 'Visualization with matplotlib/seaborn, Importing/ Cleaning data, EDA, Categorical data', 'https://www.datacamp.com/statement-of-accomplishment/track/feb13a3355b8ad31a25dbd7bb28e11dfd8ad34f1')
txt5('Python', 'Data Scientist Track', 'Functions, Date and time, Satistical Thinking, Supervised-learning, Unsupervised-learning, Tree-based models, Cluster Analysis','https://www.datacamp.com/statement-of-accomplishment/track/06dc785b91f1180e54aaeed570bbd261319b2096')
txt5('SQL', 'SQL Fundamentals Track', 'Join tables, Summary Statistics, Window funcions, Text Analysis','https://www.datacamp.com/statement-of-accomplishment/track/92043e9ef4e29d1b53372524eba2a3bd20fbc5a3')
txt5('Tableau', 'Tableau Fundamentals Track','Sheet, Dashboard, Story, EDA, Parameters, Interactive', 'https://www.datacamp.com/statement-of-accomplishment/track/df95c91be61925f8e31f48cb033af91e699cafee')

# txt4('Python', 'Introduction to Python', 'https://www.datacamp.com/statement-of-accomplishment/course/433731c66ae1b4bbeb40f3f89728156caf638850')
# txt4('Python', 'Introduction to Data Science in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/73bce8b85d68b36fe58943ad713efee0c29a829d')
# txt4('Python', 'Intermediate Python', 'https://www.datacamp.com/statement-of-accomplishment/course/d78c4a9412a86d208de64a3c531ea057b8a397cd')
# txt4('Python', 'Data Manipulation with pandas', 'https://www.datacamp.com/statement-of-accomplishment/course/d9ad98a945e3bfebcf3fa7de14e800c38ab6cd4e')
# txt4('Python', 'Joining Data with pandas', 'https://www.datacamp.com/statement-of-accomplishment/course/75909c8d895a2cf4d564448f02b0abe94f2a5483')
# txt4('Python', 'Introduction to Data Visualization with Matplotlib', 'https://www.datacamp.com/statement-of-accomplishment/course/5c77ce607d19c936cc07ac6ee7171a9e82c578b0')
# txt4('Python', 'Introduction to Data Visualization with Seaborn', 'https://www.datacamp.com/statement-of-accomplishment/course/d266da3cfdf6de611cace2066871debf1305c2ba')
# txt4('Python', 'Intermediate Data Visualization with Seaborn', 'https://www.datacamp.com/statement-of-accomplishment/course/3602b111b859ade772682921da5e5e2bf919e85c')
# txt4('Python', 'Introduction to Importing Data in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/d16974274f44ed26155b007d59d5b38b6f16c036')
# txt4('Python', 'Intermediate Importing Data in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/e1f6e15bf35629f393e8056e4e6cb60f8ae19071')
# txt4('Python', 'Cleaning Data in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/8fc45244a91bafe9d64e9baf25febd1595fc55cc')
# txt4('Python', 'Working with Categorical Data in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/7123a9e9b3b559b31ade4f1e8c8421112eb3642b')
# txt4('Python', 'Exploratory Data Analysis in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/1ef943fa9cfb160032652468c2600cf4e946d74e')
# txt4('Python', 'Analyzing Police Activity with panda', 'https://www.datacamp.com/statement-of-accomplishment/course/3f670be7297721fb6cb7cc0d1c148a4e17151ff9')
# txt4('Python', 'Streamlined Data Ingestion with pandas', 'https://www.datacamp.com/statement-of-accomplishment/course/4b26a61ffe2e265e78aa7dda45cc053243641e3b')
# txt4('Python', 'Introduction to Databases in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/a46ef8f2c56410f955bf891251a228dc566a908b')
# txt4('Python', 'Python Data Science Toolbox (Part 1): Function, Lambda', 'https://www.datacamp.com/statement-of-accomplishment/course/93b99a20fd3552d7c19591749683cf0776b6b296')
# txt4('Python', 'Python Data Science Toolbox (Part 2): Iterations, List comprehension', 'https://www.datacamp.com/statement-of-accomplishment/course/762cb44720359dd82ebad5a6bf5001b655b900f8')
# txt4('Python', 'Working with Dates and Times in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/bb7940fdf06cd9b84e42b11c0900abcc130674d7')
# txt4('Python', 'Writing Functions in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/be27486f54028dfdf5dbb9e0a7373278b4200022')
# txt4('Python', 'Statistical Thinking in Python (Part 1)', 'https://www.datacamp.com/statement-of-accomplishment/course/a0df4e485a0c170a7a839ecfda9d86e11f623528')
# txt4('Python', 'Statistical Thinking in Python (Part 2)', 'https://www.datacamp.com/statement-of-accomplishment/course/5943ed164946a84d657eec5f1aaf64674a4ab766')
# txt4('Python', 'Supervised Learning with scikit-learn', 'https://www.datacamp.com/statement-of-accomplishment/course/c487e379a4c2b23d2210e846f46ba774697b19b4')
# txt4('Python', 'Unsupervised Learning in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/4cd54727f7ed83d4e4724dfc55f56071e9d80ce2')
# txt4('Python', 'Machine Learning with Tree-Based Models in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/b6b98b02a6ebd2d9ae0f41ea33309102383c434e')
# txt4('Python', 'Case Study_School Budgeting with Machine', 'https://www.datacamp.com/statement-of-accomplishment/course/417a608cc78b18aa98f00b6603312d302cab36f6')
# txt4('Python', 'Cluster Analysis in Python', 'https://www.datacamp.com/statement-of-accomplishment/course/653b4aa6b565e9d1cbbe8d4fa4954de7b0f7ff2d')
# txt4('SQL', 'Introduction to SQL', 'https://www.datacamp.com/statement-of-accomplishment/course/74189f8967d733767cacc857fc5387e935ad5278')
# txt4('SQL', 'Introduction to Relational Databases in SQL', 'https://www.datacamp.com/statement-of-accomplishment/course/9ee409a13f241eceba04ceace80ee768363430cd')
# txt4('SQL', 'Joining Data in SQL', 'https://www.datacamp.com/statement-of-accomplishment/course/1e00235eb90442b41281276648b3f21b168a01f7')
# txt4('SQL', 'Intermediate SQL', 'https://www.datacamp.com/statement-of-accomplishment/course/938298af9bb7561fbad10ffcaf14cef7df0256ea?raw=1')
# txt4('SQL', 'PostgreSQL Summary Stats and Window Functions', 'https://www.datacamp.com/statement-of-accomplishment/course/87d4bb80c7787dd6b8887127e866630dfba3ac16')
# txt4('SQL', 'Functions for Manipulating Data in PostgreSQL', 'https://www.datacamp.com/statement-of-accomplishment/course/fdaf8ab34a4a6e5c34152e7b7f0675056ed60ce0')
# txt4('Tableau', 'Introduction to Tableau', 'https://www.datacamp.com/statement-of-accomplishment/course/4e4c9df2364aefa9cc45dd754c1a15214aa6376c')
# txt4('Tableau', 'Analyzing Data in Tableau', 'https://www.datacamp.com/statement-of-accomplishment/course/1ae628e7790653cb0c3b4acc96569807e45fde27')
# txt4('Tableau', 'Creating Dashboards in Tableau', 'https://www.datacamp.com/statement-of-accomplishment/course/151699d1c45a8602544e2d5716b61421b0d46564')
# txt4('Tableau', 'Case Study_Analyzing Customer Churn in Tableau', 'https://www.datacamp.com/statement-of-accomplishment/course/e475db386ec42fd5fc9b1264bf08aa08e1a4a6db')
# txt4('Tableau', 'Connecting Data in Tableau', 'https://www.datacamp.com/statement-of-accomplishment/course/6a07e131e77555fcdd4a38f0ba06f8d44dfc3d36')
# txt4('R', 'Introduction to R', 'https://www.datacamp.com/statement-of-accomplishment/course/433731c66ae1b4bbeb40f3f89728156caf638850')
# txt4('R', 'Data Manipulation with dplyr', 'https://www.datacamp.com/statement-of-accomplishment/course/bbc9f6ada20e2e2776fcad99d5b4532351272bdb')
# txt4('R', 'Introduction to the Tidyverse', 'https://www.datacamp.com/statement-of-accomplishment/course/46bd5c2d51131d94cf986b7c898986245f5c720d')
# txt4('R', 'Introduction to Writing Functions in R', 'https://www.datacamp.com/statement-of-accomplishment/course/465bf6d390d1baee65da2acd3d739b020ab6ab7d')
# txt4('R', 'String Manipulation with stringr in R', 'https://www.datacamp.com/statement-of-accomplishment/course/83be478ff803b61e4dadf26f709d8290b2596f69')
# txt4('R', 'Working with Dates and Times in R', 'https://www.datacamp.com/statement-of-accomplishment/course/93db3a10de7a9f453c07d979924b57aed86c51e5')
# txt4('R', 'Writing Efficient R Code', 'https://www.datacamp.com/statement-of-accomplishment/course/db17dc8e0efe5ad47e940c510f67942e9e6510c8')
# txt4('Power BI', 'Introduction to Power BI', 'https://www.datacamp.com/statement-of-accomplishment/course/ff181e5e94c279c80ff353ca2578d749d7001319')
# txt4('Power BI', 'Exploratory Data Analysis in Power BI', 'https://www.datacamp.com/statement-of-accomplishment/course/361b19db2cd94d4640eac0265b351ed6645b1b0e')


#####################
st.markdown('''
## Contact
''')
image1 = Image.open('LinkedIn.png')
txt2('LinkedIn', 'https://www.linkedin.com/in/lilian-chuang/')
txt2('GitHub', 'https://github.com/lilianchi')
txt2('Resume', 'https://reurl.cc/9OaVeX')
txt2('E-mail', 'lilianchi1020@gmail.com')
txt2('Mobile', '(765)-775-7780')


# In[ ]:




