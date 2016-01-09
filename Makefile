all: Makefile profiles/Beatwave-Profile.md profiles/Morganey-Profile.md profiles/Pacmacs-Profile.md profiles/Beatwave-Profile-Youtube.md profiles/Morganey-Profile-Youtube.md profiles/Pacmacs-Profile-Youtube.md

profiles/%-Profile.md: %-Part.md General-Part.md
	cat $< General-Part.md > $@

profiles/%-Profile-Youtube.md: profiles/%-Profile.md
	sed "s/\\[\\(.*\\)\\](\\(.*\\))/\\1: \\2/" $< > $@

.PHONY: clean

clean:
	rm -rfv profiles/*.md
