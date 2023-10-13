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

    $checkedscitani="";
    /*
        echo "a: ".$_POST["a"]."<br>";
        echo "b: ".$_POST["b"]."<br>";
        echo "mod: ".$_POST["mod"]."<br>";
    */
    echo "a: ".$a."<br>";
    echo "b: ".$b."<br>";
    echo "mod: ".$mod."<br>";

    if($a==null or $b==null or $mod==null){
        echo "nelze pocitat parametr nebyl zadan<br><br>";
    }else{
        $priklad="";
        
        switch ($mod) {
            case 'scitani':
                $checkedscitani="checked";
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
    $form='
    <form action="form2.php" method="post">
            a: <input type="number" name="a" value="#a#"><br>
            b: <input type="number" name="b" value="#b#"><br>
            mod:<br>
            <input type="radio" name="mod" value="scitani" #checkedscitani# > scitani<br>
            <input type="radio" name="mod" value="odcitani" > odcitani<br>
            <input type="radio" name="mod" value="nasobeni" > nasobeni<br>
            <input type="radio" name="mod" value="deleni" > deleni<br>
            <br>
            <input type="submit" value="odeslat">
    </form>
    ';

    $form=str_replace("#a#", $a, $form);
    $form=str_replace("#b#", $b, $form);
    $form=str_replace("#checkedscitani#", $checkedscitani, $form);
    echo $form;
    


?>
<hr>



</body>
</html>
