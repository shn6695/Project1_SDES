FILES := 130010011.pdf 

main :
	cd source && python 130010011.py
	jupyter nbconvert --to html source/130010011.ipynb
	mv source/130010011.html output/
	make paper

paper:
	cp source/Ref.bib .
	pdflatex -output-directory output source/130010011.tex
	bibtex output/130010011.aux
	pdflatex -output-directory output source/130010011.tex
	pdflatex -output-directory output source/130010011.tex
	rm Ref.bib

.PHONY: clean clean-all
tests:
	pytest source/test.py
clean:
	rm -rf output
