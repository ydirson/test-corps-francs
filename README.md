# (Manifest for a) Generic Army-building tool for figurine-based wargaming

This *may* turn into a useful tool at some point, just don't hold your
breath.

## Starting point

There are many wargaming rules to experiment with, and that's great.
But even when their army-building rules are simple, manually keeping
track of them, and following evolutions of the rules is tedious.

Thus, Army Builder apps are a thing.  But...  many are of limited scope
(tied to games of a specific editor, or even to just one game); many
are freemium apps (where you have no control over the project, which
could vanish, maybe with your data, as the Real World goes on); only a
few of them can support arbitrary rules (any other than New Recruit?);
even less have the flexibility of Open Source (quite helpful when
noone else seems to care about that feature you'd like... and to get a
chance to survive those Real World events)

So, what about playing with the idea of making a Free Software / Open
Source Army Builder, generic enough to be able to setup arbitrary
rules?  What would be needed?

## Objectives

Basically, an Army Builder takes Faction Books on one hand, lets the user
compose units according to some game-specific rules (choices for era,
faction, army type, units, figs, equipment, skills, ...), and produces
Army Lists in one form or another (text, printable cards or sheets,
exchange format for other apps, ...), with sufficient info to use in a
game as a reference for those units.

This means there should be enough info in an Faction Book to express:
- compatibility rules (what is allowed where: units and equipment
  according to era, limitations of given army type, ...)
- unit stats and skills that should be part of the Army Sheet
- effects of options (equipment, weapons, skills, ...) on unit stats

So there needs to be a formalism to express those info to constitute
an Faction Book.  And naturally a way to check a given Faction Book is valid
(i.e. can be used by the Army Builder), and conforms to a give Set of
Rules (i.e. does not violate the rules of the chosen game).

This asks for:
- at generic level:
  - a **schema for Game Rules**
  - a **schema for Faction Books**
- at a specific game's level:
  - **game rules** further specializing the *schema for Faction Books*
  - one or more **Faction Book** providing template unit and equipment
    types
- and then the tooling to manipulate those, and for the Player to
  actually build an Army

Now, rules evolve, get revised and balanced.  This eventually comes
with an impact on unit stats, and the player should get empowered with
the effect of those changes to make the necessary decisions to keep
the army valid (ie. the app should not just adjust costs and drop
items now considered invalid so old Army Lists fit in new rules).  The
player should also be allowed to continue using a previous version of
the rules, it is no one's role to restrict that.

## More concrete stuff

Whereas [*General's
Familiar*](https://github.com/ydirson/generals-familiar/#generals-familiar)
is meant to be available from a gaming table and targets mobile
devices (through a web app), this app will benefit from a larger
screen, and a desktop app looks like a good choice at this point.
That also creates a good opportunity to look at the current state of
[modern cross-platform GUI](https://areweguiyet.com/) (in Rust
naturally, because there's already a lot to be learnt in there).

Keeping an history of the various rules and appears natural, and
naturally that kind of stuff those days is best managed using Git.  A
(public or private but network-reachable) Git repository is also an
easy way to make an Army List accessible from a game assistant
(*General's Familiar* or another).
