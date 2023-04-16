"請設計一個函數，輸入為數字，輸出則為*符號為輸入數字邊長的空心正三角形。輸入: 3"

x = int(input('請輸入空心正三角形的數字邊長'))
for u in range(x + 1):
    for i in range(x + 1 - u):
        print(' ', end='')
    for j in range(u):
        print('* ', end='')
    print('\n', end='')