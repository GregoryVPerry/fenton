# fenton
specify target word then find the top n words from a dictionary which are closest using distance matching methods

```
$ python3 fenton.py -h
usage: python3 fenton.py [-h] TARGETWORD [-m 1|2|3|4|5|6|7] [-d DICTIONARY] [-n NUMWORDS] [-l] [-s] [-v]

fenton: specify target word then find the top n words from a dictionary
        which are closest using distance matching methods

positional arguments:
  TARGETWORD            target word to analyze

optional arguments:
  -h, --help            show this help message and exit
  -m METHOD, --method METHOD
                        distance matching method to use, default = 7
                        1 = Damerau-Levenshtein Distance
                        2 = Hamming Distance
                        3 = Jaro Distance
                        4 = Jaro-Winkler Distance
                        5 = Levenshtein Distance #1
                        6 = Levenshtein Distance #2
                        7 = The Kitchen Sink
  -d DICTIONARY, --dictionary DICTIONARY
                        dictionary of words to compare, default words.txt
  -n NUMWORDS, --number NUMWORDS
                        number of matches to return, default 10
  -l, --lower           convert dictionary to lowercase before analysis
  -s, --strip           strip punctuation from dictionary before analysis
  -v, --verbose         verbose mode

$ python3 fenton.py democracy -n 30 -l -s -v # return 30 results with kitchen sink (all methods)
targetword        =  democracy
method            =  7
dictionary        =  words.txt
number of matches =  30
lower             =  True
strip             =  True
verbose           =  True

Results for democracy using Damerau-Levenshtein Distance:

0 democracy
1 democracys
2 democrat
2 democrats
2 democrats
2 democraw
2 demonocracy
2 dulocracy
2 neocracy
2 nomocracy
2 timocracy
3 adhocracy
3 albocracy
3 autocracy
3 beerocracy
3 cosmocracy
3 delicacy
3 deliracy
3 democracies
3 democratic
3 demography
3 demoniac
3 demoniacs
3 demonry
3 demorage
3 desperacy
3 doulocracy
3 gunocracy
3 gynocracy
3 hemicrany

Results for democracy using Hamming Distance:

0 democracy
1 democracys
2 democrat
2 democrats
2 democrats
2 democraw
2 dulocracy
2 nomocracy
2 timocracy
3 adhocracy
3 albocracy
3 autocracy
3 democracies
3 democratic
3 demoniac
3 demoniacs
3 desperacy
3 gunocracy
3 gynocracy
3 hemicrany
3 logocracy
3 mobocracy
3 monocracy
3 popocracy
3 theocracy
4 aerocraft
4 dedolency
4 demetra
4 demiglace
4 demigrate

Results for democracy using Jaro Distance:

1.0 democracy
0.9666666666666667 democracys
0.9393939393939394 demonocracy
0.9296296296296296 mediocracy
0.8974358974358975 antidemocracy
0.8962962962962964 democratic
0.8888888888888888 ocracy
0.8842592592592592 neocracy
0.8842592592592592 democraw
0.8842592592592592 democrat
0.8809523809523809 democratically
0.872053872053872 democracies
0.8541666666666666 undemocratically
0.8518518518518517 undemocratic
0.8518518518518517 timocracy
0.8518518518518517 theocracy
0.8518518518518517 monocracy
0.8518518518518517 mobocracy
0.8518518518518517 dulocracy
0.8518518518518517 democrats
0.8518518518518517 democrats
0.8518518518518517 democratical
0.8518518518518517 adhocracy
0.8425925925925926 predemocracy
0.8425925925925926 nondemocracy
0.8412698412698413 hemocry
0.8412698412698413 demonry
0.8366402116402116 demarchy
0.8366402116402116 decarchy
0.8333333333333334 medora

Results for democracy using Jaro-Winkler Distance:

1.0 democracy
0.98 democracys
0.9636363636363636 demonocracy
0.9377777777777778 democratic
0.9305555555555555 democraw
0.9305555555555555 democrat
0.9296296296296296 mediocracy
0.9285714285714286 democratically
0.9232323232323232 democracies
0.9111111111111111 democrats
0.9111111111111111 democrats
0.9111111111111111 democratical
0.9047619047619048 demonry
0.8974358974358975 antidemocracy
0.8955555555555555 demography
0.888888888888889 demo
0.888888888888889 demo
0.8888888888888888 ocracy
0.8856481481481482 demarchy
0.8842592592592592 neocracy
0.8833333333333333 demorage
0.882828282828283 demonomancy
0.882828282828283 demonically
0.882828282828283 demographic
0.882828282828283 democritean
0.882828282828283 democratize
0.882828282828283 democratist
0.882828282828283 democratism
0.882828282828283 democratise
0.882828282828283 democratian

Results for democracy using Levenshtein Distance #1:

82 democracy
78 democracys
75 demonocracy
72 prodemocracy
72 predemocracy
72 nondemocracy
70 democratic
69 theodemocracy
69 overdemocracy
69 antidemocracy
67 neocracy
67 hyperdemocracy
67 democraw
67 democratically
67 democrat
67 democracies
64 undemocratic
64 timocracy
64 theocracy
64 nomocracy
64 monocracy
64 mobocracy
64 dulocracy
64 democrats
64 democrats
64 democratical
64 aristodemocracy
64 adhocracy
63 ocracy
62 undemocratically

Results for democracy using Levenshtein Distance #2:

0 democracy
1 democracys
2 democrat
2 democrats
2 democrats
2 democraw
2 demonocracy
2 dulocracy
2 neocracy
2 nomocracy
2 timocracy
3 adhocracy
3 albocracy
3 autocracy
3 beerocracy
3 cosmocracy
3 delicacy
3 deliracy
3 democracies
3 democratic
3 demography
3 demoniac
3 demoniacs
3 demonry
3 demorage
3 desperacy
3 doulocracy
3 gunocracy
3 gynocracy
3 hemicrany

$ python3 fenton.py republican -m 1 -n 30 -l -s -v # find 30 matches using only Damerau-Levenshtein Distance
targetword        =  republican
method            =  1
dictionary        =  words.txt
number of matches =  30
lower             =  True
strip             =  True
verbose           =  True

Results for republican using Damerau-Levenshtein Distance:

0 republican
1 republica
1 republical
1 republicans
1 republicans
2 irrepublican
2 publican
2 republic
2 republics
2 republics
2 unrepublican
3 archpublican
3 nonrepublican
3 prerepublican
3 prorepublican
3 publica
3 publicae
3 publicans
3 replica
3 replicant
3 replicas
3 replicon
3 reptilian
3 republicanise
3 republicanism
3 republicanize
3 republication
3 republish
3 rubican
4 antirepublican
```
