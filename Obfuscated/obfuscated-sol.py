from string import ascii_uppercase as v, ascii_lowercase as k
def check_flag(s):
        """ Length of the flag should be exactly 25 characters"""
	if len(s) != 0x19:
		return False
	s = list(s)
        """ 0x61a83 => 40003
        lst = [s.pop(r) for r in [20, 17, 15, 13, 11, 2]]
        revlst = lst[::-1]
        strlst = repr(lst)[::-1]
        chars = strlst[2::5] => '400003'
        final = int(chars) = 400003

        From 'lst' we can determine characters position in the flag
        21st character = 3
        18th character = 0
        16th character = 0
        14th character = 0
        12th character = 0
        3rd character = 4

        len(s) = 25 - 6 = 19
        """
	if int(`[s.pop(r) for r in ([2] + [i for i in range(11, 18, 2)] + [20])[::-1]][::-1]`[2::5]) != 0x61a83:
		return False

        """
        ("1"*5)[:2] = "11"
        ("1"*5)[2:] = "111"
        
        The map() statement can be translated as:
        newlst = [int(p, 2) for item in ["11", "111"]]
            where 2 is base i.e. it is converting binary to decimal which gives
            us newlst = [3, 7]

        plist = [s.pop(r) for r in newlst[::-1]]

        Presence of set() tells us that plist might contain same two items.
        We need to keep that in mind.

        list() converts the set(plist) to list again and len() calculates the
        length of this new list.

        Since we have popped two items and used set(), len() might return 1 or 2.
        Let's test for 2.

        If len() returns 2 then it means that "h" is in 3rd position in our
        flag "s" and character at 4th position and 8th position for s (len(s) = 19)
        are different.

        But this is not possible as we have already established that 3rd
        position has '3'.

        Now, we are sure that if len() returns 1 and in 2nd position of our
        flag s, there is a character "h" and characters at 4th position and
        8th position for s (len(s) = 19) have same character.

        len(s) = 19 - 2 = 17
        """
	if len(list(set([s.pop(r) for r in map(lambda p: int(p, 2), [("1"*5)[:2], ("1"*5)[2:]])[::-1]]))) != s.index("h"):
		return False
	y, z = [], []

        """

        rplist = [repr(y.append(s.pop(-1))) + repr(z.append(s.pop(-1))) for w in range(2)]
        
        y will have len(s) - 1 and len(s) - 3 items of s (len(s) = 17)
        z will have len(s) - 2 and len(s) - 4 items of s
        
        But since list.append() doesn't return anything (None to be precise),
        we will have:
        rplist = ["NoneNone", "NoneNone"]
        set(rplist) => set(['NoneNone'])
        list(set(rplist)) => ['NoneNone']

        len(set(rplist)) will return 1

        len(set(rplist)) - 1 => 0

        Hence, u = 0

        len(s) = 17 - 4 = 13
        """
	u = len(list(set([repr(y.append(s.pop(-1))) + repr(z.append(s.pop(-1))) for w in range(2)]))) - 1

        """
        Due to the presence of set(), we assume that there are duplicate values
        in 'y' and 'z' for the sake of simplicity.

        ^ means XOR in Python

        Since y and z have two values that are duplicates:

        len(list(set(y))) => 1
        len(list(set(z))) => 1
        
        len(s) = 13
        """
	if u != len(list(set(y))) ^ len(list(set(z))):
		return False
        """
        0x1e = 30
        So, ord(y[0]) ^ ord(z[0]) must be equal to 30. We should keep this in
        mind while choosing characters for our flag.

        len(s) = 13
        """
	if (ord(y[u]) ^ ord(z[u])) ^ 0x1e != 0:
		return False
        """
        v contains all the uppercase letters
        Upto now len(s) = 13

        But s.pop() decreases the length of s by one so len(s) = 12

        We don't know what v.index() returns but we can say that
        len(s) ^ 30 = v.index(s.pop())
        v.index(s.pop()) = 18

        We have 'S' in 19th place so, for s with length = 13 we have 'S' in the end.

        len(s) = 12
        """
	if v.index(s.pop()) ^ len(s) ^ 0x1e != 0:
		return False

        """
        filter(lambda c: c in v, s) returns all the characters that are 
        uppercased in 's'

        Similarly, filter(lambda c: c in k, s) returns all the characters that
        are lowercased in 's' here.

        len(s) = 12 
        """
	a, i = filter(lambda c: c in v, s), filter(lambda c: c in k, s)

        """
        len(s) = 12

        0x50 = 80
        0x4f = 79
        map(lambda a: a + 0x50, [7, 2, 4, -8]) + [0x4f] * 4 gives us
        [87, 82, 84, 72, 79, 79, 79, 79]

        If we convert each integer from the result to characters, we see that
        it results to ['W', 'R', 'T', 'H', 'O', 'O', 'O', 'O']

        Therefore, a = WRTHOOOOO

        So, we must have WRTHOOOOO within s when len(s) = 12
        """
	if map(lambda a: a + 0x50, [7, 2, 4, -8]) + [0x4f] * 4 != map(ord, a):
		return False

        """
        i must have these characters: 'a', 'e', 'h' and 't' len(i) = 4

        i[1:3] slices the string and returns 2nd and 3rd character
        
        i[2:0:-1] slices the string from 3rd character to 1st character but not
        including it.

        What we can notice is, first and last character don't change.
        From list("hate") we can say the first character is 'h' and last
        character is 'e'. Since final string should result to "hate" and we
        know that swapping of 2nd and 3rd character happens as
        i[1:3] = i[2:0:-1], we can say that i = "htae"

        We, now, have to fit "htae" within s for len(s) = 12 along with
        "WRTHOOOO"
        """
	i[1:3] = i[2:0:-1]
	if i != list("hate"):
		return False
	return True

"""
This challenge can have many flags.
The flag we submitted to solve the challenge was:
    Wh4teaeReTH0O0O0O0OS3XFXF

Here's how we derived it
We supposed that s = "abcdefghijklmnopqrstuvwxy"

Let s' be a string that is derived by popping items from s. s' can have
variable length.

How s' changes
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
1. a b c d e f g h i j k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  len(s) = 25
2. a b d e f g h i j k m  o  q  s  t  v  w  x  y                    len(s) = 19
3. a b d f g h j k m o q  s  t  v  w  x  y                          len(s) = 17
4. a b d f g h j k m o q  s  t                                      len(s) = 13
5. a b d f g h j k m o q  s                                         len(s) = 12

1. After popping itemsj from locations 20, 17, 15, 13, 11, 2 from original
   string "s"
2. After popping items from locations 3, 7 of s'
3. After popping four items from new s'
4. After popping an item from new s'
5. Resulting s'

Retrieving flag 's' based on what we know
   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
1. a b 4 d e f g h i j k  0  m  0  o  0  q  0  s  t  3  v  w  x  y  len(s) = 25
2. a h 4 d e f g h e j k  0  m  0  o  0  q  0  s  t  3  v  w  x  y
3. a h 4 d e f g h e j k  0  m  0  o  0  q  0  s  t  3  X  F  X  F
4. a h 4 d e f g h e j k  0  m  0  o  0  q  0  s  S  3  X  F  X  F
5. W h 4 t e a e R e T H  0  O  0  O  0  O  0  O  S  3  X  F  X  F 


1. Substituting the characters "400003" into their respective character
   positions as derived from our analysis of second 'if' statement 
2. Since 4th and 8th characters are same in the s', we replace 'i' (8th
   character of s') with 'e'. We also know that 'h' lies in the 2nd place in
   the original string. Now making changes to s using s' we get 2.
3. We know that u and v contain the item popped from s' (when len(s') = 19).
   We also know that
   u = [s'[len(s') - 1], s'[len(s) - 3]] and
   v = [s'[len(s') - 2], s'[len(s) - 4]]
   We have supposed that u and v both contain same characters in them too.
   Since u[0] ^ v[0] == 30, we chose 'X' for u and 'F' for v
   So, we have u = ['X', 'X'], v = ['Y', 'Y']

   We now make changes to the original string s using s'
4. We know that last item for s' when len(s') = 13 has character 'S', so we make
   changes to the original string s.
5. We have to fit 'WRTHOOOO' and 'hate' within s' for len(s') = 12. For latter
   string, 'e' at 5th place will already be popped off, so we have to be careful
   while making changes. Also the order should be 'htae' so that when this
   statement i[1:3] = i[2:0:-1] runs, we have "hate" stored in i.
   By making appropriate changes, we get the flag.

"""
