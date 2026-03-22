class Node:
    def __init__(self, val):
        self.val= val
        self.next= None
        self.prev= None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current= Node(homepage)

    def visit(self, url: str) -> None:
        self.current.next= None
        visit_url= Node(url)
        self.current.next= visit_url
        visit_url.prev= self.current
        self.current= visit_url


    def back(self, steps: int) -> str:
        
        for i in range(steps):
            if self.current.prev:
                self.current= self.current.prev
            else:
                break
        return self.current.val

    def forward(self, steps: int) -> str:
        
        for i in range(steps):
            if self.current.next:
                self.current= self.current.next
            else:
                break
        return self.current.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)