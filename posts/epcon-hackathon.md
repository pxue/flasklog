Over the weekend I attended [EpCon](http://hiepic.com/), an energetic Waterloo
Technology convention that features some of the industries leading entrepreneurs
and tech. founders to engage in close up and personal workshops with students
from University of Waterloo, Toronto and Ryerson.

The main highlight for me was the coding challenge sponsored  by Microsoft aptly
named Encode. The challenge is essentially building a Windows Phone 7 app. and
with a grand price of either a brand new WP7 phone or Xbox360.

Well. Of course I'm down, and so was 2 other friends of mine.

Now, I've never touched WP7, and honestly besides a first year course in C#
that's pretty much all the experience I have with it. So, I relied heavily on
Google. Thankfully, I was the only one in the ditch about C#.

Essentially, the app idea is a simple interactive game that tests your knowledge
of your friends on Facebook. The app will pull a random news feed post, pull two
friend display pictures, one being the speaker, and another randomly.

The objective of the game is to match the quote with the friend. If you get it
right, your score goes up. If you get it wrong, you can humiliate yourself by
posting your score to facebook and let your friends know how much of a terrible
friend you are.

Sounds simple enough, and we got cracking.

##Installing the SDK
This was surprisingly the easiest part. Out of all the other mobile dev. sdk
setups I have to say WP7 is hands down the easiest one. Just visit WP SDK 7.1
[download center](http://www.microsoft.com/download/en/details.aspx?id=27570),
extract, install and you're well on your way to a working app. No hastle, no
mess. This took about 30min with a relatively fast internet, the total download
is appx. 700mb and extracted to appx. 1.2gigs.

##Facebook Integration
This was a pain. Neither Facebook nor WP7 has official integrated API. Quick
google search yielded [Codeplex](http://facebooksdk.codeplex.com/) Facebook C#
SDK. Okay, that looks legit enough.

Now the rest of the night, from 9pm-2am was just a lot of cussing and heavy
drinking. Had a bottle of scotch and Absinthe on the side, ready to get us
going.

There wasn't much take away, no body knew how to do anything, quick google
search revealed that no body on the internet knew how to do anything either.

So we kinda hacked bits and pieces of codefrom like 20 different places on
the internet and hoped that it would work.

Well, it did.

##Says Who?

<iframe width="560" height="315" src="http://www.youtube.com/embed/oiwhK3SjWpc"
frameborder="0" allowfullscreen></iframe>

So yeah. That was the result. As you can see, I suck at this game and it's
actually pretty fun =)

As usual, the source code is available on my
[github](https://github.com/pxue/EpCon-Hackathon), feel free to take a look!

Wew.


ps. So after we finished the video and all patting ourselves on the back, we
realized that this would not work for anyone that had switched over the new
facebook timeline thing, because of all the API changes that facebook did
WITHOUT TELLING ANYONE (well okay they did..). So yeah, if your account has
switched over to Timeline, sorry =(

