<?php
$code = $_REQUEST['code'];
$nom =$_REQUEST['nom'];
$file="num_dep.txt";
$str=$code." ".$nom;
file_put_contents($file, $str);
echo $str




#echo "file:".$file."<br>";
#echo "cmd:".$command."<br>";
#echo $return_var."<br>";

?>