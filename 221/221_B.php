<?php
$s = istr();
$t = istr();

if ($s == $t){
	echo 'Yes';
	exit;
}

$ans = 'No';
for($i=0; $i<strlen($s)-1; $i++){
	$S = str_split($s);
	$tmp = $S[$i];
	$S[$i] = $S[$i+1];
	$S[$i+1] = $tmp;
	if($t == implode('', $S)){
		$ans = 'Yes';
		break;
	}
}
echo $ans;



//関数
function istr():string{
	return trim(fgets(STDIN));
}
function istrs():array{
	return explode(" ", trim(fgets(STDIN)));
}
function iint():int{
	return trim(fgets(STDIN));
}
function iints():array{ 
	return array_map('intval', explode(" ", trim(fgets(STDIN))));
}