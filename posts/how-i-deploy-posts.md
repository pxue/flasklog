This process doesn't work for everyone. In fact it took me sometimes to get used
to as well. I can only describe my workflow as hackish as I don't exactly manage
it from top to bottom - I cheat a bit and let Cloudnode worry about the
deployment process. Is it the best practise? Definitely, probably not. Does it
work for me? Yes. I find it easy to work with and I like how simple it is and
can be done completely without leaving the terminal (or vim).

This is what I do:

* create post in vim;
* commit to github;
* push to cloudnode;
* create couchdb entry (could be automated).

I don't have an admin interface par se, as in I don't have an editor to do the
posting in the browser on the blog because I have all my posts stored as
Markdown files in the repository, and when it is requested, it is opened and
read and then displayed. Not the best practise for any blog with a little bit of
traffic.

What can be improved/todo:

1. an interface for writing posts;
2. a less hackish file managing system (maybe caching in couch);
3. upload source to github.

It's a pretty good list, and it's not very much work. So far I really enjoy this
system and it's exactly what I have always been looking for. I can control all
the visual aspect with Jade/Stylus and any thing I need (commenting system,
twitter/facebook integration) is just a drunken coding session away.

What more can a nerd ask for? Happy coding!

ps. there are many open source nodejs blogs out there already, such as
[glog](https://github.com/guyht/Glog), [nog](https://github.com/c9/nog),
[wheat](https://github.com/creationix/wheat), etc.

