<?php
$alp = array_flip(str_split(trim(fgets(STDIN))));
$N = (int) trim(fgets(STDIN));
$names = [];
for($i=0; $i<$N; $i++){
	$names[] = str_split(trim(fgets(STDIN)));
}

$names_sub = [];
for($i=0; $i<$N; $i++){
	$names_sub[] = implode($names[$i]);
}

for($i=0; $i<$N; $i++){
	$names[$i] = array_pad($names[$i], 10, 0);
	for($j=0; $j<10; $j++){
		if($names[$i][$j] != null){
			$names[$i][$j] = $alp[$names[$i][$j]];
		}
	}
}
// var_dump($names_sub);

$i=0;
foreach($names as $value) {
	$key = $names_sub[$i];
	$key_0[] = $value['0'];
	$key_1[] = $value['1'];
	$key_2[] = $value['2'];
	$key_3[] = $value['3'];
	$key_4[] = $value['4'];
	$key_5[] = $value['5'];
	$key_6[] = $value['6'];
	$key_7[] = $value['7'];
	$key_8[] = $value['8'];
	$key_9[] = $value['9'];
	$i++;
}

array_multisort(
	$key_0, SORT_ASC, SORT_NUMERIC,
	$key_1, SORT_ASC, SORT_NUMERIC, 
	$key_2, SORT_ASC, SORT_NUMERIC, 
	$key_3, SORT_ASC, SORT_NUMERIC, 
	$key_4, SORT_ASC, SORT_NUMERIC, 
	$key_5, SORT_ASC, SORT_NUMERIC, 
	$key_6, SORT_ASC, SORT_NUMERIC, 
	$key_7, SORT_ASC, SORT_NUMERIC, 
	$key_8, SORT_ASC, SORT_NUMERIC, 
	$key_9, SORT_ASC, SORT_NUMERIC, $names);

var_dump($names);
