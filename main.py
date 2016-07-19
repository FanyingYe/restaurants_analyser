from Analyser import Analyser

productsPath = ""
salesPath = ""

productsPath = raw_input("Please input the path of products.tab: ")
salesPath = raw_input("Please input the path of sales.tab: ")

analyzer = Analyser(productsPath, salesPath)

topNumber = input("Please input the top number: ")
analyzer.findTopCategories(topNumber)
analyzer.findBestSaleCandy()
