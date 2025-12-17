import random_utils as ran
import constants as con
import string_utils as st

#Тест string_utils
test1=st.upper("апельсин")
test2=st.poly("анна")
test3=st.count("нитроглицерин")
print(test1)
print(test2)
print(test3)

#Тест constants
test4=con.pi
test5=con.grav_post(749,258)
test6=con.speed_light
print(test4**2)
print(test5)
print(test6*3.6)

#Тест random_utils
test7=ran.random_int(1,6)
test8=ran.random_list(10,1,6)
shuffled=[1,9,7,4,0]
test9=ran.shuffle_list(shuffled)
print(test7)
print(test8)
print(test9)