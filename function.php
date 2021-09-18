<?php

//座標圧縮
function zaatsu($array){
	$a = array_flip(array_flip($array));
	sort($a);
	$b = array_flip($a);
	foreach($array as $key => $value){
		$array[$key] = $b[$value];
	}
	return $array;
}