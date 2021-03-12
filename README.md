# wikibase-json-dump-double-entry-fix
Fix Wikibase JSON dumps that (erroneously) have more than one entity on a line.

### Usage:
`double-entry-fix.py [-h] infile outfile`

Can also be used directly with the gzip-ed JSON dumps:

`zcat dump.json.gz | python double-entry-fix.py /dev/stdin /dev/stdout | gzip -c9 > fixed_dump.json.gz`
