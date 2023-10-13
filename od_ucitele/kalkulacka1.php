<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>


<?php
    $a=$_POST["a"]??null;
    $b=$_POST["b"]??null;
    $mod=$_POST["mod"]??null;
   
    echo "a: ".$a."<br>";
    echo "b: ".$b."<br>";
    echo "mod: ".$mod."<br>";

    if($a==null or $b==null or $mod==null){
        echo "nelze pocitat parametr nebyl zadan<br><br>";
    }else{
        $priklad="";
        switch ($mod) {
            case 'scitani':
                $priklad="$a+$b=".$a+$b;
                break;
            case 'odcitani':
                $priklad="$a-$b=".$a-$b;
                break;
            case 'nasobeni':
                $priklad="$a*$b=".$a*$b;
                break;
            case 'deleni':
                if($b==0){
                    $priklad="$a/$b="."Nelze delit nulou";
                }else{
                    $priklad="$a/$b=".$a/$b;
                }
                break;
            default:
                echo "Neznama operace ".$mod;
            
        }
        echo $priklad;

    }



?>
<hr>
<form action="form.php" method="post">
        a: <input type="number" name="a" value="<?php echo $a;?>"><br>
        b: <input type="number" name="b" value="<?php echo $b;?>"><br>
        mod:<br>
        <input type="radio" name="mod" value="scitani" <?php echo $mod=="scitani"?"checked":""?>> scitani<br>
        <input type="radio" name="mod" value="odcitani" <?php echo $mod=="odcitani"?"checked":""?>> odcitani<br>
        <input type="radio" name="mod" value="nasobeni" <?php echo $mod=="nasobeni"?"checked":""?>> nasobeni<br>
        <input type="radio" name="mod" value="deleni" <?php echo $mod=="deleni"?"checked":""?>> deleni<br>
        <br>
        <input type="submit" value="odeslat">
</form>


</body>
</html>
