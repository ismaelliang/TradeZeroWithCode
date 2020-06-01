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
    BTN_CANCEL = (1369, 527)
    
    CDT_INPUT_TICKER = (71, 50)
    
    CDT_1st_ACTION_SEL = (122, 140)
    CDT_1st_ACTION_BUY = (85, 158)
    CDT_1st_ACTION_SHORT = (81, 195)
    CDT_1st_INPUT_QTY = (182, 142)
    CDT_1st_TYPE_SEL = (326, 141)
    CDT_1st_TYPE_LIMIT = (299, 176)
    CDT_1st_INPUT_PRICE = (193, 173)
    
    CDT_2nd_ACTION_SEL = (120, 259)
    CDT_2nd_ACTION_SELL = (76, 296)
    CDT_2nd_ACTION_COVER = (83, 331)
    CDT_2nd_INPUT_QTY = (191, 262)
    CDT_2nd_TYPE_SEL = (326, 260)
    CDT_2nd_TYPE_RANGE = (290, 385)
    CDT_2nd_INPUT_HIGH_PRICE = (407, 297)
    CDT_2nd_INPUT_LOW_PRICE = (518, 296)
    
    CDT_BTN_SEND = (93, 356)
    CDT_BTN_CANCEL = (245, 355)
    

    
class TZController:
    
    __ms = mController()
    __kb = kController()
    
    _origin_pos = None
    
    def __init__(self):
        return
    
    '''
    Some basic functions
    '''
    def __time_break(self):
        time.sleep(0.1)
        
    def _click(self, pos):
        self.__ms.position = pos.value
        self.__ms.click(Button.left)
        self.__time_break()
        
    def _dbl_clk(self, pos):
        self.__ms.position = pos.value
        self.__ms.click(Button.left, 2)
        self.__time_break()
        
    def _r_click(self, pos):
        self.__ms.position = pos.value
        self.__ms.click(Button.right)
        self.__time_break()
        
    def _typein(self, text):
        self.__kb.type(text)
        self.__time_break()
        
        self.__kb.press(Key.enter)
        self.__kb.release(Key.enter)
        self.__time_break()
        
        
    '''
    Regular Order Actions
    '''    
    def ticker(self, symbol):
        '''
        Change ticker for regular order & chartingd window
        '''
        self._dbl_clk( MOUSE_POS.TITLE_TICKER )
        self._typein(symbol)        
        
    def price(self, price):
        '''
        Set order price
        '''
        self._dbl_clk( MOUSE_POS.INPUT_PRICE )
        self._typein(str(price))
        self._click( MOUSE_POS.TITLE_TICKER )
        
    def qty(self, qty):
        '''
        Set order quantity
        '''
        self._dbl_clk( MOUSE_POS.INPUT_QUANTITY )
        self._typein(str(qty))
        self._click( MOUSE_POS.TITLE_TICKER )
        
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
        self._click( MOUSE_POS.BTN_BUY )
        
    def sell(self):
        '''
        Click SELL button
        '''
        self._click( MOUSE_POS.BTN_SELL )
        
    def short(self):
        '''
        Click SHORT button
        '''
        self._click( MOUSE_POS.BTN_SHORT )
        
    def cover(self):
        '''
        Click COVER button
        '''
        self._click( MOUSE_POS.BTN_COVER )
        
    def cancel(self):
        '''
        Click CANCEL button
        '''
        elf.__ms.position = MOUSE_POS.BTN_CANCEL.value
        self.__ms.click(Button.left)
    
    '''
    Conditional Order Actions
    '''
    def cdt_ticker(self, symbol):
        '''
        Change ticker in Condition order window
        Ensure condition order window opening
        '''
        self._dbl_clk( MOUSE_POS.CDT_INPUT_TICKER )
        self._typein(symbol)  
        
    def cdt_buy_then_sell(self, target, stop, price, qty):
        '''
        Conditional order 1
        '''
        self._click( MOUSE_POS.CDT_1st_ACTION_SEL )
        self._click( MOUSE_POS.CDT_1st_ACTION_BUY )
        
        self._click( MOUSE_POS.CDT_1st_TYPE_SEL )
        self._click( MOUSE_POS.CDT_1st_TYPE_LIMIT )
        
        self._dbl_clk( MOUSE_POS.CDT_1st_INPUT_QTY )
        self._typein(str(qty))
        
        self._dbl_clk( MOUSE_POS.CDT_1st_INPUT_PRICE )
        self._typein(str(price))
        
        '''
        Conditional order 2
        '''
        self._click( MOUSE_POS.CDT_2nd_ACTION_SEL )
        self._click( MOUSE_POS.CDT_2nd_ACTION_SELL )
        
        self._click( MOUSE_POS.CDT_2nd_TYPE_SEL )
        self._click( MOUSE_POS.CDT_2nd_TYPE_RANGE )
        
        self._dbl_clk( MOUSE_POS.CDT_2nd_INPUT_QTY )
        self._typein(str(qty))
        
        self._dbl_clk( MOUSE_POS.CDT_2nd_INPUT_HIGH_PRICE )
        self._typein(str(target)) # higher price as target
        
        self._dbl_clk( MOUSE_POS.CDT_2nd_INPUT_LOW_PRICE )
        self._typein(str(stop)) # lower price as stop
        
    def cdt_short_then_cover(self, target, stop, price, qty):
        '''
        Conditional order 1
        '''
        self._click( MOUSE_POS.CDT_1st_ACTION_SEL )
        self._click( MOUSE_POS.CDT_1st_ACTION_SHORT )
        
        self._click( MOUSE_POS.CDT_1st_TYPE_SEL )
        self._click( MOUSE_POS.CDT_1st_TYPE_LIMIT )
        
        self._dbl_clk( MOUSE_POS.CDT_1st_INPUT_QTY )
        self._typein(str(qty))
        
        self._dbl_clk( MOUSE_POS.CDT_1st_INPUT_PRICE )
        self._typein(str(price))
        
        '''
        Conditional order 2
        '''
        self._click( MOUSE_POS.CDT_2nd_ACTION_SEL )
        self._click( MOUSE_POS.CDT_2nd_ACTION_COVER )
        
        self._click( MOUSE_POS.CDT_2nd_TYPE_SEL )
        self._click( MOUSE_POS.CDT_2nd_TYPE_RANGE )
        
        self._dbl_clk( MOUSE_POS.CDT_2nd_INPUT_QTY )
        self._typein(str(qty))
        
        self._dbl_clk( MOUSE_POS.CDT_2nd_INPUT_HIGH_PRICE )
        self._typein(str(stop)) # higher price as stop
        
        self._dbl_clk( MOUSE_POS.CDT_2nd_INPUT_LOW_PRICE )
        self._typein(str(target)) # lower price as target
         
    def cdt_send(self):
        self._click( MOUSE_POS.CDT_BTN_SEND )
        
    def cdt_cancel(self):
        self._click( MOUSE_POS.CDT_BTN_CANCEL )
    
        
    '''
    Get
    '''
    def cur_pos(self):
        '''
        Return current position size for current ticker
        '''
        self._dbl_clk( MOUSE_POS.INPUT_QUANTITY )
        self._r_click( MOUSE_POS.INPUT_QUANTITY )
        self._click( MOUSE_POS.INPUT_QUANTITY_COPY )
        return clipboard.paste()
        
        
    def get_mouse_pos(self):
        '''
        Put your mouse on certain input or button,
        Run this function to get its position,
        Copy & paste it to config
        '''
        print('The current pointer position is {0}'.format(mController().position))