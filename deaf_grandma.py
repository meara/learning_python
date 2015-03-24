# Borrowed from Learn to Program by Chris Pine:
# https://pine.fm/LearnToProgram/
# 
# DEAF GRANDMA
# 
# Whatever you say to Grandma (whatever you type
# in), she should respond with this:
# HUH?! SPEAK UP, SONNY!
# unless you shout it (type in all capitals). If you shout, she can
# hear you (or at least she thinks so) and yells back:
# NO, NOT SINCE 1938!
# To make your program really believable, have Grandma shout a
# different year each time, maybe any year at random between 1930
# and 1950. (This part is optional.)
# You can’t stop talking to Grandma until you shout BYE.
# Hint 1: Don’t forget about chomp! 'BYE' with an Enter at the end is
# not the same as 'BYE' without one! --(does Python have a chomp equivalent?)
# Hint 2: Try to think about what parts of your program should
# happen over and over again. All of those should be in your while
# loop.
# Hint 3: People often ask me, “How can I make rand give me a
# number in a range not starting at zero?” Well, you can’t; rand just
# doesn’t work that way. So, I guess you’ll have to do something to
# the number rand returns to you.
# • Deaf grandma extended. What if Grandma doesn’t want you to
# leave? When you shout BYE, she could pretend not to hear you.
# Change your previous program so that you have to shout BYE
# three times in a row. Make sure to test your program: if you shout
# BYE three times but not in a row, you should still be talking to
# Grandma.