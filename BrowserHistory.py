# problem 1472

class BrowserHistory:

    def __init__(self, homepage: str):
        self.browserlist = [homepage]
        self.currentindex = 0

    def visit(self, url: str) -> None:
        if self.currentindex == len(self.browserlist) - 1:
            self.browserlist.append(url)
        else:
            self.browserlist[self.currentindex + 1] = url
        
        self.currentindex = self.currentindex + 1
        self.browserlist = self.browserlist[:self.currentindex + 1]

    def back(self, steps: int) -> str:
        min = self.currentindex if steps > self.currentindex else steps
        self.currentindex = self.currentindex - min
        return self.browserlist[self.currentindex]

    def forward(self, steps: int) -> str:
        lengthfromend = len(self.browserlist) - 1 - self.currentindex
        min = len(self.browserlist) - 1 if lengthfromend < steps else self.currentindex + steps
        self.currentindex = min
        return self.browserlist[self.currentindex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
Console
