I've been programming in Go a lot lately. Migrating from Python was fairly painless, switching from dynamically typed language such as Python to a statically typed language like Go, takes some getting used to. Go is language that is very fastidious about typing. You are forced to write boilerplate code with case statement for every single expected type, and sometimes write code like this:

		float64(data.([]interface{})[1].(float64))
		
Putting all the semantics aside, here's one thing that bugged me from the beginning. There are four distinct integer numeric types: `int8, int16, int32, and int64`, all implementing integers of different sizes. But there is also another distinct, predeclared type called **int**.

From the docs, there essentially are no difference between **int32** and **int**. Both represent set of all signed 32-bit integers, i.e. range -2147483648 through 2147483647. One subtle difference is that **int** represents a signed integer that is **at least** 32-bit.

Effectively, we can say that int can be 2^32 + 2, while int32 will overflow. And of course, that also means int occupies twice as much memory as int32, 8 bytes vs 4.
