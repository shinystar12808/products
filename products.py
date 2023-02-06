products = [] #大清單
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price]) 
print(products) #印出大清單

for p in products:
	print(p) #印出每一個小清單
	print(p[0], '的價格是', p[1])

# 'abc' + '123' = 'abc123' 字串可以合併
#'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding = 'utf-8') as f: #針對打開的檔案要進行編寫的動作
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #進行寫入_四個字串合併 '\n':空格以示換行 ',':要用逗點在excel檔才是分開兩隔

