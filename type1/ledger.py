import pandas as pd
import numpy as np

def calculateRow(stocked,ordered,incoming,backlog=0,outcoming=None,total_order=None):
    총수요 = ordered + backlog
    입고 = incoming
    재고 = stocked
    주문 = ordered
    이전부족재고 = backlog
    출고전_총재고 = 입고 + 재고
    출고량 = 총수요 if(outcoming is None) else outcoming
    출고량 = 총수요
    
    출고량 = min(출고량,min(총수요,출고전_총재고))
    if(출고량>20):
        출고량 = 20
    현재총재고 = 출고전_총재고 - 이전부족재고
    if(총수요>출고전_총재고):
        재고 = 0
        부족재고 = 총수요 - 출고량
    else:
        부족재고 = 0
        재고 = 출고전_총재고 - 출고량
    
    if(total_order is None):
        총주문량 = 0
    else:
        총주문량 = total_order
    잔량 = 1 if (부족재고>0) else 0
    총주문량 = 총주문량 - 잔량
    
    출고량 = 출고량 - 잔량
    if(부족재고>0):
        부족재고 += 1
    
    return [입고,출고전_총재고,주문,총수요,출고량,부족재고,재고,총주문량]

class Ledger:
    def __init__(self):
        super().__init__()
        self._columns = ["입고","출고전_총재고","주문","총수요","출고량","부족재고","재고","총주문량"]
        self._ledger = pd.DataFrame(columns=self._columns)
        
    def reset(self):
        del self._ledger
        self._ledger = pd.DataFrame(columns=self._columns)
    def appendLedgerRow(self,row_dict):
        self._ledger.loc[len(self._ledger)] = row_dict
    def appendRow0(self):
        #stocked,ordered,incoming,backlog=0
        row = calculateRow(stocked=12,ordered=np.random.randint(1,10),incoming=np.random.randint(1,5),backlog=0)
        row = dict(list(zip(self._columns,row)))
        self.appendLedgerRow(row)
    def getLedger(self):
        return self._ledger
    def getLedgerAsNumpy(self):
        return self._ledger.to_numpy()
    def getLastLedgerRow(self):
        return self._ledger.iloc[-1]