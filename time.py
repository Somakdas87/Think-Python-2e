# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 19:12:43 2021

@author: somak
"""

import time

t=time.time()
"""
the epoch (reference point) for time 
on python is January 1st, 1970
"""

sec=t%60
mins=(t//60)%60
hrs=(t//3600)%24
days=int(1+(t//(3600*24)))


"""
The following calculations will not work 
past this century.
the rule of division by 400 has been skipped.
Someone should be kind enough to incorporate that
before the turn of the century.
I am moving on to other projects.
I may come back later if I remember.
"""
res_yy=days%(3*365+366)
yyyy=1970+(days//(3*365+366))*4
yyyy=int(yyyy+res_yy//365)
dd=0
mm=0

for i in range(1970, yyyy):
    if i%4==0:
        days=days-366
    else:
        days=days-365

"""
day counts that I get confused with:

    regular: 31 28 31 30  31  30  31  31  30  31  30  31
    cumul:   31 59 90 120 151 181 212 243 273 304 334 365
    
    leap :  31 29 31 30  31  30  31  31  30  31  30  31
    cumul:  31 60 91 121 152 182 213 244 274 305 335 366
    
"""
if yyyy%4==0:
    if days<=31:
        mm=1
        dd=days
    elif days<=60:
        mm=2
        dd=days-31
    elif days<=91:
        mm=3
        dd=days-60
    elif days<=121:
        mm=4
        dd=days-91
    elif days<=152:
        mm=5
        dd=days-121
    elif days<=182:
        mm=6
        dd=days-152        
    elif days<=213:
        mm=7
        dd=days-182
    elif days<=244:
        mm=8
        dd=days-213
    elif days<=274:
        mm=9
        dd=days-244
    elif days<=305:
        mm=10
        dd=days-274
    elif days<=335:
        mm=11
        dd=days-305
    else:
        mm=12
        dd=days-335
else:
    if days<=31:
        mm=1
        dd=days
    elif days<=59:
        mm=2
        dd=days-31
    elif days<=90:
        mm=3
        dd=days-59
    elif days<=120:
        mm=4
        dd=days-90
    elif days<=151:
        mm=5
        dd=days-120
    elif days<=181:
        mm=6
        dd=days-151        
    elif days<=212:
        mm=7
        dd=days-181
    elif days<=243:
        mm=8
        dd=days-212
    elif days<=273:
        mm=9
        dd=days-243
    elif days<=304:
        mm=10
        dd=days-273
    elif days<=334:
        mm=11
        dd=days-304
    else:
        mm=12
        dd=days-334
"""
Excuse me for all that hard coding.
I could not think of anything cleaner
""" 

   
print("Greenwich Mean Time!")
print("Time: "+str(hrs) +" hrs : " + str(mins) +" mins : "+ str(sec) +" secs")
print("Date: "+str(mm)+"/"+str(dd)+"/"+str(yyyy))