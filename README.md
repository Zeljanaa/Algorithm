# Algorithm

given a long string containing key value pairs in any order and the keys only,
the algorithm converts the long string into a perfect dictionary

## example 1:

raw_string: `age24namezeljana`

---

mappings: `['name', 'age']`

---

output: `{'name': 'zeljana', 'age': '24'}`

## example 2:

raw_string: `namezeljanaage24`

---

mappings: `['name', 'age']`

---

output: `{'name': 'zeljana', 'age': '24'}`

## example 3:

raw_string: `departmentcomputersciencelocationserbiaprofessiondatascientist`

---

mappings: `['profession', 'department', 'location']`

---

output: `{'department': 'computerscience', 'location': 'serbia', 'profession': 'datascientist'}`
