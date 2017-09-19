#!/usr/bin/php 
<?php
/**
 * BBEdit SQL format text filter
 * For a file with SQL query, send page contents to SQL format API and repopulate file with results
 */
$str = file_get_contents('php://stdin');
$str = str_replace(array("\n", "\r", "\t"), ' ', $str);
$str = preg_replace('~  +~', ' ', $str);
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'http://www.gudusoft.com/format.php');
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, 'rqst_input_sql=' . urlencode($str) );
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/x-www-form-urlencoded'));
$result = curl_exec($ch);
curl_close($ch);
if($result and $result = json_decode($result) and !empty($result->rspn_formatted_sql))//expects: {  "rspn_http_status" : 200,  "rspn_capacity" : 0,  "rspn_db_vendor" : "generic",  "rspn_output_fmt" : "",  "rspn_parse_sql_status" : 0,  "rspn_parse_sql_message" : "success",  "rspn_formatted_sql" : "SELECT *\nFROM   DUAL \n"}
{
	$str = str_replace('\\t', "\t", $result->rspn_formatted_sql);
	$str = str_replace('\\r', "\r", $str);
	$str = str_replace('\\n', "\n", $str);
}
echo $str;
exit(0);