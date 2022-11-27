---
weight: 11
title: "Hic1 Flox/Cre PCR Protocol"
---


# Hic1 Flox/Cre PCR Protocol

## PCR Protocol

1. Thaw DNA in water bath or incubator
2. Centrifuge and vortex X, MgCl2, and 5X GO buffer
3. Gently flick primers and controls
    1. Hic1 primers: 84, 85, 86 (Max’s primer box)
        1. Hic1 + control: cKO
        2. Hic1 - control: CT2 and H2O
    2. UBC Cre primers: 80, 81, 82, 83 (Max’s primer box)
        1. Cre + control: CT2
        2. Cre - control: cKO and H2O
    3. Zeb2 primers: Zeb1, Zeb2, Zeb3 (Shannon’s box); working on finding primer stock
        1. Zeb2 + control: Zeb2 +
        2. Zeb2 - control: Zeb2 - and H2O
    4. Making Primers: Dilute primers 1:10 in ddH2O (100uL final volume)
4. Make master mix; [PCR calculator](https://docs.google.com/spreadsheets/u/1/d/1KQnku03JQWAxwmSI1ExukldTsRrIlwtF--9MxJH9g_M/edit)
    1. Hic1 use ER Cre
    2. UBC Cre use LSL Cas 9
    3. Zeb2 use Zeb2 flox
5. Label and add 1uL of controls/ DNA to PCR tubes
6. Add Taq polymerase (must be kept on ice!)
7. Vortex and centrifuge master mix
8. Add 24uL of master mix to PCR tubes
9. Centrifuge PCR strips
10. Place in PCR machine
    1. Hic1 & UBC Cre: ER Cre setting (machine A, B, D)
    2. Zeb2: Zeb2 setting (machine C)
    {{< hint info >}}  
If not running gel day of PCR, PCR product can be kept in 4C overnight
    {{< /hint >}}

## Gel Electrophoresis
1. Make agarose gel (more % agarose for small fragments)
    1. Hic1 gel (small): 1.5% (1.5g) agarose and 100mL **TBE**
    2. Zeb2 & UBC Cre (small): 2.5% (2.5g) agarose and 100mL TAE
    3. Add 4uL EtBr for small gel; > 20 samples
    4. Add 8uL EtBr for large gel; < 20 samples
    5. For large gel double grams of agarose and volume of buffer
2. Microwave gel bottle for 1.5 - 2 minutes until agarose has dissolved; add EtBr (mix well) and let cool for 15 minutes
3. Load gel mold & combs
4. Pour liquid into gel mold; pop/move bubbles to the bottom with pipet tip; let cool for 10 - 15 minutes
5. Remove combs & place gel into easycast
6. Fill easycast with 1x TAE OR 1x TBE (for Hic1) to cover gel
7. Load 10uL gene ladder in the first lane; 20uL of sample in other lanes
8. Run gel @ 90-120V
    1. UBC Cre & Zeb2: 35 minutes
    2. Hic1: 80 minutes
9. UV Image

## Results

### Hic1 Expected Bands:
- WT: 650bp
- Flox: 700bp
- Deletion: 320bp

### UBC Cre Expected Bands:
- Cre +: band @ 100bp
- Cre -: no band @ 100bp

{{< lightbox src="Cre.jpg" caption="CRE: 1st lane: Cre positive sample; 2nd lane: Cre negative sample; 3rd lane: positive control; 4th lane: H20 control" >}} 

{{< lightbox src="Hic1_floxed.jpg" caption="Hic1 floxed: 1st lane: Hic1 WT (650bp); 2nd lane: Hic1 floxed (700bp)" >}} 