if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
    grid= [[k,l,m] for k in range(x+1) for l in range(y+1)for m in range(z+1) if(k+l+m)!=n]
    
    print(grid)
