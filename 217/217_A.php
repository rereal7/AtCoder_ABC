<?php
//読取
[$s, $t] = explode(" ", trim(fgets(STDIN)));

//計算
$ans = 'No';
$result = strnatcmp($s, $t);
if($result<0){
	$ans = 'Yes';
}

//結果
echo $ans;