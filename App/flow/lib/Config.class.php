<?php
/**
 * Clase para Configurar el cliente
 * @Filename: Config.class.php
 * @version: 2.0
 * @Author: flow.cl
 * @Email: csepulveda@tuxpan.com
 * @Date: 28-04-2017 11:32
 * @Last Modified by: Carlos Sepulveda
 * @Last Modified time: 28-04-2017 11:32
 */
 
 $COMMERCE_CONFIG = array(
 	"APIKEY" => "4258F333-8007-4EA4-95F3-98CCD29C4LF3", // Registre aquí su apiKey
 	"SECRETKEY" => "b0726605aaecc68bbab78079f70712490fe2a65f", // Registre aquí su secretKey
 	"APIURL" => "https://www.flow.cl/api", // Producción EndPoint o Sandbox EndPoint
 	"BASEURL" => "http://127.0.0.1:8000/apiFlow" //Registre aquí la URL base en su página donde instalará el cliente
 );
 
 class Config {
 	
	static function get($name) {
		global $COMMERCE_CONFIG;
		if(!isset($COMMERCE_CONFIG[$name])) {
			throw new Exception("The configuration element thas not exist", 1);
		}
		return $COMMERCE_CONFIG[$name];
	}
 }