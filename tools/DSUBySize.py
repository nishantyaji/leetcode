# Python program for the above approach
class UnionFind:
    def __init__(self, n):
        # Initialize Parent array
        self.Parent = list(range(n))

        # Initialize Size array with 1s
        self.Size = [1] * n

    # Function to find the representative (or the root node) for the set that includes i
    def find(self, i):
        if self.Parent[i] != i:
            # Path compression: Make the parent of i the root of the set
            self.Parent[i] = self.find(self.Parent[i])
        return self.Parent[i]

    # Unites the set that includes i and the set that includes j by size
    def unionBySize(self, i, j):
        # Find the representatives (or the root nodes) for the set that includes i
        irep = self.find(i)

        # And do the same for the set that includes j
        jrep = self.find(j)

        # Elements are in the same set, no need to unite anything.
        if irep == jrep:
            return

        # Get the size of i’s tree
        isize = self.Size[irep]

        # Get the size of j’s tree
        jsize = self.Size[jrep]

        # If i’s size is less than j’s size
        if isize < jsize:
            # Then move i under j
            self.Parent[irep] = jrep

            # Increment j's size by i's size
            self.Size[jrep] += self.Size[irep]
        # Else if j’s size is less than i’s size
        else:
            # Then move j under i
            self.Parent[jrep] = irep

            # Increment i's size by j's size
            self.Size[irep] += self.Size[jrep]


# Example usage
n = 5
unionFind = UnionFind(n)

# Perform union operations
unionFind.unionBySize(0, 1)
unionFind.unionBySize(2, 3)
unionFind.unionBySize(0, 4)

# Print the representative of each element after unions
for i in range(n):
    print("Element {}: Representative = {}".format(i, unionFind.find(i)))

# check problem 1759