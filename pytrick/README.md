pyspades
========

python modules for modelling trick-taking card games

this was a small project to get familiar with python that I wrote in March 2013.

i'm currently refactoring with sane naming, organization and unit tests.


retrospective
=============

this was a fun exercise that increased my awareness of applying an analytical perspective to modelling a realworld problem with data structures and code.
with that said, most of this is implemented incredibly naively. i've abused inheritence and typing in the process of learning.
the program logic is disjointed and convoluted. i directly access data instead of using the object's provided methods in some cases.
all of these were decisions made in the moment to get things to work, and as i now try to extend the code base or add views i am running into the limitations set by lack of foresight that comes with inexperience.

what i've learned:

- don't fight convention
- shoehorning language/library features has made for some unnecessarily obfuscated code
- seperation of concerns is vital -> easy with the concrete modules, but got complicated w/ abstract ones
- sitting down and coding before planning is Bad; don't do it
- composition is usually better suiting than inheritance
- do not hardcore stdin prompts, it creates headaches down the line
- if i implement data abstraction methods in modules, they should be utilized once imported
- test. test. test. i did some naive testing, but i never kept up with the growth of the code and now they are useless.
- if a method or block of code is a mess, profile its action and remove the offending code then rewrite code to the spec rather than 'fixing' the bad code
- i have made many, many mistakes that i was complicit in committing. i've made even more that i'm unaware of.
