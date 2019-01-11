

def KelvinToFahrenheit(Temperature):
	try:
		assert (Temperature >= 0),"Colder than absolute zero!"
		return ((Temperature-273)*1.8)+32
	except AssertionError:
		print('some assert error')

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
	except StopIteration:
		print('the iterator value is all showed')
	except:
		print('the basic exception')

def runtime_error():
	try:
		li = generate_list()
		for item in li:
			print(item)
	except RuntimeError:
		print('the Runtime wrong ')

def attribute_error(num):
	try:
		a = 12
		a.pdwsfe()
	except AttributeError:
		print('the wrong Attribute')
	except:
		print('the basic exception')

def value_error(num):
	try:
		int(num)
	except ValueError:
		print('the wrong value')
	except:
		print('the basic exception')

def type_error(num):
	try:
		a = 12 + num#when the num is str
	except TypeError:
		print('the wrong type')
	except:
		print('the basic exception')

def zero_error():
	try:
		b= 120 / 0
	except ZeroDivisionError:
		print('the dividied can not be zero')
	except:
		print('the basic exception')

def name_error():
	try:
		print(v)
	except NameError:
		print('the identifier is not found')
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