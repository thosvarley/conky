# Modular conky sidebar
A modular conky sidebar for keeping an eye on system behavior. 

Each piece of the sidebar is defined in its own configuration file in the `configs` directory. You can change the order in the `buildconky.sh` script.

To compile a new master `conky.conf`, run `./buildconky,sh`. To start it, run ``./startconky.sh``.

## Install
The ``buildconky.sh`` and ``runconky.sh`` assume that conky is running out of the ``~/.conky/`` directory. Clone this repo, and unpack everything in that directory and it should all work out of the box. If you just run ``./startconky.sh`` without first configuring and building a desired layout, it will automatically build the layout you see in the image below.  

### Setting network address

To use the ``network.conky`` module, you will need to hardcode in your own network address. You can find this by running ``iwgetid | awk '{print $1}'`` in your terminal, and substituting in the output into the relevant network.conky (where you see ID). 

## Image
Here's a photo my desktop so you can see what it looks like in-context.

![Conky on a desktop](images/desktop.png) 
