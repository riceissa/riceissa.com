from subprocess import call

# List of programs to install.
programs = [
# "Essential" utilities:
"sudo", # the minimal install on Debian doesn't come with this
"vim",
"vim-gtk", # for gundo, which requires python
"python",
"python3",
"git",
#"mercurial",
"htop",
"pandoc",
"elinks",

#"lynx-cur",

"python-gpgme", # for Dropbox

# More advanced utilities:
"surfraw",
"par",
"detox",
"xclip",
"wodim",
"gparted",

# Screen and tmux ... and byobu
#"tmux",
#"screen",
#"byobu",

# Programming-related:
"flex",
"bison",
"gcc",
r"g\+\+",
"ghc",
"hugs",
"haskell-platform", # this can probably replace both "ghc" and "hugs"...
"build-essential",
"ruby",

# Music On Console:
#"moc", # Run using 'mocp'.
#"moc-ffmpeg-plugin", # Extra plugins.

# Support for Japanese:
#"ibus-anthy",
#"fonts-ipafont",
# On the command line, type 'ibus-setup' to bring up the IBus
# preferences.  Under "Input Method" > "Select an input method" >
# "Japanese", find "Anthy" and click.  Click "Add" to add it to the list
# of input methods.  You can now close the window.  You must logout once
# in order to enable Japanese input.  To switch to Japanese input, hit
# <Ctrl>-<Space> while in a text-field.

# For Japanese on the commandline, see http://riceissa.github.io/computing/commandline-japanese.html

# LaTeX (warning: large download):
#"texlive-full",

# For the Acer laptop; Wi-Fi driver and bluetooth diabler.
# Make sure to enable 'non-free' and 'contrib' for the driver.
#"firmware-iwlwifi",
#"rfkill",

# For the PowerBook Mac
#"firmware-b43-installer",

# ALSA; possibly outdated packages ...
#"alsa-base",
#"alsa-oss",
#"alsa-tools",
#"alsa-utils",

# Some media-related tools:
#"cdparanoia",
#"flac",
#"vlc",
#"vorbis-tools",

#"bsdgames",

# jsmath; probably unnecessary since many websites now use mathjax.
#"jsmath",
#"jsmath-fonts",
#"ttf-jsmath",


# Openbox
#"xorg",
#"openbox",
#"obconf",
#"obmenu",
#"rxvt-unicode",
#"iceweasel",
#"gtkchtheme",
#"emelfm2",
#"leafpad",
#"mirage",
#"epdfview",

#"gnupg",
#"virtualbox-ose",
#"wine",

# These are packages (or in some cases non-packages) that still have not
# been sorted.
#"hexer",
#"mc",
#"flashplugin-nonfree",
#"alsaequal",
#"antiword",
#"aspell",
#"detox",
#"dict",
#"fbgrab",
#"fim",
#"mplayer",
#"o3read",
#"odt2txt",
#"renameutils",
#"rtorrent",
#"recorder",
#"eatdoc",
#"catppt",
#"espeak",
#"vlock",
#"dtrx",
#"cmatrix",
#"openssl",
#"docx2txt",

# gitosis, gitolite?
# openssl-server?
# get scheme! keepass(X)
]

# Update sources and upgrade system:
#call("sudo aptitude update && sudo aptitude upgrade", shell=True)

# Install programs:
#call("sudo aptitude install {programs}".format(programs=' '.join(programs)), shell=True)


# Some commands for Bash:
call('''echo "PS1='[\u:\W]> '" >> ~/.bashrc''', shell=True)
call('''echo "alias {upgrade,update}='sudo aptitude update && sudo aptitude -y upgrade'" >> ~/.bashrc''', shell=True)
#call('''echo "alias ls='ls --color'" > ~/.bashrc''', shell=True)
