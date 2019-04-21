# JAGpy
Common Utils

## Looper
Looper is mainly for the PuzzleSolver code. 

## MMDDYYYY
These are some simple sugar code for using dates in the MM/DD/YYYY format.
I had a project using a lot of dates and this made things simpler. 'Nuff said. 
(Tests not provided.)

## Structs
I wrote this to avoid checking for missing keys over and over.
I figured there might be other useful stuff later.
(Tests not provided.)

## Numbers
Some generic number functions.
(Tests not provided.)

## Pyrove
An alternative way to run tests/scripts. 

### Concept
Consider a directory structure like this:

```
Project/
	Foo/
		bar.py # wants to import Baz/qux.py
		test.py
		tests/
			test_bar.py # wants to import Foo/bar.py
	Baz/
		qux.py
```

Where Foo and Baz are "independent-ish" projects or libraries or etc. Debates about repository theory or package-and-build techniques aside, I think this is pretty reasonable situation in which to to find oneself. 

Each one might have their own set of unit tests. It gets a bit tough when those tests want to import things above it. Generally speaking, you can do something like these:
	
	$ python -m unittest Foo/tests/test_bar.py
	$ python -m unittest Foo/tests/test_*.py 

Which is fine, although perhaps a bit less "elegant" looking. And you for sure can't do something like this (AFAIK):

	$ python -m unittest Foo/tests/test_bar.py arg
	$ python -m unittest Foo/tests/test_bar.py --arg
	$ python -m unittest discover

In the first two cases, `unittest` will interpret your args as a module or argument to itself, which will likely fail. And in the third case `unittest` will of course try to run more than you want, and probably will have module issues.

So instead, this module tries to make things a little easier. Use it to run a set of tests like this:

	# Runs anything in `Foo/tests/` named like `test_*.py`
	$ python Foo/test.py 
	# ...same, but passing "safe" into each
	$ python Foo/test.py safe

Now, I grant that this is probably only useful in development--and specifically when you don't have paths set up or IDEs, whatever. But it certainly allows me to write in a README for anyone coming across my Git to run `python Foo/test.py`, which is pretty simple. 

### Set up
For this to work, you need two things:

1. Ability to import `Pyrove.py`
2. A file that looks like `test.py` or similar. The one given here is so generic, you probably can just drop it anywhere and be done, so long as `Pyrove.py` is importable from it.

Once you have one, you can pretty much copy-drop it anywhere without changes.

### Some commentary
Look, I get it. One might say that I'm not really doing things the way that Python intended, although I'm not so sure this is a great argument. The setup I propose above is not so radical. I also feel like I've been bitten by this many, many times. It seems like Python makes it harder than it should be.

Ultimately it comes down to the decision by Python to make your working directory default to the place you are running your file, NOT from where you ran the command. For instance, when you run `PlaycodePython user$ python Foo/tests/test_bar.py`, your working directory is `tests/` and you simply cannot back your way out to stuff above, even to `Foo`. 

If instead, your working directory defaulted to `PlaycodePython`, you could easily build your module imports based on that. (This is, incedentally, how Perl works.) Maybe there's a good reason why Python didn't do it this way. I don't know. I do know that, IMHO, module importing is one of the more frustrating parts of Python.  



