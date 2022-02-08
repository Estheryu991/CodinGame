n=gets.to_i
s=gets.tr(',.','').upcase.split
o=s.flat_map{w=[?_*~-n]*2*_1
(0..w.size-n).map{|i|w[i...i+n]}}
$><<o.uniq.sort*' '
