import pytest
import Webscrapper

#Test if the list returns from GetConsoles contains a title and price column
def test_GetConsoles():
    containsTitle = False
    containsPrice = False

    list1 = Webscrapper.GetConsoles()
    
    try:
        if(len(list1[0]["title"]) > 0):
            containsTitle = True
        
        if(len(list1[0]["price"]) > 0):
            containsPrice = True
    except:
        print("fail")
      
    assert containsTitle and containsPrice 