#python_list
max=["Audi","Mastang","BMW","GT350"]
print(max)

#list_length
max=["Audi","Mastang","BMW","GT350"]
print(len(max))

#access
max=["Audi","Mastang","BMW","GT350"]
print(max[1])

#negative-indexing
max=["Audi","Mastang","BMW","GT350"]
print(max[-1])

#range of index
max=["Audi","Mastang","BMW","GT350","innova","esport"]
print(max[2:5])

#item_existance
max=["Audi","Mastang","BMW","GT350"]
if "Audi" in max:
    print("yes","Audi in list")
else:
    print("invalid data")

#change_list
max=["Audi","Mastang","BMW","GT350"]
max[2]="innova"
print(max)

#range of change
max=["Audi","Mastang","BMW","GT350"]
max[1:2]=["innova","Esport"]
print(max)

#inser change
max=["Audi","Mastang","BMW","GT350"]
max.insert (1,"Innova")
print(max)

#add
max=["Audi","Mastang","BMW","GT350"]
max.append("innova")
print(max)

#extend
max=["Audi","Mastang","BMW","GT350"]
pax=["innova","esport"]
max.extend(pax)
print(max)

#remove list
max=["Audi","Mastang","BMW","GT350"]
max.remove("Audi")
print(max)

#pop
max=["Audi","Mastang","BMW","GT350"]
max.pop()
print(max)

#pop_2
max=["Audi","Mastang","BMW","GT350"]
max.pop(1)
print(max)

#del_keyword
max=["Audi","Mastang","BMW","GT350"]
del max [0]
print(max)

#clear list
max=["Audi","Mastang","BMW","GT350"]
print(max)


