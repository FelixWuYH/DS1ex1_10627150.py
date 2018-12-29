import os
import sys
import time
import numpy as np

## 10627150 林易賢 ##


def Perm( i, array_size, number  ):						## number = int[], array_size = number-size, i = rotate-count 
	
	global Gstack										## recursion 計數器
	global counter  									## 編號計數器 
	Gstack = Gstack + 1									## each time call Perm, recursion-times + 1 
	size = array_size									## set size
	
		
	if i == size :										## each time finish rotate, go print number 	
		print( "[", counter,"](",end='' )				## print 流水編號 & "("
		for j in range( array_size ):					## print number(array) 
			print( number[j],end='' )					## print number(array) 
			i = j + 1									## to check number[j+1]  
			if i < array_size :							## if check number[j+1] not the last element in array 
				print( ",",end='')						## if true print "," 
		print( ")" )									## print "," 
		counter = counter + 1							## 編號計數器 + 1 
	else :
		for j in range( i, array_size ) :				## set j range 
			number[i],number[j] = number[j],number[i]	## change number[i] & number[j] element 
			Perm( i+1, array_size, number ) 			## rotate recursion 
			number[i],number[j] = number[j],number[i]	## change number[i] & number[j] element 



def Combin( k, n, list, size ):							## k = add element, n = add count, list = [], size = array_size
	
	number = []											## number宣告
	
	if n == 0 and len(list) == size :					## set array clear condition, to complete array call-by-reference 
		list.pop(size-1)								## clear element
	elif n != 0 and len(list) == size :					## set array clear condition, to complete array call-by-reference 
		for i in range(0,n+1):							## set array clear condition, to complete array call-by-reference 
			list.pop(size-i-1)							## clear element
		
	list.append(k)										## add element
	
	for i in range( k,10-n ) :							## set element-add condition
		if n > 0 :										## set element-add condition
			Combin( i+1, n-1, list, size )				## call Combin to add element
		
	if n == 0 :											## set print condition
		for i in range( 0, len(list) ) :				## set print condition
			number.append(list[i])						## update array
		Perm( n, size, number )							## print all the rotate

def Mission1():

	print( "輸入一個正整數 N , 程式會產生 1 ~ N 的所有排列 並計算最大遞迴層數 :" ) 	## mission introduce
	
	global Gstack										## recursion 計數器
	Gstack = 0											## Gstack 初始化 
	
	num =  int(input('請輸入一個正整數 N :')) 			## get 正整數 N, str in num ##
	number = []											## array  宣告
	zero = 1											## counter for initial array
	j = 0												## rotate-count = 0
	
	if num >= 1 :										## check if num -> 正整數 == true 
		array_size = num								## set array_size
		for i in range( 0, array_size ) :				## set rotate range 
			number.append(zero)							## number[zero] = zero + 1
			zero = zero + 1								## zero ++
		Perm( j, array_size, number )					## call Perm 
		print ( "遞迴層數 : ",end='' )					## print recursion-time
		print ( Gstack )								## print recursion-time
	
	else : 												## N 不等於正整數 ##
		print( "input error, back to the first page." ) ## print error
		
	return Which_Mission 								## return Which_Mission ##
	

def Mission2():
	print( "輸入一個正整數 M ( M介於 2 ~ 9 ) 接著再輸入 M 個相異數字",end='' )	## mission introduce
	print( "程式會產生這 M 個相異數字的各種排列 並測量執行時間" )				## mission introduce
	
	start = time.time()															## record start time 
	
	i = 0																		## counter for input 
	number = []																	## number 宣告
	num = int(input("請輸入一個正整數 M ( 介於 2 ~ 9 之間 ) :"))				## get 正整數 M
	
	if num >= 2 and num <= 9 :													## check if 2 <= num <=9, true 
	
		array_size = num														## set array_size
	
		while i < array_size :													## stop when input done
			j = int(input("再輸入 M 個相異數字 : "))							## get input
			if j <= 0 :															## check input if j <= 0
				print( "input error , back to the first page." ) 				## print error	
				return Which_Mission											## beck to Which_Mission
			number.append(j)													## add element to list
			i = i + 1															## count ++ 
		for i in range( 0, array_size ) :										## set i range
			for j in range( 0, array_size ) :									## set j range
				if number[i] == number[j] and i != j :							## check in input repeat
					print( "input error , back to the first page." ) 			## print error
					return Which_Mission										## bacck to Which_Mission
		i = 0																	## initial i
		
		if num >=2 and num <= 9 :												## if input correct
			Perm( i, array_size, number )										## call Perm
		
	else : 																		## M 不介於 2 ~ 9 之間 
		print( "input error , back to the first page." ) 						## print error
		
	end = time.time()															## record end time
	print( "程式執行時間 : ", end - start , " sec" )							## print spent-time
		
	return Which_Mission 														## return Which_Mission 
	
	
	
	
def Mission3():
	print( "輸入一個不大於9的正整數 M 程式會從1~9挑出M個相異數字產生各種排列 並測量執行時間" )	## mission introduce
	
	num = int( input("請輸入一個不大於9的正整數 : ") )							## get 正整數 M
	start = time.time()															## record start time 
	
	if num <= 9 and num >= 0 :													## check if 0 <= num <= 9
		list = []																## list 宣告
		for i in range( 0,10-num ):												## set array_size
			list.clear()														## each time call Combin reset, list[]
			if num > 0 :														## check if num > 0 
				Combin( i+1, num-1, list, num )									## call Combin
	else : 
		print( "input error , back to the first page." ) 						## print error

	end = time.time()															## record end time
	print( "程式執行時間 : ", end - start , " sec" )							## print spent-time	

	return Which_Mission 														## return Which_Mission 
		
def Which_Mission():

	global Gstack										## recursion 計數器
	Gstack = 0											## Gstack 初始化 
	global counter  									## 編號計數器 
	counter = 1											## counter 初始化 

	task = int(input("input mission choice ( 0, 1, 2, 3 ) :")) 	## GET mission number( 0, 1, 2, 3 ) 
	
	if task == 0 :  									## mission number == 0,
		return 											## leave 
	elif task == 1 :									## mission number == 1, 
		Mission1()										## call Mission1 
	elif task == 2 :									## mission number == 2,  
		Mission2()										## call Mission2
	elif task == 3 :									## mission number == 3,  
		Mission3()										## call Mission3
	else :												## illegal command,
		print( "input error, please try again" )		## print error,
		Which_Mission()									## return Which_Mission 


def main() :
				 
	global Gstack										## recursion 計數器
	Gstack = 0											## Gstack 初始化 
	global counter  									## 編號計數器 
	counter = 1											## counter 初始化 
	
	print( "Design To DS-week 1 - homework" )													## mission introduce
	print( "0. Quit " )																			## mission introduce
	print( "1. 輸入一個正整數N 產生1~N的所有排列 並計算最大遞迴層數" ) 							## mission introduce
	print( "2. 輸入M個相異正整數 M介於2和9之間 產生這M個相異數字的各種排列 並測量執行時間" ) 	## mission introduce
	print( "3. 輸入一個不大於9的正整數M 從1~9挑出M個相異數字產生各種排列 並測量執行時間" ) 		## mission introduce

	Which_Mission() 									## call Which_Mission 
	
     
main()													## main start