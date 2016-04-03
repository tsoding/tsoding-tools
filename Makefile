GENERAL_PROFILES=$(shell ls params/ | xargs -Ixx echo "profiles/xx-Profile.md")
YOUTUBE_PROFILES=$(shell ls params/ | xargs -Ixx echo "profiles/xx-Profile-Youtube.md")

all: Makefile $(GENERAL_PROFILES) $(YOUTUBE_PROFILES)

profiles/%-Profile.md: params/% Profile-Template.md Expand-Template.sh
	./Expand-Template.sh $< ./Profile-Template.md > $@

profiles/%-Profile-Youtube.md: profiles/%-Profile.md
	sed "s/\\[\\(.*\\)\\](\\(.*\\))/\\1: \\2/" $< > $@

.PHONY: clean

clean:
	rm -rfv ${GENERAL_PROFILES} ${YOUTUBE_PROFILES}
