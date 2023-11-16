import sys



if len(sys.argv) == 3:

	bin1 = sys.argv[1]
	bin2 = sys.argv[2]
else:
	exit()


def and_(inp1,inp2):
	if inp1 & inp2:
		return 1
	else:
		return 0


def not_2inp(inp1,inp2):
	if inp1 | inp2:
		return "on"
	else:
		return "off"

# inverse 
def not_(inp1):
	return int(not inp1 )


# and and --> not = nand
# simply !& 					0 0 = 1; 0 1 = 1; 1 0 = 1; 1 1 = 0;
def NAND(inp1,inp2):
	ret_and = and_(inp1,inp2)
	return not_(ret_and)


# not not --> nand = or
# 0 0 = 0; 1 0 = 1; 0 1 = 1; 1 1 = 1
def OR_(inp1,inp2):
	ret_not_1 = not_(inp1)
	ret_not_2 = not_(inp2)

	nand = NAND(ret_not_1,ret_not_2)
	return nand

# or and --> and = xoe
def XOR(inp1,inp2):
	ret_or = OR_(inp1,inp2)
	ret_and = NAND(inp1,inp2)

	xor = and_(ret_or,ret_and)
	return xor   


# print(XOR(1,1))



# add_table = {
# #    a b : carry  sum; carry=and
# 	[1,1] : [0,0],
# 	[0,1] : [0,1],
# 	[1,0] : [0,1],
# 	[1,1] : [1,0]
# }

#	  1	1  1  <- carry
# 1 0 0 0 1 1
# 0 0 0 1 1 1
# 1 0 1 0 1 0  <-sum
# take 3 inp and ret sum and carry





# use or to calculate sum bit and use and to  make a carry bit one when both'em are 1

def adder(inp1,inp2,inp3):
	xor_1_2 = XOR(inp1,inp2)
	and_1_2 =  and_(inp1,inp2)
	
	xor_2_xor12 = XOR(inp3,xor_1_2)
	
	and_xor_12_3 = and_(xor_1_2,inp3)
	carry = OR_(and_xor_12_3,and_1_2)
	
	sum_ = xor_2_xor12

	return (sum_,carry)


# print(adder(1,1,1))


def adder4bit(a,b,over=0):
	a1,a2,a3,a4 = a
	b1,b2,b3,b4 = b

	add1 = adder(over,b4,a4)
	add2 = adder(add1[1],b3,a3)
	add3  =adder(add2[1],b2,a2)
	add4 = adder(add3[1],b1,a1)

	s1,s2,s3,s4,ov = add4[0],add3[0],add2[0],add1[0],add4[1]
	if ov == 1:
		return False # "over flow"
	return[s1,s2,s3,s4]


# print(adder4bit([0,0,0,1],[1,1,1,1]))

def bin_dec(bin_):
	b1,b2,b3,b4 = bin_
	# print(b1,b2,b3,b4)
	decimal = 8*int(b1) + 4*int(b2) + 2*int(b3) + 1*int(b4)
	print(b1,b2,b3,b4," = ",decimal)
	return decimal


bin1 = [int(i) for i in list(bin1)]
bin2 = [int(i) for i in list(bin2)]
if len(bin1) != 4 or len(bin2) != 4:
	print("invalid bin")
	exit()
for i in bin1:
	if i == 0 or i == 1:
		pass
	else:
		print(":invalid bin")
		exit()
for i in bin2:
	if i == 0 or i == 1:
		pass
	else:
		print(":invalid bin")
		exit()

print(bin_dec(bin1))
print(bin_dec(bin2))


res = adder4bit(bin1,bin2)
if not(res):
	print("overflow; result os to big for 4bit")
else:

	print(''.join([''.join(str(i)) for i in bin1])," + ",''.join([''.join(str(i)) for i in bin2])," = ",''.join([''.join(str(i)) for i in res]),"",[bin_dec(res)])




