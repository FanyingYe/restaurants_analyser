import os, re
import numpy as np
import matplotlib
matplotlib.rc('xtick', labelsize=8) 
import matplotlib.pyplot as plt


class Analyser:

	# Constructor
	# Input: 
	#	productsPath: file path of products.tab
	#	salesPath: file path of sales.tab
	def __init__(self, productsPath, salesPath):

		# self._products: 
		#	a dictionary, where key is product name and value is its category
		self._products = {}
		# self._sales: 
		#	a dictionary, where key is product name and value is its total sale amount
		self._sales = {}

		f_products = open(productsPath, 'r')
		for i, line in enumerate(f_products):
			product = line.rstrip('\n').split('\t')
			if len(product) < 2:
				continue
			else:
				self._products[product[0]] = product[1]
		f_products.close()

		f_sales = open(salesPath, 'r')		
		for i, line in enumerate(f_sales):
			sale = line.rstrip('\n').split('\t')
			if self._sales.has_key(sale[0]):
				self._sales[sale[0]] = self._sales[sale[0]] + float(sale[1])
			else:
				if len(sale) < 2:
					continue
				else:
					self._sales[sale[0]] = float(sale[1])
		f_sales.close()


	def findTopCategories(self, topNumber):
		# Category_Sale: 
		#	a dictionary, where key is category and value is its total sale amount
		Category_Sale = {}

		# Traverse self._products, 
		# find its sales amount in self._products, 
		# add its sales amount to according category in Category_Sale
		for i in self._products:
			if self._sales.has_key(i):
				if Category_Sale.has_key(self._products[i]):
					Category_Sale[self._products[i]] = Category_Sale[self._products[i]] + self._sales[i]
				else:
					Category_Sale[self._products[i]] = self._sales[i]

		li = sorted(Category_Sale.iteritems(), key = lambda d:d[1], reverse = True)

		# xtick label
		topCategoryName = []
		# bar value
		topCategorySale = []

		# if user want to find top N category where N is bigger than total categories we have
		# just return all we have
		liLength = len(li)
		if topNumber > liLength:
			topNumber = liLength
		for i in range(0, topNumber):
			topCategoryName.append(li[i][0])
			topCategorySale.append(li[i][1])
			print li[i]
		for i in range(topNumber,liLength):
			topCategoryName.append(li[i][0])
			topCategorySale.append(li[i][1])

		# Plot sorted list of category sales
		index = np.arange(liLength)
		bar_width = 1.0
		opacity = 0.5

		topCategoryBar = plt.bar(index, topCategorySale, bar_width, alpha = opacity, color = 'b')
		plt.xlabel('Category')
		plt.ylabel('Sales')
		plt.title('Top Category in sales') 
		plt.xticks(index + bar_width/2, topCategoryName,rotation=20)
		plt.show()

	def findBestSaleCandy(self):
		
		maxProduct = ''
		maxSale = 0

		productName = []
		# bar value
		productSale = []

		# Traverse self._sales
		# Find current product's category in self._prodcuts,
		# If its categort is Candy and sale amount is bigger than current maxSale
		# set maxSale and maxProduct 
		for i in self._sales:
			if self._products.has_key(i) and self._products[i] == 'Candy':
				productName.append(i)
				productSale.append(self._sales[i])
				if self._sales[i] > maxSale:
					maxSale = self._sales[i]
					maxProduct = i

		print maxProduct + ': ', maxSale

		# Plot
		index = np.arange(len(productName))
		bar_width = 1.0
		opacity = 0.5

		topCategoryBar = plt.bar(index, productSale, bar_width, alpha = opacity, color = 'b')
		plt.xlabel('Candy product sale')
		plt.ylabel('Sales')
		plt.title('Candy sales') 
		plt.xticks(index + bar_width/2, productName,rotation=90)
		plt.show()


























