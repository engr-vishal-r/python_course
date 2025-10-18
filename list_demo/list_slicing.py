#lists are mentioned in [] and is mutable
playlist=['naan vanavilaiye pathen', 'golden sparrow', 'ranu bombay ki ranu', 'nenjinile']

#list methods
print("count the song number  -->", playlist.count("golden sparrow"))

playlist.pop()
print("remove the last element and printing the rest -->", playlist)

playlist.reverse()
print("print in reverse  --> ",playlist)


playlist.insert(1,"jhol")
print("new song is added -->", playlist)

playlist.append("hrudaiye bayaside")
print("new song added at last element -->", playlist)

#list slicing
print("first 2 elements  -->", playlist[0:2])
print("last 2 elements -->", playlist[-2::])