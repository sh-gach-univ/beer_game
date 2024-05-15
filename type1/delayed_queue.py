class DelayedQueue:
    def __init__(self):
        super().__init__()
        self._delay_slot = []#None,]*2
        self._order_amount = None
    def putDelay(self,value):
        self._delay_slot = [value]+self._delay_slot
        
    def getDelayed(self):
        value = None
        if(len(self._delay_slot)>0):
            value = self._delay_slot.pop(-1)
        
        return value
    def reset(self):
        self._delay_slot = []
        self._order_amount = None
    def getOrderAmount(self):
        value = self._order_amount
        self._order_amount = None
        return value
    def putOrderAmount(self,value):
        self._order_amount = value