all: Makefile profiles/Beatwave-Profile.md profiles/Morganey-Profile.md profiles/Pacmacs-Profile.md profiles/Beatwave-Profile-Youtube.md profiles/Morganey-Profile-Youtube.md profiles/Pacmacs-Profile-Youtube.md

profiles/Beatwave-Profile.md: General-Part.md Beatwave-Part.md
	cat Beatwave-Part.md General-Part.md > profiles/Beatwave-Profile.md

profiles/Morganey-Profile.md: General-Part.md Morganey-Part.md
	cat Morganey-Part.md General-Part.md > profiles/Morganey-Profile.md

profiles/Pacmacs-Profile.md: General-Part.md Pacmacs-Part.md
	cat Pacmacs-Part.md General-Part.md > profiles/Pacmacs-Profile.md

profiles/Beatwave-Profile-Youtube.md: profiles/Beatwave-Profile.md
	sed "s/\\[\\(.*\\)\\](\\(.*\\))/\\1: \\2/" profiles/Beatwave-Profile.md > profiles/Beatwave-Profile-Youtube.md

profiles/Morganey-Profile-Youtube.md: profiles/Morganey-Profile.md
	sed "s/\\[\\(.*\\)\\](\\(.*\\))/\\1: \\2/" profiles/Morganey-Profile.md > profiles/Morganey-Profile-Youtube.md

profiles/Pacmacs-Profile-Youtube.md: profiles/Pacmacs-Profile.md
	sed "s/\\[\\(.*\\)\\](\\(.*\\))/\\1: \\2/" profiles/Pacmacs-Profile.md > profiles/Pacmacs-Profile-Youtube.md
