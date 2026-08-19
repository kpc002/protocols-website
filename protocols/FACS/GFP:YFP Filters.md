---
title: "GFP:YFP Filters"
description: 'The filter setup depends on your particular machine and how the lasers/filters are set up inside.'
order: 10
author: "Goldrath Lab"
date: last-modified
---

The filter setup depends on your particular machine and how the lasers/filters are set up inside.

there are some examples of setup you can look at online  
  
<span class="underline">http://www.cyto.purdue.edu/hmarchiv/Current/1356.htm</span>  
use a 510/21BP  plus the 505LP dichroic in the FITC channel plus a  
550/30 BP with a 525LP dichroic in the PE channel. The 525LP replaces  
the usual 550LP.  
  
  
<span class="underline">http://www.cyto.purdue.edu/hmarchiv/Current/1355.htm</span>  
  
            LP          BP  
YFP          525LP             530/30  
GFP          502LP             510/20  
  
<span class="underline">http://www.cyto.purdue.edu/hmarchiv/Current/1354.htm</span>  
 For YFP 550/30BP with the 525LP en for GFP 510/20BP with (or without)  
the 505LP.

Most likely you won't have those filters at your core and I suggest buying it from Omega Filters <span class="underline">https://www.omegafilters.com</span>,  they cost about $200 each. Since they are a jack-of-all-trades mirror maker, make sure you order the right size for the FACS machine. 

Goldrath Lab specifications:

525DRLP and 510DF21 from Omega Filters were fitted on Aria and LSRII, Fortessa

These three machines are set up differently because of the laser configuration,

For LSRII, GFP takes place of FITC and YFP takes place of PERCP5.5.  I used 510/21+502LP for GFP and 530/30+525LP for YFP. (Monica Macal/Louise knows how to change it)

For Fortessa, GFP takes place of FITC and YFP takes place of PE.  I used 510/21+502LP for GFP and 525/30+525LP for YFP. There are pictures of filter configuration posted on the side wall. (Martin/Kyla/Louise knows how to change it)

For Aria, it is the same as Fortessa. There are also pictures of filter configuration on the side of the filter panel. (The pictures made by Karen is pretty self-explainable)

(note 530/30, 525/30 , and 535/30 are pretty much interchangeable here, 510/20 is interchangeable with 510/21, 502LP is interchangeable with 505LP, depending on the current filters you have)

If you have any problem figuring out the filters setup, ask somebody with extensive knowledge of the laser/filters, or just BD support technician(in person).  
  
  
Compensation for FACS analysis

The key thing is to get really bright controls for GFP/YFP singles. Also, try to keep the voltages of both GFP and YFP the same, otherwise the signal will bleed too much, Start with 500 V each. Also the same compensation can be used again and again unless things are looking funny.
