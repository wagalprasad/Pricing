import pandas as pd

class Cart:
    def getDetails(self):
        """function to read input data"""
        item = pd.read_csv('data.csv')
        basket = pd.read_csv('basket.csv')
        # join item and basket data
        item_basket =item.set_index('Item').join(basket.set_index('Item'))
        item_basket = item_basket.sort_values(by=['basket'])
        # calulate subtotal and add in dataframe
        item_basket['sub-total'] = item_basket['Price']*item_basket['Quantity']
        item_basket = cart.getCalculation(item_basket)
        return item_basket

    def getCalculation(self, item_basket):
        """funtion to calculate total dicount and total"""
        for index, row in item_basket.iterrows():
            item_basket['TotalDisc'] = item_basket['ActualDiscount']/100*item_basket['sub-total']
            item_basket['Total']= item_basket['sub-total'] - item_basket['TotalDisc']
            item_basket_group = item_basket.groupby(['basket'])[['sub-total','TotalDisc','Total',]].sum('Total')
            item_basket_group.round(2)
        details = cart.getBasketDetails(item_basket_group)
        return details


    
    def getBasketDetails(self,item_basket_group):
        """ print final basket price"""
        for basket in item_basket_group.index:
            print(f"Basket {basket} details : \n SubTotal is GBP {round(item_basket_group['sub-total'][basket],2)} \
            \n Discount is GBP {round(item_basket_group['TotalDisc'][basket],2)} \
            \n Total is GBP {round(item_basket_group['Total'][basket],2)}")

cart = Cart()
cart.getDetails()
