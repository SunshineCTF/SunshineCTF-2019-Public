<?php
//include("config.php");
//session_start();

class MyDB extends SQLite3 {
    function __construct() {
        $this->open('../db.sqlite', SQLITE3_OPEN_READONLY);
    }
}
$db = new MyDB();

if($_SERVER["REQUEST_METHOD"] == "POST") {
    // username and password sent from form
    
    
    $myusername = $_POST['username'];
    $mypassword = $_POST['password'];
    
    $sql = "SELECT * FROM users WHERE username = '$myusername' and password = '$mypassword'";
    $result = $db->query($sql);
    $row = $result->fetchArray(SQLITE3_ASSOC);
    
    // If result matched $myusername and $mypassword, table row must be 1 row
    
    if($row) {
        $page = file_get_contents("../stats.html");
        $page = str_replace("XXAVATARXX", $row["avatar"], $page);
        $page = str_replace("XXUSERNAMEXX", $row["username"], $page);
        $page = str_replace("XXNAMEXX", $row["name"], $page);
        $page = str_replace("XXTITLEXX", $row["title"], $page);
        $page = str_replace("XXAGEXX", $row["age"], $page);
        $page = str_replace("XXFLAGXX", $row["flag"], $page);
        echo $page;
    } else {
        header("Debug: ".$sql);
        echo 'Your Login Name or Password is invalid <a href="/index.html">Try again</a>';
    }
}
?>
