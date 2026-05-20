###you manage a store and have a list of item with there stock level you need 
# to check which item need restoring (stock <5).
# write a function low_stock_items(inventory: dict) ->ist hat returns a list
#  hat need to be restored


# sample Input:

# low_stock_items({"milk":10 , "bread": 3 , "eggs": 4}:)

# samle Output:
# ["bread", "eggs"]

stock = {"milk":10 , "bread": 3 , "eggs": 4}

def low_stock_items(stock):
    restocked = []

    for i in stock:
        if stock[i]<5:
            restocked.append(i)
    print(restocked)        

low_stock_items(stock)


# #####You're simulating a snooze alarm. The alarm goes off every 5 minutes. 
 # The person snoozes it until they finally get up after a certain number of minutes.

# Write a function count_snoozes (minutes_awake: int) - int that tells 
# how many times the person hit snooze before waking



def count_snooze(minutes_awake):
    count = 0
    time = 0
    while time + 5 <= minutes_awake:
        count +=1
        time +=5
    return count    
a = count_snooze(23)
print(a)