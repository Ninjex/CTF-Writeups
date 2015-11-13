Description: Solved by 992 teams.
Oh look, it's a perfectly innocent picture of an [apple](https://www.easyctf.com/static/problems/apple/apple.jpg. Nothing to see here!)

Solving this challenge is pretty easy. We just had to click the link, download the image and issue following commands under Linux
``` strings apple.jpg | grep easyctf ```
which revealed the flag to be `easyctf{w0w_much_appl3s}`
