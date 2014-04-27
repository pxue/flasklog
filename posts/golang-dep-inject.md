Unit testing, no body likes it, everyone talks about trying it, your have colleagues that have never heard of it (or pretending anyway). Before we make this sound like some new street drug, let's talk reals: so you've written some, probably with a whopping unit coverage of 26.4%, it ended as some dead code you run/update maybe once a month; or you've automated some, I won't judge.

Before I begin getting into what I want to talk about, let's get this out of the way: unit testing is important. There are right ways, okay-if-you're-the-only-one-knows ways and the dead-wrong ways to unit test code. I won't talk about what's right or wrong here, because honestly it depends on the piece of code you're testing. Here, I will talk about a very useful and important methodology of testing code, that is **dependency injections**.

If you've never heard of dependency injection, [here's a wiki](http://en.wikipedia.org/wiki/Dependency_injection) article on it. I'd suggest you to skip all the historical stuff and go straight to the Examples.

I like concrete examples and real world use cases, and here I will present one. The language is Golang.


I have an important and large function I want to test, but in the middle of this function it makes an http call to external server to grab some piece of data. I want to unit test this function without mocking this http call.

    func FooManShoo(cell *phone.IPhone) (bool) {
        //.. some logics ..
        
        go func(ch chan bool) {
            // below is generally a bad idea.
            response := <- phone.ExternalCall(cell, "exgirlfriend")
            if response == "okay" {
                ch <- true
            } else {
                ch <- false
            }
        }(ch)

        // some more logics, depending on ch value
        
        return <-ch 
    }

In my unit test, I don't want to make the phone call, but I also want to pretend it returned something meaningful that I can use later.

Let's redefine the function in a new way:

    var FooManShoo = func(cell *phone.IPhone) (bool) { … }
    
This requires no change anywhere else, we're safe to use this everywhere we call it after the change.

In our test, we can now overwrite this function…

    fund TestHappyThoughts(t *testing.T) {
        
        phone.ExternalCall = func(cell *phone.IPhone, who string) { 
            return "okay"
        }
        
        cell := &phone.IPhone{}
        rv := FooManShoo(cell)
        
        //.. do something with rv, or not ..
    } 

This works because how golang handles function scopes, essentially it works because the function is a [first-class-citizen](http://en.wikipedia.org/wiki/First-class_functions). The function doesn't even have to be public, golang's testing package is given access to private functions as well.

Dependency injection breaks the wall of pure statically typed language (such as Golang), many hardcore Golang users would prefer using interfaces instead of DI. Each have their benefits, I prefer DI simply because it's cleaner, I will have to benchmark the code to know if there's a performance difference.
