<?php


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

// $input = trim(fgets(STDIN));
// $inputs = explode(" ", trim(fgets(STDIN)));
// $inputs = array_map('intval', explode(" ", trim(fgets(STDIN))));