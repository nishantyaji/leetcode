array = []  # input array
x = 0  # desired value
start, end = 0, 10 ** 7
while start <= end:
    mid = (start + end) // 2
    if array[mid] == x:
        # x found at mid
        # return mid
        pass
    if array[mid] > x:
        end = mid - 1
    else:
        start = mid + 1

# ------------------------------------------------


k = 0
array = []
n = 10 ** 7  # size of the array

end = n // 2
while end >= 1:
    while end + k < n and array[k + end] <= x:
        k += end
    end = end // 2

if array[k] == x:
    # found at index k
    pass

# ------------------------------------------------

"""
Finding the smallest solution
An important use for binary search is to find the position where the value of a
function changes. Suppose that we wish to find the smallest value k that is a
valid solution for a problem. We are given a function ok(x) that returns true if x
is a valid solution and false otherwise. In addition, we know that ok(x) is false
when x < k and true when x ≥ k. The situation looks as follows:
x    | 0     | 1     |··· | k −1  | k    | k +1 ···
ok(x)| false | false |··· | false | true | true ···
Now, the value of k can be found using binary search:

"""
def ok(num: int):
    return True
    # return False

x = -1
end = 10**7 # max(array)
while end >= 1:
    while not ok(x + end):
        x += end
    end = end // 2

print("Result: ", x + 1)

"""
The search finds the largest value of x for which ok(x) is false. Thus, the next
value k = x+1 is the smallest possible value for which ok(k) is true. The initial
jump length z has to be large enough, for example some value for which we know
beforehand that ok(z) is true.
"""
#------------------------------------------------
"""
Finding the maximum value
Binary search can also be used to find the maximum value for a function that is
first increasing and then decreasing. Our task is to find a position k such that
• f (x) < f (x+1) when x < k, and
• f (x) > f (x+1) when x ≥ k.
The idea is to use binary search for finding the largest value of x for which
f (x) < f (x+1). This implies that k = x+1 because f (x+1) > f (x+2). The following
code implements the search:
"""
def f(num: int):
    return -1

x = -1
end = 10**7  # max(array)
while end >= 1:
    while f(x) < f(x+end+1):
        x += end

print("Result is", x+1)

"""
Note that unlike in the ordinary binary search, here it is not allowed that
consecutive values of the function are equal. In this case it would not be possible
to know how to continue the search.
"""
