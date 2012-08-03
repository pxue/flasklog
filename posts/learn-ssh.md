#Getting Started with SSH

For many of us who spend most of our days behind a terminal, ssh is an important
tool that should be mastered. SSH provides an easy and secure way to access
another machine, it's one of the essential tools for any programmer.

Here are a few tips that I wish I knew when I first got started, which
I obtained through finding some blog posts on Hacker's News.

##Setting up your SSH

A few steps we want to make sure we have done already, we will go through them and
make sure everything is setup correctly.

1. If you don't have one, create your SSH key pair via:

        ssh-keygen -t rsa

    This command will generate two files, your private key (id\_rsa) and your public
    key (id\_rsa.pub). You want to keep your private key safe. Also make sure you put
    in a passphrase on this (make sure it's something secure, since you only ever
    have to type it once).

2. Push the public key component to the remote server you want to connect to:

        cat ~/.ssh/id_rsa.pub | ssh user@remote "cat >> .ssh/authorized_keys"

3. Connect to the remote box:

        ssh user@remote

    If you're on a unix box you should be getting a OS dialog asking you for the
    passphrase you chosed in step 1. Enter it, and that should be it.

## Proxying connections through a VPN (bastion host)

In most cases (at your work), you'll be going through a VPN. This is a very
useful way of keeping everything simple on a clustered network without exposing
their SSH services to the internet. All you need to keep open is ssh on your
VPN host and you have access to all the internal machines nearly automatically:

Say you have a network of machines on a <code>\*.internal</code> domain
(foo.internal, bar.internal, etc), assuming you already have access to the
machines as detailed in the previous section, you can simple add something like
this to your <code>~/.ssh/config</code> file:

    Host \*.internal
    ProxyCommand ssh <vpn_host> nc %h %p

and you'll magically be able to run commands like the following

    ssh foo.internal

Magic!

##Conclusion

SSH is important in the daily operation of many programmers, it's pretty
important to learn how to use it properly. Take a look at [github](http://help.github.com/ssh-key-passphrases/)
passphrase guide, they have a very well written post on it. If you want to dig
even deeper, here's [ a page ]( http://unixwiz.net/techtips/ssh-agent-forwarding.html ) on how ssh-agent forwarding works.

