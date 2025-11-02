import pandas as pd

person={"id":[1,2,3],
        "email":["abc@gmail.com","gmail@gmail.com","abc@gmail.com"]}


person=pd.DataFrame(person)

person.sort_values(by="id", inplace=True)

person.drop_duplicates(subset="email",keep="first",inplace=True)

print(person)