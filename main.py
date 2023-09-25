#INF601 - Advanced Programming in Python
#Spencer Maley
#Mini Project 2


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#(5/5 points) Proper import of packages used.
#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#Think of some question you would like to solve such as:
#"How many homes in the US have access to 100Mbps Internet or more?"
#"How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
#Here are some other great datasets: https://www.kaggle.com/datasets
#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.




#start of program
 # create charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

#entire file from the database
raw_data = pd.read_csv("tornados.csv")

#shortened version to make graph more legible
refined_data = raw_data.sample(n=15)


#Date vs len

#make graph readable
plt.figure(figsize=(20,10))
#bar graph
plt.bar(refined_data["date"], refined_data['len'])
#labels
plt.title("Avg Length of Tornado in Miles of 15 Random Tornadoes from 1950-2022")
plt.xlabel("Date (yyyy/mm/dd)")
plt.ylabel("Length in miles")
#saving and showing graph
savefile = "charts/Date vs Length.png"
plt.savefig(savefile)
plt.show()

#Date vs time

#make graph readable
plt.figure(figsize=(20,10))
#scatterplot graph
plt.scatter(refined_data["date"], refined_data["time"])
#labels
plt.title("Time of 15 Random Tornadoes from 1950-2022")
plt.xlabel("Date (yyyy/mm/dd)")
plt.ylabel("Time (hh/mm/ss)")
#save and show
savefile = "charts/Date vs Time.png"
plt.savefig(savefile)
plt.show()

#Date vs width

#readable
plt.figure(figsize=(20,10))
#bar graph
plt.bar(refined_data["date"], refined_data['wid'])
#labels
plt.title("Avg Width of Tornado in Yards of 15 Random Tornadoes from 1950-2022")
plt.xlabel("Date (yyyy/mm/dd)")
plt.ylabel("Length in yards")
#save and show
savefile = "charts/Date vs Width.png"
plt.savefig(savefile)
plt.show()
