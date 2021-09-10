<?php
/*
** 計算量を改善しないとTLEから抜け出せない
** すでに出ている素因数を保存しておいて、重複するものん関しては計算を省く処理をしたい
*/

/*
** input
*/
[$n, $m] = array_map('intval', explode(" ", trim(fgets(STDIN))));
$a = array_map('intval', explode(" ", trim(fgets(STDIN))));

/* 
** calc
*/
$numbers  = range(1, $m);
for($i=0; $i<$n; $i++){
	$P = pf($a[$i]);
	foreach($P as $p){
		$j = 1;
		while($p*$j <= $m){
			$numbers = array_diff($numbers, [$p*$j]);
			$j++;
		}
	}
}

/*
** output
*/
echo count($numbers)."\n";
foreach($numbers as $num){
	echo $num."\n";
}

/*
** function
*/
function pf($num) {
	$result = array();

	if ($num === 1) {
			return [1];
	}

	$init = 2;

	while ( $num !== 1 ) {
			$i = $init;
			while ($i < 0xFFFFFF) {
					if ($num % $i == 0) {
							$result[] = $i;
							$num /= $i;
							break;
					}
					$i++;
			}
			$init = $i;
	}
	return $result;
}