FILES := 130010011.pdf

main :
	cd source && python 130010011.py
	jupyter nbconvert --to html source/130010011.ipynb
	mv source/130010011.html output/
	make pdf

pdf:
	cp source/Ref.bib .
	pdflatex -output-directory output source/130010011.tex
	bibtex output/130010011.aux
	pdflatex -output-directory output source/130010011.tex
	pdflatex -output-directory output source/130010011.tex
	rm Ref.bib

.PHONY: clean clean-all
test:
	pytest source/test.py
clean:
	rm -rf output
