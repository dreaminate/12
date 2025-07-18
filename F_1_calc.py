p=float(input("请输入precision值："))
r=float(input("请输入recall值："))
F_1=2*(p*r/(p+r))
print("F_1值为：",F_1)