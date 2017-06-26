<?
  require_once 'dbconnect.php';
  extract($_POST);
  if($condition=="default"){
    $query = "delete from alarm where userid='".$_SESSION['id']."'";
    $result = mysqli_query($conn, $query);
  }
  else if($condition=="add"){
    for ($i=0; $i < count($data); $i+=4) {
      $query = "insert into alarm(`alarmid`,`userid`,`name`,`param`,`value`,`target`) values('".$_SESSION['id'].$idx."','".$_SESSION['id']."','".$data[$i]."','".$data[$i+1]."','".$data[$i+2]."','".$data[$i+3]."')";
      $result = mysqli_query($conn, $query);
    }
  }
  else if($condition=="delete"){
    $query = "delete from alarm where alarmid='".$target."'";
    $result = mysqli_query($conn, $query);
  }
  else if($condition=="get"){
    $return = array();
    $query = "select * from alarm where userid='".$_SESSION['id']."'";
    $result = mysqli_query($conn, $query);
    while($row = mysqli_fetch_array($result)) array_push($return,$row[1],$row[3],$row[4],$row[5],$row[6]);
    echo json_encode($return);
  }
?>
