% pandoc-beamer-notes
% Sebastian Höffner
% March 2017


# How to compile

Remember to compile using a command similar to this:

```Makefile
default:
	pandoc -t beamer -V classoption=notes \
		--filter pandoc-beamer-notes \
		-o presentation.pdf \
		presentation.md
```

# The plain LaTeX way

The second slide contains latex notes like this:
```
\note{A very simple note to appear on the note page.}
```

\note{A very simple note to appear on the note page.}


# Markdown in notes in LaTeX

Markdown can also be used inside notes:
```
\note{
* Bullet *one*
* Bullet two
* Bullet three
}
```

\note{
* Bullet *one*
* Bullet two
* Bullet three
}
