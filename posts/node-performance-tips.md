Node.js is really cool, and easy to learn. If you know a bit of Javascript,
you're well on your way. It took me a bit to get with the way how node optimizes
it's code structures, mainly wrapping my head around the single threaded
callback system vs. python's multi-threading. Once I figured that out, everything
falls into place, and it's practically the same thing.

A few of things I figured out along the way, I figured it might be of help for
anyone who's getting started with Node, and are looking for things to optimize
their code on. Here we go.

1. Callbacks/Asynchronous
---

Node should be non-blocking. You should try to use as much non-blocking code as
possible. That means callbacks and asynchronous, and since you can use anonymous
functions as callbacks, there shouldn't be any excuse to not do it.. you set it
up once and it'll work forever.

2. Turn off socket pooling
---

The Node.js http client automatically uses socket pooling, which severely limits
you to 5 sockets per host. While it helps to curb resource usage, it is
a serious bottleneck if you are processing many concurrent connections all
requesting data from the same host.

3. Separate the static assets from Node.js
---

Use a standard webserver such as [nginx](http://nginx.org/). This will help
reduce load on your Node server.

4. Render on client-side
---
Let user's browser cache and take care of the static files. Just worry about the
dynamic data on the server side.

5. Use gzip
---
Use whenever possible to reduce size of the requests sent.

6. Go session free
---
Or use external session store such as MongoDB, Redis or CouchDB.

7. Keep your code clean
---
Lastly, it's up to the programmer to keep their code in tip top shape. A little
optimization can go a long way!

###Links:
For examples and full Node.js Performance Tips, read this
[article](http://engineering.linkedin.com/nodejs/blazing-fast-nodejs-10-performance-tips-linkedin-mobile)
from linkedin Engineering blog. 

