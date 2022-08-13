class Stack:
    def __init__(self) -> None:
        self.items=[]
    
    def isempty(self):
        return self.items==[]
    
    def push(self, item):
        self.items.insert(0,item)
    
    def pop(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[0]

class Solution:
    def isValid(self, s: str) -> bool:
        sta=Stack()
        ClosetoOpenMap={
            ")":"(", "}":"{","]":"["
        }
        for c in s:
            if c in ClosetoOpenMap:
                if not sta.isempty() and sta.peek()==ClosetoOpenMap[c]:
                    sta.pop()
                else:
                    return False
            else:
                sta.push(c)
        
        if sta.isempty():
            return True 
        else:
            return False
