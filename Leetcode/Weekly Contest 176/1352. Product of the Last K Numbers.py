# Question Link:- https://leetcode.com/contest/weekly-contest-176/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    def __init__(self):
        self.pre = [1]
        

    def add(self, num: int) -> None:
        
        # reset product table after 0 is insert
        if num==0:
            self.pre = [1]
        
        # update product table if num is non-zero.
        else:
            self.pre.append(self.pre[-1]*num)
        
    def getProduct(self, k: int) -> int:
        
        #  last k elements include at least one zero, which was inserted before getProduct() query
        if k>=len(self.pre):
            return 0
        
        # compute the product of last k elemetns by look-up table
        else:
            return self.pre[-1]//self.pre[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
