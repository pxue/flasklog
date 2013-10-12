A design feature of Golang is that it does not handle exceptions. The programmer is expected to explicitly handle all error that might occur in an execution process. This may inevitably lead to code that look something like this:

	func Foo() (int, error){
		err = Bar1()
		var i int
		if err != nil {
			return i, err
		} else {
			i += 1
			var n int
			n, err = Bar2()
			i += n
			if err != nil {
				return i, err
			} else {
				err = Bar3()
				if err != nil {
					i += 2
				} else {
					return i, err
				}
			}
		}		
	}
	
There're few things wrong with this, one: nested error handling is just a mess, two: else statement is redundant, three: we're repeating ourselves.

Let's try to clean this up a little with an useful Golang feature called [named result parameter](http://http://golang.org/doc/effective_go.html#named-results).

	func Foo() (i int, err error) {
		err = Bar1()
		if err == nil {
			i += 1
			var n int
			n, err = Bar2()
			i += n
			if err == nil {
				err = Bar3()
				if err == nil {
					i += 2
				}
			}
			return
		}
		return	
	}
	
This is much cleaner, but not clean enough. We can do better.

Let's avoid nesting by handling errors first:

	func Foo() (i int, err error) {
		err = Bar1()
		if err != nil {
			return
		}
		i += 1
		n, err := Bar2()
		i += n
		if err != nil {
			return
		}
		err = Bar3()
		if err == nil {
			i += 2
		}
		return
	}
	
Not shorter, but cleaner and easier to read.
Question is, can we do better? Let's try something new, let's avoid repetition by creating a one-off utility type:
	
	type Bar struct {
		n		int
		err 	error
	}
	
	func (b *Bar) BarAction() {
		if b.err != nil {
			return
		}
		if b.err = DoSomething() {
			b.n += someNumber
		}
	}
	
	func Foo() (int i, error) {
		b := &Bar{}
		b.BarAction(var1)
		b.BarAction(var2)
		b.BarAction(var3)
		
		return b.n, b.err
	}

We got rid of nesting, and we've "abstracted" the functions to a simple structure that holds the data we want.

This might be confusing first, but with practise, it'll seem second nature soon enough. For more examples and a much better presentation, go throught this presentation: [Twelve Go Best Practises](http://talks.golang.org/2013/bestpractices.slide#1).



