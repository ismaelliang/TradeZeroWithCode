from pynput.mouse import Button, Controller as mController
from pynput.keyboard import Key, Controller as kController

import clipboard

from enum import Enum
import time


class MOUSE_POS(Enum):
    """
    Mouse position enumerater
    
    Config specific input or button's cursor position
    """
    TITLE_TICKER = (1365, 23)
    
    INPUT_TICKER = (1286, 57)
    INPUT_PRICE = (1273, 492)
    INPUT_QUANTITY = (1270, 462)
    INPUT_QUANTITY_COPY = (1331, 496)
    
    BTN_POSITION = (1282, 529)
    BTN_BUY = (1287, 551)
    BTN_SELL = (1371, 549)
    BTN_SHORT = (1466, 545)
    BTN_COVER = (1560, 549)
    
    def get_mouse_pos():
        '''
        Put your mouse on certain input or button,
        Run this function to get its position,
        Copy & paste it to config
        '''
        print('The current pointer position is {0}'.format(mController().position))

    
class TZController:
    
    __ms = mController()
    __kb = kController()
    
    def __init__(self):
        return
    
    def __time_break(self):
        time.sleep(0.1)
    
    def ticker(self, symbol):
        '''
        Change displaying ticker
        '''
        self.__ms.position = MOUSE_POS.TITLE_TICKER.value
        self.__ms.click(Button.left, 2)
        self.__time_break()

        self.__kb.type(symbol)
        self.__time_break()
        
        self.__kb.press(Key.enter)
        self.__kb.release(Key.enter)
        self.__time_break()
        
    def price(self, price):
        '''
        Set order price
        '''
        self.__ms.position = MOUSE_POS.INPUT_PRICE.value
        self.__ms.click(Button.left, 2)
        self.__time_break()
        
        self.__kb.type(str(price))
        self.__ms.position = MOUSE_POS.TITLE_TICKER.value
        self.__ms.click(Button.left)
        
    def qty(self, qty):
        '''
        Set order quantity
        '''
        self.__ms.position = MOUSE_POS.INPUT_QUANTITY.value
        self.__ms.click(Button.left, 2)  
        self.__time_break()
        
        self.__kb.type(str(qty))
        self.__ms.position = MOUSE_POS.TITLE_TICKER.value
        self.__ms.click(Button.left)
        
    def lmt(self, qty, price):
        '''
        Prepare lmt order with qty/price
        '''
        self.qty(qty)
        self.price(price)
        
    def buy(self):
        '''
        Click BUY button
        '''
        self.__ms.position = MOUSE_POS.BTN_BUY.value
        self.__ms.click(Button.left)
        
    def sell(self):
        '''
        Click SELL button
        '''
        self.__ms.position = MOUSE_POS.BTN_SELL.value
        self.__ms.click(Button.left)
        
    def short(self):
        '''
        Click SHORT button
        '''
        self.__ms.position = MOUSE_POS.BTN_SHORT.value
        self.__ms.click(Button.left)
        
    def cover(self):
        '''
        Click COVER button
        '''
        self.__ms.position = MOUSE_POS.BTN_COVER.value
        self.__ms.click(Button.left)
        
    def cur_pos(self):
        '''
        Return current position size for current ticker
        '''
        self.__ms.position = MOUSE_POS.INPUT_QUANTITY.value
        self.__ms.click(Button.left, 2)
        self.__time_break()
        
        self.__ms.click(Button.right)
        self.__time_break()
        
        self.__ms.position = MOUSE_POS.INPUT_QUANTITY_COPY.value
        self.__ms.click(Button.left)
        self.__time_break()
        return clipboard.paste()
        