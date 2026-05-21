# ###infinite loop
# i = 1 
# while(i<10):
#     print("welcome to conition less loop")
#     print(i)
 

#  ##### Nested Loop
# for hour_hand in range (1,25,1):
#     for min_hand  in range (1,61,1):
#         print (hour_hand, "hour", min_hand, "min")



for i in range (0,60,2):
    for j in range(2,3,1):
        if (i%j==0):
            print(i)

