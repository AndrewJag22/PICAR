<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>Home_Smarter</title>
</head>
<body>
	<form>
       	Light Controllings:
        <form method="get" action="gpio.php">
                <input type="submit" value="ON" name="on">
                <input type="submit" value="OFF" name="off">
       </form>
	<form>
	Door Controllings:
        <form method="get" action="gpio.php">
                <input type="submit" value="OPEN" name="open">
                <input type="submit" value="CLOSE" name="close">

        </form>
        <?php
        $setmode17 = shell_exec("/usr/local/bin/gpio -g mode 17 out");
        if(isset($_GET['on'])){
                $gpio_on = shell_exec("/usr/local/bin/gpio -g write 17 1");
                echo "Light is on";
        }
        else if(isset($_GET['off'])){
                $gpio_off = shell_exec("/usr/local/bin/gpio -g write 17 0");
                echo "Light is off";
        }
        $setmode4 = shell_exec("/usr/local/bin/gpio -g mode 4 out");
        if(isset($_GET['open'])){
                $gpio_on = shell_exec("/usr/local/bin/gpio -g write 4 1");
                echo "Door is open";
        }
        else if(isset($_GET['close'])){
                $gpio_off = shell_exec("/usr/local/bin/gpio -g write 4 0");
                echo "Door is closed";
        }

        ?>
        </body>

</html>
