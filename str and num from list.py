A = [1,3,5,"Name","Py",80,"Apple", "Fruit", "Mahi", "Neha", "Zahir", "Berry", "Asif", "Bahar"]
B = [1,3,"py","apple", "bahar", "fruit", "berry", "nill"]
C = []
filter = 0
str_A = []
str_A_lower = []
str_B_lower = []
num_A = []
str_B = []
num_B = []
index_num = 0

for ele_A in A:
	try:
		filter = ele_A +1
		num_A.append(ele_A)
	except Exception:
		str_A.append(ele_A)
		continue
		
for ele_B in B:
	try:
		filter = ele_B +1
		num_B.append(ele_B)
	except Exception:
		str_B.append(ele_B)
		continue
		
set_num_A = set(num_A)
set_num_B = set(num_B)
diff_num_list = list(set_num_A - set_num_B)
diff_num_list.sort()

for ele_str_A in str_A:
	ele_str_A_lower = ele_str_A.lower()
	str_A_lower.append(ele_str_A_lower)

for ele_str_B in str_B:
	ele_str_B_lower = ele_str_B.lower()
	str_B_lower.append(ele_str_B_lower)
	
str_A_lower_set = set(str_A_lower)
str_B_lower_set = set(str_B_lower)	
diff_str_list = list(str_A_lower_set - str_B_lower_set)

for ob  in diff_str_list :
	index_num = (str_A_lower.index(ob))
	C.append(str_A[index_num])
	
C = sorted (C)
C = C + diff_num_list
print(C)		