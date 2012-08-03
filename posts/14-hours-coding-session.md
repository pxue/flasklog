Most of the time with long flights people tend to sleep it away, which makes
sense since it's long and gruesome, and economy seatings aren't the most
comfortable for doing any real work.

For me it's a great opportunity to sit down and do some casual coding, instead
of loading my laptop with movies/shows, I downloaded a whole bunch of E-books
that were suggested on Hacker's News, StackExchange etc, I've blogged about the
books before and you can find them [here](/must-read-programming-books).

Okay, enough stories, let's get down to work!

## Enroute to China: 14hrs coding session!

## Hour #1: simple NodeJS messaging app
    15:32 EST

I've been messing around with node for a while now, and one of the standard
application to make for node is a messaging/chat program. It's simple and
demonstrates an important concept of long polling. The E-book I'm reading on
this is located [here](http://book.mixu.net/single.html).

There are generally three ways how a chat application can work.
Request-response(simple polling), long polling, and sockets. In short, simple
polling is when the server responds immediately to any request the client sends,
with or without any data changes. The client then waits a set interval, and
resends the request, this continues until client disconnects.

Long polling is when the server keeps the request connection open until a set
timeout is reached or a change has occurred. What this means is that the client
does not determine the request interval, whenever the server returns a message
to the client, either with changed data or a timeout message, the client
immediately resubmits a request.

Sockets is a whole complete idea on it's own. Instead of "polling", there will
be a constant, established connection between the server and the client, and
whenever a change happens on either end, the event is "emitted" and
corresponding "listener" or "event handler" picks it up and processes it
accordingly.

In short, we need to know when new messages are available to the client, if
there are no changes, the server should store the the client request in a queue.
Lastly, when a client sends a new message, the server should parse it and add it
to a list of messages and broadcast it to all connected clients.

I built a very barebone server script, using two arrays as our data store:

    var message = ['testing']; // our message store
      , clients = [];          // our client queue

The server shall serve three pages, <code>/</code>, <code>/poll</code>, and
<code>/msg</code>.

    var req_url = url.parse(req.url);
    if (req_url.pathname === "/"){
        // server index.html
    } else if (req_url.pathname.substr(0,5) === "/msg"){
        // server message
    } else {
        // handle polling requests
    }

For handling messages, we can just get the messages attached to the url (ie.
localhost:8000/msg/MESSAGEHERE).
    
    var msg = unescape(req_url.pathname.substr(5));
    messages.push(msg);

    while (clients.length > 0){
        var client = clients.pop();
        client.end(JSON.stringify({
            count:messages.length,
            append: msg+"\n"
        }));
    }

Polling is the same but for clients, we strip the counter and append that to
client array.

The full code can be found on pastebin here.

### Hour #1 complete!
    16:36 EST

## Hour #2: instagram streamer

    18:41 EST

Dinner break/1 movie later (Good Will Hunting, such an amazing movie!), I'm back
at it, hour #2 is actually hour #5 into flight. Only 9 more to go =)

I wanted to make a site that would stream my instagram pictures, after taking
a look at instagram's api, it seems that they are using OAuth as their
authentication system. In short, clients request permissions from the user,
obtains access key which then allows the client to access user data.

so, step one is authentication process, a simple back and forth between
instagram and your application. We'll hack together an authentication token,
since we aren't opening this app to everyone (only me), we don't need to build
a system that automatically gets the authentication token.

hit up instagrams authentication url and you'll receive a <code>code</code>
param back in the redirect url.

    res.redirect("http://api.instagram.com/oauth/authenticate/?client_id=# \
        &redirect_uri=#&response_type=code")

make sure rediret\_uri is the same as one you set up with instagram.

the callback will look something like this:

    http://locahost:8000/callback?code=###

take the code param and now POST it again to instagram via access\_token

    http://api.instagram.com/oauth/access_token/?...

the params you need are client\_id, client\_secret, grant\_type, redirect\_uri, and
code. The grant type is the permission param, where default is
authorization\_code that allows the client to pull user pictures, without
additional data like comments, likes etc.

alternative, just cheat and do a curl:


    curl -F 'code=CODE' 
         -F 'client_id=ID' 
         -F 'client_secret=SECRET' 
         -F 'grant_type=authorization_code' 
         -F 'redirect_uri=CALLBACK'
         https://api.instagram.com/oauth/access_token

Now you'll have an access token, which then you can use to get anything you want
about a user.

Being lazy, I'm using a module called Nodestagram to do all the api calls for
me. So the actual code to generate the json for my pictures are very simple:

    instagram.user.self({access_token:###, count:20}, function(images, err, pagination){
        res.render('index', {'images':images});
    })

That's it, make good time too!

    19:06 EST

##Hour #3: improving on the chat app.

    19:30 EST

The basic chat app is not very user friendly, now I'm going to add a input
textbox for the user to type the message in.

The front end is simple:

    form(method="POST")
      input(name="message")
      input(type="submit", value="Send")

on the server side:

    app.post('/', function(req, res){
        var datetime = dateformat("longTime");
        var msg = req.param("message");
        messages.push(datetime+":\t"+msg);
        ...
    });

basically the code is almost the same with an extra POST function to accomodate
the message being sent to server.

    20:15 EST

At this point, I realized long polling is not a very good way of doing this,
because if I want to implement nickserver this is going to lag considerably and
I would have to implement multiple http requests from the client.

Next I'm going to look into how to use Socket.IO



