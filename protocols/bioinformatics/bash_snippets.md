---
weight: 20
bookFlatSection: false
title: "Bash code snippets"
---

# Bash code snippet magic &#129668;

This is a small collection of `bash` code snippets, that make my life a little bit easier.


## Download all files from a web-directory

This can be usefull if e.g. the sequencing files are provided on a server with an apache directory listing.

```bash
wget --spider -r --no-parent --level=1 --reject index.html* -nd -e \
    robots=off --reject-regex '(.*)\?(.*)' http://igc2.salk.edu/illumina/runs/210824_10XA/Kaech_Anna/ 2>&1 | \
    grep '^--' | awk '{ print $3 }' | sed "s/'/% 27/" | sed -e '1,2d' | sed '$!N; /^\(.*\)\n\1$/!P; D' | \
    aria2c --deferred-input true -x 16 -i -
```


## TSCC

Command to facilitate working with the TSCC

```bash
alias tscc="ssh -X  mheeg@tscc-login2.sdsc.edu"
alias tunneltscc="ssh -NL 22888\:localhost:22888 mheeg@tscc-login2.sdsc.edu &"
```


Put this in the `.bashrc` on TSCC

```bash
interactive_session() {
    #do things with parameters like $1 such as
    echo "Starting Interactive session on ${1} with ${2} cores for ${3:-8} hours"
    qsub -I -l walltime=${3:-8}:00:00 -q $1 -l nodes=1:ppn=$2
}

alias start_jupyter="jupyter lab --no-browser --port 22888 &"
alias tunnel_ssh="ssh -NR 22888:localhost:22888 tscc-login2 &"

alias qstat-queues="qstat -q | head -5 && qstat -q | grep -E 'home-yeo|condo|hotel' --color=never"
alias myqstat="qstat -u mheeg"
```

## Crop PDF and convert to PNG

```bash
alias crop_pdf_in_current_folder='mkdir -p cropped; for f in ./*.pdf; do pdf-crop-margins -o "cropped/$f" -p 0 -a -6 $f; done'
alias pdf_to_png_current_folder='mkdir -p png; for f in ./*.pdf; do pdftoppm -r 300 -png $f > "png/${f%.*}.png"; done'
```