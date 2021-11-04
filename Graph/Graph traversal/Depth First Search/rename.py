import os


def solve():
    def rename(s):
        return s.replace(' ', '_')
    path = r"C:\Users\ranja\My Projects\CP-Algorithms\Data_Structures\Fundamentals\Minimum Stack-Minimum Queue"
    for filename in os.listdir(path):
        if filename != ".git":
            print(filename)
            os.rename(os.path.join(path, filename),
                      os.path.join(path, rename(filename)))


solve()
