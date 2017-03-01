all:
	pandoc \
		-t beamer \
		-V classoption=notes \
		--filter pandoc-beamer-notes \
		-o presentation.pdf \
		presentation.md
