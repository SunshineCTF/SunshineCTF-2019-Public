<?php

$whitelist = array(
    '127.0.0.1',
    '::1'
);
// if this page is accessed from the web server, the flag is returned
// flag is in env variable to avoid people using XXE to read the flag
// Grant only for genuine server-internal requests: a loopback source AND one
// that did NOT come through the public edge proxy (which stamps X-From-Edge).
// The loopback check alone already separates the intended internal SSRF
// (127.0.0.1) from external traffic (which arrives from the container gateway);
// the marker is a second, deployment-independent guard in case the app is ever
// fronted so that external traffic appears to come from localhost.
if(in_array($_SERVER['REMOTE_ADDR'], $whitelist) && !isset($_SERVER['HTTP_X_FROM_EDGE'])){
	echo $_ENV["FLAG"];
	return;
}
// make sure the input parameter exists
if (empty($_GET["input"])) {
	echo "Please include the 'input' get parameter with your request, Brother";
	return;
}

// get input
$xmlData = base64_decode($_GET["input"]);
// parse xml
$xml=simplexml_load_string($xmlData, null, LIBXML_NOENT) or die("Error parsing XML: "."\n".$xmlData);
$firstName = $xml->firstName;
$lastName = $xml->lastName;
// generate name
$nouns = array("Killer", "Savage", "Stallion", "Coder", "Hacker", "Slasher", "Crusher", "Barbarian", "Ferocious", "Fierce", "Vicious", "Hunter", "Brute", "Tactician", "Expert");
$noun = $nouns[array_rand($nouns)];
$generatedName = $firstName.' "The '.$noun.'" '.$lastName;

// return html for the results page
echo <<<EOT
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Wrestler Name Generator</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
  <h1>Your Wrestler Name Is:</h1>
  <h2>$generatedName</h2> 
<!--hacker name functionality coming soon!-->
<!--if you're trying to test the hacker name functionality, make sure you're accessing this page from the web server-->
<!--<h2>Your Hacker Name Is: REDACTED</h2>-->
  <a href="/">Go Back</a> 
</div>
</body>
</html>
EOT;
?>
