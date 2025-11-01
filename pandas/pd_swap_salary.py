import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex']=salary['sex'].replace({'f':'m','m':'f'})

    return(salary)


salary = {
    "id": [1, 2, 3, 4],
    "name": ["A", "B", "C", "D"],
    "sex": ["m", "f", "m", "f"],
    "salary": [2500, 1500, 5500, 500]
}

salary= pd.DataFrame(salary)

print(swap_salary(salary))