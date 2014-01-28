We will work on this project in a way that will be similar to how things are
done in "the real world". This means the core repository will be here, and you
will fork the repo to your own github profile, make your changes there in new
branches and issue pull requests. This will also give me the chance to review
the code and leave comments better.

We will also try to work through GitHub issues, so check there for more
information.

# Coding standards

We will adhere to the [Plone API coding
conventions](http://ploneapi.readthedocs.org/en/latest/contribute/conventions.html),
which are short and very useful. Read them!

# Editor

While the editor choice is left to you, I would recommend [Sublime Text
2](http://www.sublimetext.com/2) for it's many and easily installable addons.
Tutorial on how to set ST2 up comming soon.

# Installation

As is the norm, we will work inside a Python virtualenv. I'd recommend creating
a new folder named *cocos2d* or something similar, creating the virtualenv
inside it, installing the needed packages with pip and then cloning the git
repository.

To do all that on Ubuntu, you need to run the following commands.

Installing the prerequisites:

    sudo apt-get install git python python-setuptools python-pip python-virtualenv

Make a new folder and move to it:

    mkdir cocos2d
    cd cocos2d

Create the virtualenv:

    virtualenv .

Source the Python virtualenv and install cocos2d with pip:

    source bin/activate
    pip install cocos2d

Clone the GIT repository from GitHub:

    git clone URL_OF_YOUR_FORK_HERE

Lastly, just run the game with Python:

    cd two-runner
    python src/main.py
