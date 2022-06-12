import os
import math


class HackerRankTests():


    def __init__(self):
        self.Me = self
        self.IntArr = []
        pass

    def avg(strArgs) -> float:
        lArgs =  strArgs.split(' ')  #"{:.2f}".format(strArgs.split(' '))
        fArgs = []

        print(strArgs)
        print(lArgs)

        for i in lArgs:
            fArgs.append(float(i))
            pass

        print(fArgs)

        soma = sum(fArgs)
        qtde = len(fArgs)

        result = 0.00
        result = "%.2f" % (soma / qtde)
        return result
        pass
    
    def sockMerchant(n, ar):
        n=9
        ar=[10, 20, 20, 10, 10, 30, 50, 10, 20, 20, 30]
        ar.sort()
        par=0
        arb = []
        
        for i in ar:
            if (i in arb) == False:
                arb.append(i)

        results = 0
        xpto = [] 

        for x in arb:
            xpto.append([x,ar.count(x)])
            pass

        for xx in xpto:
            divs = xx[1] // 2
            if divs > 0:
                results = results + divs
        pass
        
        return results
        pass

    def countingValleys(steps, path):
        steps = 1000000
        path = ""
        Mar = 2500
        MarAntes = Mar

        if steps > 2 and steps <= 1000000:
            args = []
            args = ",".join(path).split(",")
            limit = 0
            sinal = 0

            for i in args:
                if limit <= steps:
                    limit = limit + 1 
                if i == "U":
                    Mar = Mar + 1
                elif i == "D":
                    Mar = Mar - 1

                if Mar < 2500 and MarAntes >= 2500:
                    sinal = sinal +1
                    MarAntes = Mar
                elif Mar >= 2500 and MarAntes < 2500:
                    #sinal = sinal + 1
                    MarAntes = Mar
                    #print(mais)
                    #print(menos)
                    #print(sinal)
        # Write your code here
        return sinal
        pass

        #args = input("Entre com os valores espaçados...: ")
        #print(avg(args))
        #print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
        #print(countingValleys(0,""))
        pass

    def fibn(self, var) -> int:
        if var <= 1:  
            print(var)
            return var
        else:
            return self.fibn(var=var-1) + self.fibn(var=var-2)
        pass #End of fibonattiRecursive(n)


    
    def fibonacci(self, var):
        IntArr = [0,1]
        Tam = len(IntArr)
        result = sum(IntArr)
        Index = 0
        while sum(IntArr) < var:
            result = IntArr[Tam-2]+IntArr[Tam-1]

            IntArr.append(result)
            Tam = len(IntArr)
            #result = IntArr[Tam-2]+IntArr[Tam-1]+IntArr[Tam]
            pass #while
        return IntArr
        pass #fibonacci
       
        
        pass #End of fibonattiRecursive(n)
	#print(self.IntArr)

    #n = int(input().strip())
    #c = [int(c_temp) for c_temp in input().strip().split(' ')]

    def jumpingOnClouds(c):
        n=len(c)
        res = 0
        i = 0
        while i < n-1:
            if i+2<n and c[i+2] == 0:
                i = i+2
                res += 1
            else:
                i = i+1
                res += 1
                #print(res)
        return res
        pass
    #print(jumpingOnClouds(c))


    #s='bab'
    #n=725261545450
    #resposta: 241753848483

    #s='a'
    #n=1000000000000

    #s='beeaabc'
    #n=711560125001
    #resposta:203302892858

    #s='aadcdaccacabdaabadadaabacdcbcacabbbadbdadacbdadaccbbadbdcadbdcacacbcacddbcbbbaaccbaddcabaacbcaabbaaa'
    #n=942885108885
    #resposta:330009788107

    def repeatedString(s, n):
        i=0
        ret=0
        tam = len(s)
        rest = 0.000000
        sr = ''
        ret2 = 0

        if tam <= 100 and n <= 1000000000000 and 'a' in s:
            if tam > 1:
                for i in range(0,tam):
                    if s[i]=='a':
                        ret=ret+1
                        rest = (n/tam) % 1
                        ret = (((n/tam) - rest) * ret)
                        sr = s[0:round(tam * rest)]
            i=0
            for i in range(0,len(sr)):
                if s[i]=='a':
                    ret2 = ret2 + 1
        elif len(s) == 1:
            ret = n
        return round(ret + ret2)
        pass
        #print(repeatedString(s,n))


    #arr = [[1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]]
    #arr = [[1, 1, 1, 0, 0, 0],[0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 9, 2, -4, -4, 0],[0, 0, 0, -2, 0, 0],[0, 0, -1, -2, -4, 0]]
    #arr = [[-1, -1, 0, -9, -2, -2],[-2, -1, -6, -8, -2, -5],[-1, -1, -1, -2, -3, -4],[-1, -9, -2, -4, -4, -5],[-7, -3, -3, -2, -9, -9],[-1, -3, -1, -2, -4, -5]]
    def hourglassSum(arr):
        hglss=[]
        i=0
        result=0
        valor=0
        first=1
        for z in range(0,4):
            i=0
            while i <= 3:
                hglss.append([arr[z][i], arr[z][i+1], arr[z][i+2], arr[z+1][i+1], arr[z+2][i], arr[z+2][i+1], arr[z+2][i+2]])
                i = i+1
                pass

        #print(hglss)
        for ix in hglss:
            valor=0
            for num in ix:
                valor += round(float(num))

        if valor > result or first == 1:
            first = 0
            result = valor
        pass

        return result
        pass
    #print(hourglassSum(arr))


    def rotLeft(a, d):
        tam = len(a)
        x = d/tam
        x1 = round(d % tam)
        b = a * 2
        result = ""

        if d <= 100000 and tam <= 1000000:
            a.clear()
            for x1 in range(x1,x1+tam):
                a.append(b[x1])

        #print(a) #[2, 3, 4, 5]
        return print(*a)
        pass #FIM
    

    #a=[1,2,3,4,5]
    #d=54
    #print(rotLeft(a,d))
    #6 4
    magazine = "give me one grand today night"
    note = "give one grand today"
    def checkMagazine(magazine, note):
        h1 = {}
        h2 = {}
        arrM = magazine.split(' ')
        arrN = note.split(' ')

        ret = 'No'

        i=0
        for m in arrM:
            h1[i] = m
            i = i+1


        i=0
        for n in arrN:
            h2[i] = n
            i = i+1


        l1 = len(h1)
        l2 = len(h2)

        loopH = 0
        if l1 < l2:
            loopH = l1
        else:
            loopH = l2

        count=0
        for loop in range(0,loopH):
            if h1[loop] == h2[loop]:
                count = count + 1

        if count > l1/2:
            ret = 'Yes'


        print(h1)
        print(h2)

        return ret
        pass
    #print(checkMagazine(magazine, note))

    #n = 3
    #a = [1, 2, 3]

    def countSwaps(a):
        tam = len(a)
        nswp = 0
        if n >= 2 and n <= 600:
            if tam >= 1 and tam <= 2000000:
                for final in range(tam,0,-1):
                    for current in range(0,tam-1):
                        if a[current] > a[current+1]:
                            a[current], a[current+1] = a[current+1], a[current]
                            nswp = nswp + 1
                    pass
                pass
            pass
        pass

        strg = "Array is sorted in " + str(nswp) + " swaps.\nFirst Element: " + str(a[0]) + "\nLast Element: " + str(a[tam-1])
        #print(strg)
        #return a
        return strg
        pass #FIM
    #print(countSwaps(a))

    def sobras():
        var1 = 0
        var2 = 0.0
        var3 = ""
        i = 4
        d = 4.0
        s = 'HackerRank '

        var1 = int(input("Entre com o valor inteiro..:"))
        var2 = float(input("Entre com o valor double...:"))
        var3 = str(input("Entre com a string.........:"))

        var1 = var1 + i
        var2 = var2 + d

        print(str(var1))
        print(str(var2))
        print(s + var3)

        pass

    #expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    #d = "9 5"


    def activityNotifications(expenditure, d):
        print("")
        pass


#BTG 


#samDaily = 3
#kellyDaily = 5
#difference = 1

def minNum(samDaily, kellyDaily, difference):
    # Write your code here
    intI = 1
    samSolved = samDaily + difference
    kellySolved = kellyDaily
        
    while kellySolved <= samSolved:
        samSolved += samDaily
        kellySolved += kellyDaily
        intI += 1
        pass #while
    print(intI)
    pass #####


####minNum(samDaily, kellyDaily, difference)


def BinFunc(numberInt):
    i = 0
    Bin = bin(numberInt)
    tam = len(Bin) - 3
    result = ""
    for cDigit in Bin:
        i = i+1 
        if i==tam:
            result = cDigit
            print(cDigit)
    pass #BinFunc


###BinFunc(77)


#Hk = HackerRankTests()
#print(Hk.fibonacci(5))



def reverseArray(arr):
    # Write your code here
    arr.reverse()
    return arr
    pass #reverse


#AR = [5,1,3,2,4,5]
#print(reverseArray(AR))


def divided(arr):
    # Write your code here
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    out = []
    p1 = arr[1][0] + arr[2][0] + arr[2][1] + arr[3][0] + arr[3][1] + arr[4][0]
    p2 = arr[0][1] + arr[0][2] + arr[0][3] + arr[0][4] + arr[1][2] + arr[1][3]
    p3 = arr[1][5] + arr[2][4] + arr[2][5] + arr[3][4] + arr[3][5] + arr[4][5]
    p4 = arr[4][2] + arr[4][3] + arr[5][1] + arr[5][2] + arr[5][3] + arr[5][4]
    out.append(p1)
    out.append(p2)
    out.append(p3)
    out.append(p4)

    print(out)

    pass #divided


#arr=[[7,11,9,9,11,3], [8,9,3,4,0,13], [3,10,4,14,3,7], [4,15,5,6,3,9], [3,12,3,12,8,0], [17,4,2,4,14,3]]
#divided(arr)


def stockPairs(stocksProfit, target):
    # Write your code here
    copia = stocksProfit.copy()
    i = len(copia)-1

    while i >= 0:
        try:
            copia.remove(copia[i])
            stocksProfit.remove(stocksProfit[i-1])
        except:
            break
        pass #while

    i = len(copia)-1

    while i >= 0:
        for st in stocksProfit:
            if (copia[i] + st) == target:
                count = count + 1
                copia.remove(copia[i])
                stocksProfit.remove(st)

            pass #for
        i = i -1
        pass #while	
    pass #StockPairs

#sp = [6,6,3,9,3,5,1]
#tgt = 12
#stockPairs(stocksProfit=sp, target=tgt)





##### HACKER HANK CHALENGES #####

def minimumBribes2(Q):
	print("teste")
	#
    # initialize the number of moves
	moves = 0 
    #
    # decrease Q by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our
    # indices.  (Not necessary but makes it easier to
    # understand.)

	Q = str(Q).split(" ")

	for x in range(0, len(Q)):
		Q[x] = int(Q[x])


	Q = [P-1 for P in Q]

	# Loop through each person (P) in the queue (Q)
	for i,P in enumerate(Q):
		# i is the current position of P, while P is the
        # original position of P.
        #
        # First check if any P is more than two ahead of 
        # its original position
		if P - i > 2:
			print("Too chaotic")
			return
        #
        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front if P's original position,
        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those 
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
		for j in range(max(P-1,0),i):
			if Q[j] > P:
				moves += 1
	print(moves)

	pass #minimumBribes




def minimumBribes(q):
	q = str(q).split(" ")
	#desired_array = [int(numString) for numString in q]
	
	for i in range(0, len(q)):
		q[i] = int(q[i])
		
	q2 = []
	for i in range(1,len(q) + 1):
		q2.append(i)

	valor = 0
	valorFull = 0
	tam = len(q2) -1
	vSwap = 0

	for i in range(0, tam):
		Index = q2.index(q[i])
		valor = abs(i - Index)
		if valor > 2:
			print("Too chaotic")
			return 
			pass
		if Index != i:
			valorFull = valorFull + valor 
			pass
		for x in range(0,valor):
			vSwap = q2[Index-1]
			q2[Index-1] = q2[Index]
			q2[Index] = vSwap
			Index -= 1
			pass
		valor = 0
		vSwap = 0
		pass
	print(valorFull)
	return 
	pass ##minBribes

#2
#8
#5 1 2 3 7 8 6 4
#8
#1 2 5 3 7 8 6 4

#Expected Output
#Too chaotic
#7

#q = '2 1 5 3 4'
#q = '2 5 1 3 4'
#q = '1 2 5 3 7 8 6 4'
	

#minimumBribes(q)

#--------------------------------------------------------------------------------------------------------------------
###############import requests
###############import urllib.request
###############import urllib.parse
###############import json
###############url = 'https://jsonmock.hackerrank.com/api/countries/search?name='
###############url = url + 'us'

###############receive = requests.get(url)

###############strx = receive.text

###############jObj = json.loads(str(strx)) 
###############var = jObj.items()
###############strValue = ""
###############count = 0
###############for key, value in var:
###############	print(key)
###############	print(value)
###############	if key=="data":
###############		strValue = value

###############for Obj2 in strValue:
###############	intPop = Obj2.get('population')
###############	if intPop >= 10090:
###############		print(intPop)
###############		count += 1

###############print(count)

################# REGEX ## -->> "population": (\d+)

################f = urllib.request.urlopen(url)
################print(f.read().decode('utf-8'))
#--------------------------------------------------------------------------------------------------------------------

#	n = 10
#queries = [[1,5,3], [4, 8, 7], [6, 9, 1]]
#matrix = [[0,0,0, 0, 0,0,0,0,0, 0], [3,3,3, 3, 3,0,0,0,0, 0], [3,3,3,10,10,7,7,7,0, 0], [3,3,3,10,10,8,8,8,1, 0]]
#print (  max( map(max, matrix) ))

#result = [0] * n

#for qi in queries:
#	for i in range(qi[0] -1, qi[1]):
#		result[i] = result[i] + qi[2]

#print(max(result))




def most_frequent(List): 
    counter = 0
    num = List[0] 
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i

    return num 

    pass #most_frequent

#List = [2, 1, 2, 2, 1, 3] 
#print(most_frequent(List)) 


#MEAN, MODE and MEDIAN

def MeanModeMedian(vArray):
	counter = 0
	num = 0
	Mode = 0
	Median = 0
	Mean = 0
	for i in vArray: 
		curr_frequency = List.count(i) 
		if(curr_frequency > counter): 
			counter = curr_frequency 
			num = i
	
	print(Mode)
	print(Median)
	print(Mean)

	pass #MeanModeMedian




####
####



def teste():
    pass #teste













