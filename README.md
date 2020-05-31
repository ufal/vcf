# vcf
Convertor from wiki table of contacts to vCard for import into phones and such

Usage:
1. Copy paste the wiki source of the contact list into a file.
It should contain lines which look like something this:

`| Rudolf Rosa   | ÚFAL      | 123      | 1234            | 987 654 321     | 123 456 789  | rosa |`

2. Give the file to standard input of the script and receive a VCF file at the standard output:

`python3 vcf.py < contacts > contacts.vcf`
