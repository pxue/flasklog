One thing we take for granted in Python is it's ability to convert any arbiturary data types to simple string representations. We are able to seemlessly convert numerics or objects to strings with "str()" or "repr()" respectively. So in a way, we don't ever have to deal with byte or hex representations of data in Python.

But just because we don't use it, doesn't mean it's not useful. Let's see some cool ways Python use bytes and bitshifts.

####1. UUID

Python has a nifty library called [uuid](http://docs.python.org/2/library/uuid.html), it's a quick and painless way to generate unique ids.

We can simply create a unique id from your host ID, a (random 14-bit) sequence number and the current time:

	>>> u = uuid.uuid1(); print u
	UUID('d8f78047-588a-11e3-8dcf-28373725972c')

the hex representation, removing the '-', of the above UUID object is of length 32.

	>>> len(u.hex)
	32

interesting, we need 32 bytes to represent this id, can we compress the data a bit to save some space? What happens when we call the bytes property?

	>>> u.bytes
	'\xd8\xf7\x80GX\x8a\x11\xe3\x8d\xcf(77%\x97,'
	>>> len(u.bytes)
	16
	>>> uuid.UUID(bytes=u.bytes)
	UUID('d8f78047-588a-11e3-8dcf-28373725972c')
	
we magically cut the storage size in half.

let's look at what `u.bytes` is really doing:

    @property
    def bytes(self):
        bytes = bytearray()
        for shift in range(0, 128, 8):
            bytes.insert(0, (self.int >> shift) & 0xff)
        return bytes_(bytes)

in our case, `self.int` is a 128bit integer generated based of varies clock sequences and timings.

	>>> u.int
	288398346214630334003296320690724378412L
	
let's do one iteration of the bit shift:

	# let's pick an interesting shift
	>> u.int >> 112
	55543L
		
	# bitwiseAnd with 0xff
	>> 55543L & 0xff
	247L
	
nice, corresponds to the second most significant byte, `\xf7`. Therefore, we have a cool way to represent a 32 character string by shifting a specifically generated 128bit integer. Neat!

####2. Unique string check

let's try to implement a function to determine if a string is unique or not:

here's a naive O(n^2) solution:

	def str_iter_fn(s):
		for i, ch in enumerate(s):
			for j, chr in enumerate(s):
			if i != j and ch == chr:
				return False
		return True

passable for a novice, let's trade some space for speed:

	def str_array_fn(s):
		tmp = ['']*256
		for ch in s:
			if tmp[ord(ch)]:
				return False
			else:
				tmp[ord(ch)] = 1
		return True
	
O(n), but uses considerable amounts of space, a bit wasteful if you have a really large string. Let's see if we can save some space by doing some clever bitshifting:

	def str_bitvector_fn(s):
	# lets assume lowercase string a-z
	
	checker = 0
	for ch in s:
		val = ord(ch) - ord('a')
		if (checker & (1 << val)) > 0):
			return False
		checker |= (1 << val)
	return True

boom, we've effectively replaced a map with a `len(s)` bit integer. Cool or what?









	
 
