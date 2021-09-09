<?php

//読取
[$s, $k] = explode(" ", trim(fgets(STDIN)));

//計算
$s_split = str_split($s);
sort($s_split);
// var_dump($s_split);
$a = pat($s_split);
$ans = array_values(array_unique($a));
// var_dump($ans);

//結果
echo $ans[$k+1];

//参照
//https://www.softel.co.jp/blogs/tech/archives/2263
//関数
function pat($a, $s = '')
{
  $r = array();
  if (count($a) && is_array($a)) {
    //第1引数に文字の配列を渡されたらループして処理
    foreach ($a as $k => $v) {
      //文字の配列から1文字もらってこちらにくっつけて
      $_s = $s . $v;
      //もらった1文字を除いた文字の配列を作って
      $_a = $a;
      unset($_a[$k]);
      //再帰呼び出し
      $_r = pat($_a, $_s);
      //返り値にする変数に結果を追加
      $r = array_merge($r, $_r);
    }
  } else {
    //第1引数が空っぽの配列だったら、再帰呼び出しはここでストップ
    //返り値はこれだけ
    $r[] = $s;
  }
  return $r;
}