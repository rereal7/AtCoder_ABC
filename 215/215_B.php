<?php

//正整数 N が与えられるので、 2^k≤N となる最大の整数 k を求めてください。
//読取
$n = (int)trim(fgets(STDIN));
$k = 0;

//計算
$num = 0;
while($num<$n){
	$k++;
	$num = pow(2, $k);
	if($num>$n){
		$k--;
		break;
	}
}

//結果
echo $k;