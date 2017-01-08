GENERAL_PROFILES=$(shell ls params/ | xargs -Ixx echo "profiles/xx-Profile.md")
YOUTUBE_PROFILES=$(shell ls params/ | xargs -Ixx echo "profiles/xx-Profile-Youtube.md")
DIGEST_PROFILES=$(shell ls params/ | xargs -Ixx echo "profiles/xx-Profile-Digest.md")
YOUTUBE_DIGEST_PROFILES=$(shell ls params/ | xargs -Ixx echo "profiles/xx-Profile-Digest-Youtube.md")

all: Makefile $(GENERAL_PROFILES) $(YOUTUBE_PROFILES) $(DIGEST_PROFILES) $(YOUTUBE_DIGEST_PROFILES)

profiles/%-Profile.md: params/% Profile-Template.md.m4
	m4 -DPARAMS=$< ./Profile-Template.md.m4 > $@

profiles/%-Profile-Youtube.md: profiles/%-Profile.md
	sed "s/\\[\\(.*\\)\\](\\(.*\\))/\\1: \\2/" $< > $@

profiles/%-Profile-Digest.md: params/% Digest-Profile-Template.md.m4
	m4 -DPARAMS=$< ./Digest-Profile-Template.md.m4 > $@

profiles/%-Profile-Digest-Youtube.md: profiles/%-Profile-Digest.md
	sed "s/\\[\\(.*\\)\\](\\(.*\\))/\\1: \\2/" $< > $@

.PHONY: clean

clean:
	rm -rfv ${GENERAL_PROFILES} ${YOUTUBE_PROFILES} $(DIGEST_PROFILES) $(YOUTUBE_DIGEST_PROFILES)
