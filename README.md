## What is this?
Use code to make mouse & keyboard actions
to use TradeZero to trade

## Warning
Be responsible for your own actions.
When you call Buy/Sell function, it may execute real trade

## Install dependencies
cd TradeZeroWithCode && pip install -r requirements.txt

## Config your intut/button positions
def get_mouse_pos():
    '''
    Put your mouse on certain input or button,
    Run this function to get its position,
    Copy & paste it to config
    '''
    print('The current pointer position is {0}'.format(mController().position))