import os #operating system作業系統

# 讀取檔案
def read_file(filename):
	products = [] #大清單
	with open(filename, 'r',encoding = 'utf-8') as f: #寫入或讀取都有編碼的問體所以要調整
		for line in f:
			if '商品,價格' in line:
				continue #'繼續'，只能在迴圈(5-8行為一個迴圈)中使用，意指跳到下一迴的意思(這一迴的迴圈不會執行7-8行)
			name, price= line.strip().split(',')#先把尾巴換行符號去掉，後再每一行遇到逗點就進行切割(split切割完會變成清單)
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		products.append([name, price]) #建立小清單，並裝入大清單中
	print(products) #印出大清單
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:#小清單
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w',encoding = 'utf-8') as f: #針對打開的檔案要進行編寫的動作，編寫並存成csv檔
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') #進行寫入_四個字串合併 '\n':空格以示換行 ',':要用逗點在excel檔才是分開兩隔

def main():
	# 檢查檔案
	filename = 'products.csv'
	if os.path.isfile(filename): #於os中使用path模組找尋有無此檔案(isfile)
		print('YEAH!找到檔案了!')
		products = read_file(filename)	
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()