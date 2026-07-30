---
title: "sgRNA_Viral_transduction_Wei_2019"
description: 'Methods from Wei et al 2019'
order: 10
author: "Goldrath Lab"
date: last-modified
---

[Download the original paper](s41586-019-1821-z.pdf){.btn .btn-primary download="s41586-019-1821-z.pdf"}

Methods from Wei et al 2019

**Cell purification and Viral Transduction**

Naïve Cas9-expressing OT-I cells were isolated from the spleen and peripheral lymph nodes (PLNs) of Cas9-OT-I mice using naïve CD8a+ T cell isolation kit (Miltenyi Biotec 130-096-543) according to manufacturer's instructions. Purified naïve OT-I cells were activated in vitro for 18h with 10 mg/ml anti-CD3 (2C11; Bio X Cell), 5 μg/ml anti-CD28 (37.51; Bio X Cell) before viral transduction. Viral transduction was performed by spin-infection at 800 g at 25 °C for 3 h with 10 mg/ml polybrene (Sigma). Cells were continued to culture with human IL-2 (20 UI/ml; PeproTech), mouse IL-7 (25 ng/ml; PeproTech) and IL-15 (12.5 ng/ml; PeproTech) for 3−4. 502  days. Transduced cells were sorted using a Reflection (i-Cyt) before adoptive transfer into recipients. sgRNAs were designed by using the online tool (https://portals.broadinstitute.org/gpp/public/analysis-tools/sgrna-design). sgRNAs used in this study were as follows: non-targeting control sgRNA: ATGACACTTACGGTACTCGT

> sgRegnase-1: AAGGCAGTGGTTTCTTACGA;
> 
> sgRegnase-1 \#2: GGAGTGGAAACGCTTCATCG;
> 
> sgBatf: AGAGATCAAACAGCTCACCG;
> 
> sgBatf \#2: AGGACTCATCTGATGATGTG (which gave similar results as sgBatf; data not shown);
> 
> sgPtpn2: AAGAAGTTACATCTTAACAC;
> 
> sgPtpn2 \#2: CACTCTATGAGGATAGTCAT (which gave similar results as sgPtpn2; data not shown);
> 
> sgSocs1: TGATGCGCCGGTAATCGGAG;
> 
> sgSocs1 \#2: TGGTGCGCGACAGTCGCCAA (which gave similar results as sgSocs1; data not shown).

The coding sequence of Batf (Addgene \# 34575) was subcloned into pMIG-II retroviral vector (Addgene \# 52107), which was co-transfected into Plat-E cells with the helper plasmid pCL-Eco (Addgene \# 12371) for the production of retrovirus.

**Lentiviral sgRNA metabolic library CRISPR-Cas9 mutagenesis screening**

Lentiviral and retroviral gRNA vector design

The gene list of mouse metabolic library was based on the reported human metabolic genes. A total of 6 gRNAs were designed for each mouse metabolic gene according to our previously published selection criteria and were split into two sub-libraries (AAAQ05 and AAAR07, Supplementary Table 1), each containing 500 non-targeting controls. Oligonucleotides containing the guide sequence were synthesized (Custom Array), PCR amplified, and cloned into the recipient vector via a Golden Gate cloning procedure, including 5 ml Tango Buffer (ThermoFisher), 5 μl DTT (10 mM stock); 5 μl ATP (10 mM stock); 500 ng vector, pre-digested with Esp3I, gel-extracted, and isopropanol-precipitation purified; 100 ng insert PCR product; 1 ml Esp3I (ThermoFisher ER0452); 1 ml T7 ligase (Enzymatics, 3,000 Units/ml, L6020L); and water, up to 50 ml, and incubated in cycle (5 min at 37 °C and 5 min at 20 °C) for 100 times. The product was then purified by isopropanol precipitation and electroporated into STBL4 cells (Life Technologies 11635018). The distribution of the library was determined by Illumina sequencing

**In vivo screening**

Lentivirus was produced by co-transfecting HEK293T cells with the lentiviral metabolic library plasmids, psPAX2 (Addgene plasmid \# 12260) and pCAG4-Eco. At 48 h after transfection, virus was harvested and froze at −80 °C. Four hundred to five hundred million naïve Cas9-expressing OT-I cells were isolated from 8–14 Cas9-OT-I mice and transduced at a MOI of 0.3 to achieve **\~20% transduction efficiency**. After viral transduction, cells were cultured with human IL-2 (20 IU/ml; PeproTech), mouse IL-7 (25 ng/ml; PeproTech) and IL-15 (12.5 ng/ml; PeproTech) for 4 days. **Transduced cells expressing Ametrine were sorted using a Reflection sorter (i-Cyt), and an aliquot of 5 × 106 transduced OT-I cells was saved as “input”** (\~500 × cell coverage per sgRNA). Transduced OT-I cells (5 × 106 cells per recipient) were i.v. transferred into mice at day 14 after B16-Ova melanoma engraftment. Sixty recipients were randomly divided into 3 groups as biological replicates in each sub-library screening. At 7 days after adoptive transfer, transferred Ametrine+ OT-I cells were recovered from the tumor pooled from 20 recipients per sample using a Reflection sorter (i-Cyt). On average, 5 × 105 OT-I cells per sample (\~50 × cell coverage per sgRNA) were recovered for further analysis.
