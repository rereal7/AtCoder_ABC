<?php
$X = array_map('intval', str_split(trim(fgets(STDIN))));
$ans = 'Strong';

$array = array_count_values($X);
if(count($array) === 1){
	$ans = 'Weak';
}else{
	for($i=0; $i<3; $i++){
		$target = $X[$i];
		$next_target = $X[$i+1];
		if(($target+1)%10 !== $next_target){
			break;
		}
	}
	if($i === 3){
		$ans = 'Weak';
	}
	// $count = 0;
	// for($i=0; $i<3; $i++){
	// 	$target = $X[$i];
	// 	$next_target = $X[$i+1];
	// 	if($target === 9){
	// 		if($next_target === 0){
	// 			$count++;
	// 		}
	// 	}else{
	// 		if($next_target-$target === 1){
	// 			$count++;
	// 		}
	// 	}
	// }
	// if($count === 3){
	// 	$ans = 'Weak';
	// }
}

echo $ans;
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