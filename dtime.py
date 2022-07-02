a = int(input("Input number of times: "))
b = int(input("Input commands completed: "))
c1 = 35*a; c2 = 35*b; c3 = c1-b*35
print(f"It will take {c1}sec {c1/60:.3f}mins {c1/3600:.3f}hours")
print(f"It took {c2}sec {c2/60:.3f}mins {c2/3600:.3f}hours to execute")
print(f"It will take {c3}sec {c3/60:.3f}mins {c3/3600:.3f}hours until completion")
