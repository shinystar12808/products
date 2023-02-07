import os #operating system作業系統

products = [] #大清單
# 檢查檔案後，若有就讀取檔案
if os.path.isfile('products.csv'): #於os中使用path模組找尋有無此檔案(isfile)
	print('YEAH!找到檔案了!')
	with open('products.csv', 'r',encoding = 'utf-8') as f: #寫入或讀取都有編碼的問體所以要調整
		for line in f:
			if '商品,價格' in line:
				continue #'繼續'，只能在迴圈(5-8行為一個迴圈)中使用，意指跳到下一迴的意思(這一迴的迴圈不會執行7-8行)
			name, price= line.strip().split(',')#先把尾巴換行符號去掉，後再每一行遇到逗點就進行切割(split切割完會變成清單)
			products.append([name, price]) 
	print(products)
else:
	print('找不到檔案.....')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p1roducts.append([name, price]) #建立小清單，並裝入大清單中
print(products) #印出大清單

# 印出所有購買紀錄
for p in products:#小清單
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w',encoding = 'utf-8') as f: #針對打開的檔案要進行編寫的動作，編寫並存成csv檔
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #進行寫入_四個字串合併 '\n':空格以示換行 ',':要用逗點在excel檔才是分開兩隔

