#without partial
import pandas as pd

df1 = pd.read_csv("file1.csv", delimiter=",", header=0, encoding="utf-8")
df2 = pd.read_csv("file2.csv", delimiter=",", header=0, encoding="utf-8")
df3 = pd.read_csv("file3.csv", delimiter=",", header=0, encoding="utf-8")


#with partial
from functools import partial
import pandas as pd

# Create a partially applied function
read_configured_csv = partial(pd.read_csv, delimiter=",", header=0, encoding="utf-8")

df1 = read_configured_csv("file1.csv")
df2 = read_configured_csv("file2.csv")
df3 = read_configured_csv("file3.csv")