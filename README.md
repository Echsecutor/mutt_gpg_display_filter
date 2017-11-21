# mutt_gpg_display_filter
This is a simple stream filter to be used with the mutt email client to make gnuPG less verbose.

I am using `trust-model tofu+pgp` with gpg2 with mutt. While the mode itself is great, the gpg output is terribly verbose and obscures the whole mutt screen. Since it seems that there are no good gpg2 options to reduce the verbosity further, I wrote this script to do so.


# Usage
Put something like
```
set display_filter="/full/path/to/mutt_gpg_display_filter/filter.py"
```
into yout `.muttrc` file to activate the filter. (`python` needs to be installed, of course.)

As you can see, the filtering is straight forward. Feel free to customize it to your needs.
