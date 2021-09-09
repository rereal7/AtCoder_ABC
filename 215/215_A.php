<?php

//読取
$s = trim(fgets(STDIN));
$t = 'Hello,World!';

//計算
$ans = 'WA';
if($s === $t){
	$ans = 'AC';
}

//結果
echo $ans;