def pyramid(h):
    for i in range(h):
        for j in range(h-i-1):
          print(" ", end="")
        for j in range(i,0,-1):
          if j!=0:
              print(j+1, end="")
        for j in range(i + 1):
          print(j + 1, end="")
        print("")

pyramid(5)