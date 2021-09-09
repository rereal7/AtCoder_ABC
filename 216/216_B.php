<?php
//読取
$n =(int) trim(fgets(STDIN));
$st = [];
for($i=0; $i<$n; $i++){
	$st[] = str_replace(' ','.', trim(fgets(STDIN)));
}

//計算
$result = 'No';
$check_array = array_count_values($st);
foreach($check_array as $check_int){
	if($check_int > 1){
		$result = 'Yes';
		break;
	}
}

//結果
echo $result;