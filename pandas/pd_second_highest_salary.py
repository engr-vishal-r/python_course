import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    if len(distinct_salaries) < 2:
        result = pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        result = pd.DataFrame({'SecondHighestSalary': [distinct_salaries.iloc[1]]})
        
    return result


data = {'id': [1, 2, 3], 'salary': [100, 200, 300]}
employee = pd.DataFrame(data)

print(second_highest_salary(employee))
