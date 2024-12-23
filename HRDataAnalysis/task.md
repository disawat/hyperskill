# Project: HR Data Analysis
In this project, you'll be working with datasets represented in the XML format. XML is an eXtensible Markup Language,
one of the most popular formats for storing and exchanging data.

## Stage 1/5: Load the data and modify the indexes
Your HR boss gave you three datasets. The first two are from different offices: A and B (A_office_data.xml and B_office_data.xml, respectively);
the third is the HR dataset (hr_data.xml). The guy wants you to investigate the data.
The first thing you need to do is to check and reindex it for further stages.

## Stage 2/5: Merge everything
Use concatenation to generate a dataset with information from both offices.
Use the left merging by index to merge the previously created dataset with the HR's dataset. When joining,\
generate a column containing information about each row's origin. Keep only those employees' records that are present in both datasets.

## Stage 3/5: Get the insights
The HR boss needs to know something about the employees. Find out the answers to the following questions:
1. What are the departments of the top ten employees in terms of working hours?
2. What is the total number of projects on which IT department employees with low salaries have worked?
3. What are the last evaluation scores and the satisfaction levels of the employees A4, B7064, and A3033?

## Stage 4/5: Aggregate the data
The HR boss wants to delve into the metrics of the two employee groups: those who left the company and those who still work for us.
You decided to present the information in a table.

The HR boss asks for the following metrics:
- the median number of projects the employees in a group worked on, and how many employees worked on more than five projects;
- the mean and median time spent in the company;
- the share of employees who've had work accidents;
- the mean and standard deviation of the last evaluation score.
Remember that the guy from HR asks for those metrics for two different groups!

## Stage 5/5: Draw up pivot tables
The HR boss desperately needs your pivot tables for their report.
1. The first pivot table displays departments as rows, employees' current status, and their salary level as columns.
The values should be the median number of monthly hours employees have worked. In the table,
the HR boss wants to see only those departments where either one is true:
- For the currently employed: the median value of the working hours of high-salary employees is smaller than the hours
  of the medium-salary employees, OR:
- For the employees who left: the median value of working hours of low-salary employees is smaller than the hours of high-salary employees
2. The second pivot table is where each row is an employee's time in the company;
  the columns indicate whether an employee has had any promotion. The values are the last evaluation score's minimum, maximum, mean,
  and satisfaction level. Filter the table by the following rule: select only those rows where the previous mean evaluation score
  is higher for those without promotion than those who had.
  
