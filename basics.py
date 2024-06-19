#selecting the data and consider the dataframe called employees and we dhould 
'''
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+ '''
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(students)
    return students.loc[students["student_id"]==101,["name","age"]]

#creating the new colums with doubling the salary as bonus
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']=2*employees['salary']
    return employees

#removing duplicates based on the email column.
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='email')

#changing the name of the columns
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'id':'student_id','first':'first_name','last':'last_name','age':'age_in_years'},inplace=True)
    return students
  
#FILLING THE NULL WITH 0 IN THE QUANTITY COLUMN
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0,inplace=True)
    return products
    
