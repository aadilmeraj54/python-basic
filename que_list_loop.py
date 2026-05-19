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