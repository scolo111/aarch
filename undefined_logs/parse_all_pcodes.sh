egrep UNDEFI all_pcode.log | sort | uniq -c                   > all_pcode_patterns.log
egrep UNDEFI all_pcode.log | egrep -v "^if " | sort | uniq -c > all_pcode_patterns_without_if.log
egrep UNDEFI all_pcode.log | egrep -v "^if " | egrep -v "Have\w+\(\)" | sort | uniq -c > all_pcode_patterns_without_if_Have.log