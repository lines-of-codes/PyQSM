# PyQSM
Quick Server Manager (Python Version) or PyQSM is a Quick and easy way to 
start up and manage a Minecraft server.

This is NOT designed for pro users. This software is designed to be too simple.
Simple enough that my friends could use it.

This project is written in Python with Qt 6.
This project used to be written in C++ but I gave up on fixing linker errors 
and turned the C++ version private.

This software *should* work on x86_64 and aarch64 platforms. (Basically 
most PCs are supported, and that includes Mac too)

This software is not designed for use on servers. You are better off using 
something like Pterodactyl, This software should only be used for home 
servers at best.

## Features
- Setup new servers
- Import existing server without losing any data
- Update mods and plugins quickly
- Install new mods and plugins quickly
- Allow the user to easily setup and manage the Java Runtime
- Cross-platform. allowing Windows, Mac, and Linux users to use it.

## Setting up JRE through PyQSM
A little bit of information about the feature that allows you to 
setup Java Runtime through this software.

This software make use of Azul's Metadata API and Adoptium API to 
list out the possible choices of JRE for you.

Even though you are not directly interacting with Azul's or Adoptium's 
services, By using their JRE, you will be agreeing to their respective 
Terms of Use and Policies.

Azul's Terms of Use is available [here](https://www.azul.com/terms-of-use/)

Eclipse Foundation's Terms of Use is available [here](https://www.eclipse.org/legal/termsofuse.php)

## License
Please send and email to linesofcodes@proton.me if I accidentally broke 
any license's rules.

This project code is under the GPLv3 license.

Qt 6 which is used by this project is licensed under LGPL and some parts in GPL.
The licenses of the dependencies of Qt 6 modules can be found [here][1]

This project uses icons from the [Lineicons][2]
project under the Free plan which is licensed under the MIT license.

The NeoForge, PaperMC and Velocity logo used within the project is owned 
by their respective owner.

Even though some Minecraft assets are used in this project, **THIS IS NOT AN 
OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR 
MICROSOFT.**

[1]: https://doc.qt.io/qt-6/licenses-used-in-qt.html
[2]: https://github.com/LineiconsHQ/Lineicons
