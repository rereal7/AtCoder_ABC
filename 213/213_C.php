<?php
//参考[https://atcoder.jp/contests/abc213/submissions/24904480]

[$H, $W, $N] = array_map('intval', explode(" ", trim(fgets(STDIN))));
for($i=0; $i<$N; $i++){
	[$A[], $B[]] = array_map('intval', explode(" ", trim(fgets(STDIN))));
}

$A = zaatsu($A);
$B = zaatsu($B);

for($i = 0; $i < $N; $i++){
	$ans[] = ($A[$i]+1)." ".($B[$i]+1);
}
echo implode("\n", $ans);

function zaatsu(array $array){
	$a = array_flip(array_flip($array));
	sort($a);
	$b = array_flip($a);
	foreach($array as $key => $value){
		$array[$key] = $b[$value];
	}
	return $array;
}