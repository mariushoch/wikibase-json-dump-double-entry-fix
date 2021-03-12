#!/bin/bash

set -e

md5sumGood="$(zcat test_data/wikidata-20210308-all_first2500.json.gz | md5sum)"

set -x

[ "$(zcat test_data/wikidata-20210308-all_first2500.json.gz | python double-entry-fix.py /dev/stdin /dev/stdout | md5sum)" == "$md5sumGood" ]
[ "$(zcat test_data/wikidata-20210308-all_first2500_broken.json.gz | python double-entry-fix.py /dev/stdin /dev/stdout | md5sum)" == "$md5sumGood" ]
[ "$(python double-entry-fix.py test_data/more_than_one_possible_split_point_per_line.json /dev/stdout)" == "$(cat test_data/more_than_one_possible_split_point_per_line_fixed.json)" ]

if zcat test_data/wikidata-20210308-all_first2500_broken_beyond_repair.json.gz | python double-entry-fix.py /dev/stdin /dev/null 2>/dev/null; then
	echo "Fixing test_data/wikidata-20210308-all_first2500_broken_beyond_repair.json.gz should fail!"
	exit 1
fi

echo "Success"
