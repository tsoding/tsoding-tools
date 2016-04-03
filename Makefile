GENERAL_PROFILES=profiles/OCaml-Profile.md profiles/Whatever-Profile.md profiles/Horta-Profile.md profiles/Beatwave-Profile.md profiles/Morganey-Profile.md profiles/Pacmacs-Profile.md profiles/Ebf-Profile.md
YOUTUBE_PROFILES=profiles/OCaml-Profile-Youtube.md profiles/Whatever-Profile-Youtube.md profiles/Horta-Profile-Youtube.md profiles/Beatwave-Profile-Youtube.md profiles/Morganey-Profile-Youtube.md profiles/Pacmacs-Profile-Youtube.md profiles/Ebf-Profile-Youtube.md

all: Makefile $(GENERAL_PROFILES) $(YOUTUBE_PROFILES)

profiles/%-Profile.md: params/%.param Profile-Template.md Expand-Template.sh
	./Expand-Template.sh $< ./Profile-Template.md > $@

profiles/%-Profile-Youtube.md: profiles/%-Profile.md
	sed "s/\\[\\(.*\\)\\](\\(.*\\))/\\1: \\2/" $< > $@

.PHONY: clean

clean:
	rm -rfv ${GENERAL_PROFILES} ${YOUTUBE_PROFILES}
