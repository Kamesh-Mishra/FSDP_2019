#Weighted Score Calculator


A1= float(input("score in A1 assingmnet:"))
A2= float(input("score in A2 assingmnet:"))
A3= float(input("score in A3 assingmnet:"))

E1= float(input("score in E1 exam:"))
E2= float(input("score in E2 exam:"))

weighted_score = int(( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35)

print("weighted score based on individual assignment scores is:",weighted_score)
