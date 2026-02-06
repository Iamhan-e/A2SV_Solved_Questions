import sys

def solve():
   
    s = sys.stdin.readline().strip()

    
    first_ab = s.find("AB")
    if first_ab != -1 and s.find("BA", first_ab + 2) != -1:
        print("YES")
        return

    
    first_ba = s.find("BA")
    if first_ba != -1 and s.find("AB", first_ba + 2) != -1:
        print("YES")
        return

    
    print("NO")

if __name__ == "__main__":
    solve()