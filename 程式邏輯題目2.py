'國泰國中的老師出了一道題目給同學們練習，同學們自己設定一串奇偶混和地亂數，並將數字依照” 奇數都在偶數前面”，且”偶數升冪排序”，”奇數降冪排序”。'
'例如 ‘417324689435’ 將會變成 ‘975331244468’。'
'然而，班上有50位學生，每一個同學給出的數字長度不一，老師希望能用一段小程式來幫助他驗證答案，請你寫一個函數幫幫老師吧!'


number = "417324689435"
int_list = []
for num in number:
    int_list.append(int(num))       #將 417324689435 放進 list
even = []
odd = []
for number in int_list:         #將 list 的數字除2,來判斷是否為偶數
    if number % 2 == 0:
        even.append(number)     #除盡的為偶數並放進 even
    else:
        odd.append(number)      #除不盡的為基數放進 odd
even.sort()                     #偶數由小到大排序
odd.sort(reverse=True)          #基數由大到小排序
total=(odd+even)                #將基數與偶數合併
for i in range (len(total)):    #迴圈列印答案
   print(str(total[i]),end="")