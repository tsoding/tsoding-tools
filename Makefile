GENERAL_PROFILES=profiles/Beatwave-Profile.md profiles/Morganey-Profile.md profiles/Pacmacs-Profile.md
YOUTUBE_PROFILES=profiles/Beatwave-Profile-Youtube.md profiles/Morganey-Profile-Youtube.md profiles/Pacmacs-Profile-Youtube.md

all: Makefile $(GENERAL_PROFILES) $(YOUTUBE_PROFILES)

profiles/%-Profile.md: %.profile Profile-Template.md Expand-Template.sh
	./Expand-Template.sh $< ./Profile-Template.md > $@

profiles/%-Profile-Youtube.md: profiles/%-Profile.md
	sed "s/\\[\\(.*\\)\\](\\(.*\\))/\\1: \\2/" $< > $@

.PHONY: clean

clean:
	rm -rfv ${GENERAL_PROFILES} ${YOUTUBE_PROFILES}
