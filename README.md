# Challenge:

## First Step
We’d like you to write a simple function that given a piece of text and an integer n, it
returns the n-grams for that text. For background, “an n-gram is a contiguous
sequence of n items from a given sample of text or speech” [Wikipedia]. It is
commonly used in the field of Natural Language Processing (NLP). Here are some
examples to help you understand this concept:
```python
	def calculatNGrams(string,number):
		"""
		Function that is in charge of calculating n-grams of the word with the number of separations received
		Receives:
			string: piece of text
			number: number of separations
		"""
		lenString = len(string)
		nGrams = []
		for i in range(lenString-number+1):
			nGrams.append(string[i:number+i])
		nGrams = nGrams[:-1]
		return nGrams
```
## Second Step
We’d like you to extend the functionality of your algorithm to return only the most
frequent n-gram, not all of them.

## Expectations
We’re expecting an algorithm that handles these two steps in a nice, cleanly
organized and efficient way. It should handle edge cases. You can choose any
language you feel most comfortable with to implement it. Make sure you follow
conventions and idiomatic guidelines for your chosen language! We move fast but
are fanatical about writing clean, idiomatic, maintainable code. You should, as a
comment within your functions, correctly explain the running time complexity of your
algorithm. Extra credit if it’s better than quadratic.

### Prerequisites
You need to have installed the next software to successfully run the program:

* Python 3

## Built With
* Python 3
* Git - Version-control system

## Author

[**Nikolai Bermudez Vega**](https://github.com/Nikolai9906) Software Engineering Student

## License

 This project is licensed under the MIT License
