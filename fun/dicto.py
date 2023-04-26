my_dict={"apple":5,"mango":6,"orange":7,"bean":8}
 
value=2
count=len([x for x in my_dict.values()if x< value ])
print(count)
