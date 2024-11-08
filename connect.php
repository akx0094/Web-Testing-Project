<?php

// Retrieve form data
$name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
$email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
$message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);


    // Database connection
	$servername="localhost";
    $username="root";
    $password="";
    $dbname="testt";
	
	
    // Database connection
	
	
    $conn = mysqli_connect($servername,$username,$password,$dbname,3306);
	
	
    // Check connection
    if (!$conn){
    die("Sorry we failed to connect: ". mysqli_connect_error());
	}
else{
    echo "Connection was successful<br>";

}

// Variables to be inserted into the table

// Sql query to be executed
$sql = ("INSERT INTO `get_in_touch` (`name`,`email`,`message`) VALUES ('$name','$email','$message');");

$result = mysqli_query($conn, $sql);

// Add a new trip to the Trip table in the database
if($result){
    echo "The record has been inserted successfully successfully!<br>";
}
else{
    echo "The record was not inserted successfully because of this error ---> ". mysqli_error($conn);
}

?>
