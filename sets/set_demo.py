city_1={"chennai", "bangalore","delhi","hyderabad"}
city_2={"cochin","pune","chennai","delhi","mumbai"}

print("Join both sets  --> ",city_1.union(city_2))
print("Common fields --> ",city_1.intersection(city_2))
print("Difference  --> ", city_1.difference(city_2))


city_1.remove("delhi")
print("printing city after removing 1 element  ---> ", city_1)

city_1.add("Kolkata")
print("printing city after new element  ---> ", city_1)