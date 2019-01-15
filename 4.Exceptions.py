

def KelvinToFahrenheit(Temperature):
	try:
		assert (Temperature >= 0),"Colder than absolute zero!"
		return ((Temperature-273)*1.8)+32
	except AssertionError as e:
		print(e)

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))

def generate_list():
	for i in range(5):
		yield i

def stopiterator_error():
	try:
		li = [1,2]
		iteratorli = iter(li)
		print(next(iteratorli))
		print(next(iteratorli))
		print(next(iteratorli))
	except StopIteration as e:
		print(e)
	except:
		print('the basic exception')

def runtime_error():
	try:
		li = generate_list()
		for item in li:
			print(item)
	except RuntimeError as e:
		print(e)

def attribute_error(num):
	try:
		a = 12
		a.pdwsfe()
	except AttributeError as e:
		print(e)
	except:
		print('the basic exception')

def value_error(num):
	try:
		int(num)
	except ValueError as e:
		print(e)
	except:
		print('the basic exception')

def type_error(num):
	try:
		a = 12 + num#when the num is str
	except TypeError as e:
		print(e)
	except:
		print('the basic exception')

def zero_error():
	try:
		b= 120 / 0
	except ZeroDivisionError as e:
		print(e)
	except:
		print('the basic exception')

def name_error():
	try:
		print(v)
	except NameError as e:
		print(e)
	except:
		print('the basic exception')

def main():
	stopiterator_error()
	runtime_error()
	attribute_error(45)
	value_error('ou')
	type_error('y')
	zero_error()
	name_error()

if __name__ == '__main__':
	main()
