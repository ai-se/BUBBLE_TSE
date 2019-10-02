all: git

clean:
	@echo ""
	@echo "Cleaning Auxillary files"
	@echo ""
	@- latexmk -CA
	@echo ""

git: clean
	@echo "Syncing with Overleaf"
	@echo ""
	@- git add --all .
	@- git commit -am "Local Changes"
	@- git push origin master
	@echo ""