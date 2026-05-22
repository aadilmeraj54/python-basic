# for i in range(0,15,1):
#     print(i)
#     if i ==10:
#         continue ##it will skipp the reamaning steps for that iteration
#     print(i)

    

# for i in range(0,5,1):
#     for j in range(0,5,1):
#         if i+j<4:
#             continue
#         print(f"for this pair{i,j}we printed{i}")    



for i in range(0,6,2):
    print("*", end=" ")
    if i ==3:
        break
    for j in range (0,10,3):
        if i==3:
            continue
        print("*", end=" ")
    print(" ")    