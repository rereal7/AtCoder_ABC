<?php
//読取


//計算


//結果


//関数
function int($N=1){
	return fscanf(STDIN, str_repeat("%d", $N));
}
function str($N=1){
	return fscanf(STDIN, str_repeat("%s", $N));
}
function float($N=1){
	return fscanf(STDIN, str_repeat("%f", $N));
}

function zaatsu($array){
	$a = array_flip(array_flip($array));
	sort($a);
	$b = array_flip($a);
	foreach($array as $key => $value){
		$array[$key] = $b[$value];
	}
	return $array;
}

