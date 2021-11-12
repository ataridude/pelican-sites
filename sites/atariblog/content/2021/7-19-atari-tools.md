Title: Creating and using disk images
Date: 2021-7-19
Status: published

I recently discovered [Mikey Walters's Atari BASIC series](https://wearethemutants.com/author/webmikey7/), and my sons
and I went through the tutorials, learning a lot about Atari BASIC along the way.  We typed in most of the program, but
I also wanted to try Mikey's revised version.

I downloaded the [BASIC files](https://wearethemutantsdotcom.files.wordpress.com/2017/06/basfiles.zip) for Mikey's game,
downloaded and compiled [atari-tools](https://github.com/jhallen/atari-tools) on my iMac, and used the `atr` command from 
atari-tools to make a disk image so that I could easly copy the game to my Atari 800:

```
% atr basfiles.atr mkfs dos2.5
% ls -l basfiles.atr
-rw-rw-r--  1 daniel  staff  133136 Jul 19 15:12 basfiles.atr
% atr basfiles.atr ls
% atr basfiles.atr put basfiles/asltorg.bas 
asltorg.bas
% atr basfiles.atr put basfiles/asltrev.bas 
asltrev.bas
% atr basfiles.atr ls
asltorg.bas  asltrev.bas                                                      
% atr basfiles.atr ls -l

-rw--  11584 ( 93) asltorg.bas  
-rw--  13065 (105) asltrev.bas  

2 entries

198 sectors, 24649 bytes

812 free sectors, 103936 free bytes

% 
```

Once the `basfiles.atr` disk image was ready, I moved it to my TNFS server, and mounted it on my FujiNet using the web UI:

![basfiles.jpg](/images/fujinet/basfiles.jpg)

Then I ran BASIC on my Atari 800, loaded the program, and was off to the races.

Very fun stuff.
