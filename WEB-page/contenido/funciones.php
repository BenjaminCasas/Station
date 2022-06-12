<?php
// Lee el instrumento seleccionado
if(isset($_GET['insSel'])){ $insSel = $_GET['insSel']; } else { $insSel ='0'; }

// Variable de declaración en segundos
$ActualizarDespuesDe = 60;

// Funcion para listar ficheros en un directorio
function getFiles($dir){
    $files = array();
    // Leemos el directorio ordenado ascendentemente
    $tmp = scandir($dir);
    // Recorremos los ficheros del directorio
    foreach ($tmp as $file){
        // Comprobamos que sea un fichero y no un subdirectorio
        if (is_file($dir.'/'.$file)){
            $files[] = $file;
        }
    }
    return $files;
}

// Funcion para calcular tamaño
function dataSize($Bytes){
	$Type    = array("", "kilo", "mega", "G", "tera");
	$counter = 0;
	while($Bytes>=1024){
		$Bytes/=1024;
		$counter++;
	}
	return("".floor($Bytes)." ".$Type[$counter]."Bytes");
}

// Envíe un encabezado Refresh al navegador preferido.
header('Refresh: '.$ActualizarDespuesDe);

// Fecha actual
$fecha_actual = date_create(date('Y-m-d H:i:s'));
$dia  = date("d");
$mes  = date("m");
$anyo = date("Y");
//echo 'La fecha actual es: '.date_format($fecha_actual,"Y/m/d H:i:s").'<br>';

// Obtiene la URL actual
//$url = 'http://'.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
$url = 'http://'.$_SERVER['HTTP_HOST'];

// Carga el fichero info.txt
$datos     = file('../scripts/info.txt');
$station   = substr($datos[0],strpos($datos[0],'"')+1);
$fin       = strpos($station ,'"');
$station   = substr($datos[0],strpos($datos[0],'"')+1,$fin);

$dir_home  = substr($datos[1],strpos($datos[1],'"')+1);
$fin       = strpos($dir_home ,'"');
$dir_home  = substr($datos[1],strpos($datos[1],'"')+1,$fin);

$n_instrum = substr($datos[11],strpos($datos[11],'"')+1);
$fin       = strpos($n_instrum  ,'"');
$n_instrum = substr($datos[11],strpos($datos[11],'"')+1,$fin);


for ($n = 0; $n < $n_instrum; $n++) {
    $instrumento[$n]     = substr($datos[13+10*$n],strpos($datos[13+10*$n],'"')+1);
    $fin                 = strpos($instrumento[$n] ,'"');
    $instrumento[$n]     = substr($datos[13+10*$n],strpos($datos[13+10*$n],'"')+1,$fin);
    $instrumento_typ[$n] = substr($datos[14+10*$n],strpos($datos[14+10*$n],'"')+1);
    $fin                 = strpos($instrumento_typ[$n] ,'"');
    $instrumento_typ[$n] = substr($datos[14+10*$n],strpos($datos[14+10*$n],'"')+1,$fin);    
    $instrumento_id[$n]  = substr($datos[15+10*$n],strpos($datos[15+10*$n],'"')+1);
    $fin                 = strpos($instrumento_id[$n] ,'"');
    $instrumento_id[$n]  = substr($datos[15+10*$n],strpos($datos[15+10*$n],'"')+1,$fin);
    $parametro_1[$n]     = substr($datos[16+10*$n],strpos($datos[16+10*$n],'"')+1);
    $fin                 = strpos($parametro_1[$n] ,'"');
    $parametro_1[$n]     = substr($datos[16+10*$n],strpos($datos[16+10*$n],'"')+1,$fin);
    $parametro_2[$n]     = substr($datos[17+10*$n],strpos($datos[17+10*$n],'"')+1);
    $fin                 = strpos($parametro_2[$n] ,'"');
    $parametro_2[$n]     = substr($datos[17+10*$n],strpos($datos[17+10*$n],'"')+1,$fin);
    $parametro_3[$n]     = substr($datos[18+10*$n],strpos($datos[18+10*$n],'"')+1);
    $fin                 = strpos($parametro_3[$n] ,'"');
    $parametro_3[$n]     = substr($datos[18+10*$n],strpos($datos[18+10*$n],'"')+1,$fin);
    $parametro_4[$n]     = substr($datos[19+10*$n],strpos($datos[19+10*$n],'"')+1);
    $fin                 = strpos($parametro_4[$n] ,'"');
    $parametro_4[$n]     = substr($datos[19+10*$n],strpos($datos[19+10*$n],'"')+1,$fin);
}


// Carga el ultimo test de velocidad
$spe = '../scripts/logs/SPE-Station.log';
if (file_exists($spe)) {
    $spe    = file($spe);
    $A_Test_Date = $spe[0];
    $A_Test = substr($spe[5],strpos($spe[5],':')+1);
    $P_Test_Date = $spe[10];
    $P_Test = substr($spe[11],strpos($spe[11],':')+1);
    $U_Test_Date = $spe[12];
    $U_Test = substr($spe[17],strpos($spe[17],':')+1);
} else {
    $U_Test = "No hay datos disponibles";
    $A_Test = " ";
    $P_Test = " ";
}
if ($U_Test == ''){
    $U_Test = $P_Test;
    $U_Test_Date = $P_Test_Date;
}
if ($U_Test == ''){
    $U_Test = $A_Test;
    $U_Test_Date = $A_Test_Date;
}

// Lee el UpTime
$data   = shell_exec('uptime');
$pos_i  = strpos($data,'up ')+3;
$pos_f  = strpos($data,',');
$uptime = substr($data,$pos_i,$pos_f-$pos_i);
$pos_i  = strpos($data,'e: ')+3;
$pos_f  = strpos($data,',',$pos_i);
$load   = substr($data,$pos_i,$pos_f-$pos_i);
$data   = shell_exec('curl "https://api.ipify.org?format=json"');
$pos_i  = strpos($data,'":"')+3;
$pos_f  = strpos($data,'"}');
$pub_ip = substr($data,$pos_i,$pos_f-$pos_i);
$dsk_sz = dataSize(disk_total_space("/"));
$dsk_pr = round(disk_free_space("/")*100/disk_total_space("/"));

// Lee la temperatura del procesador
$thermal = '/sys/class/thermal/thermal_zone0/temp';
if (file_exists($thermal)) {
    $fichero  = file('/sys/class/thermal/thermal_zone0/temp');
    $CPU_Temp = round($fichero[0]/1000,1);
} else {
    $CPU_Temp = '-';
}

// Carga los datos de la ultima intervencion
$datos           = file('DATOS/scripts/logs/MTO-Station.log');
$mto_fecha       = substr($datos[0],strpos($datos[0],'"')+1,-2);
$mto_operador    = substr($datos[1],strpos($datos[1],'"')+1,-2);
$mto_descripcion = substr($datos[2],strpos($datos[2],'"')+1,-2);

//Carga versiones
$fichero       = file('DATOS/scripts/pythonFunciones.py');
$VER_funciones = substr($fichero[5],strpos($fichero[5],"'")+1);
$fin           = strpos($VER_funciones ," ");
$VER_funciones = substr($fichero[5],strpos($fichero[5],"'")+1,$fin);
//echo 'VERSION= '.$VER_funciones.'<br>';

$fichero     = file('DATOS/scripts/pythonCaptura.py');
$VER_captura = substr($fichero[6],strpos($fichero[6],"'")+1);
$fin         = strpos($VER_captura ," ");
$VER_captura = substr($fichero[6],strpos($fichero[6],"'")+1,$fin);
//echo 'VERSION= '.$VER_funciones.'<br>';

$fichero   = file('DATOS/scripts/speedTest.sh');
$VER_speed = substr($fichero[0],strpos($fichero[0],"'")+1);
$fin       = strpos($VER_speed ," ");
$VER_speed = substr($fichero[0],strpos($fichero[0],"'")+1,$fin);
//echo 'VERSION= '.$VER_speed .'<br>';

$fichero    = file('DATOS/scripts/pythonEnvioDAT.py');
$VER_envioD = substr($fichero[6],strpos($fichero[6],"'")+1);
$fin        = strpos($VER_envioD ," ");
$VER_envioD = substr($fichero[6],strpos($fichero[6],"'")+1,$fin);
//echo 'VERSION= '.$VER_speed .'<br>';



//Calcula Semaforos y ultimos datos recibidos
for ($n = 0; $n < $n_instrum; $n++) { 
    // Comprueba si el instrumento es una camara
    if (substr($instrumento[$n],0,3) == 'CAM'){
        echo 'Este instrumento es una cámara';
        //Opción 1: El instrumento es una camara
        $DIR    = 'DATOS/'.$instrumento[$n].'/rawInput';
        $CAM_ID = scandir($DIR)[2];
        $DIR    = $DIR.'/'.$CAM_ID.'/snap/';
        $IMG_LS = getFiles($DIR);
        $IMG_SZ = count($IMG_LS);
        if ($IMG_SZ > 0) {
            $semaforo[$n] = 'V';
            $semaforo_color[$n] ='#000';
            $IMG_ULT = filectime($DIR.$IMG_LS[$IMG_SZ]);
        }else{
            $semaforo[$n] = 'N';
            $semaforo_color='#FF6600';
            $DIR    = 'DATOS/'.$instrumento[$n].'/rawArchive';
            $IMG_LS = getFiles($DIR);
            $IMG_SZ = count($IMG_LS);
            $IMG_ULT = filectime($DIR.$IMG_LS[$IMG_SZ]);
            $fecha_ult = date_create(date("Y-m-d H:i:s" ,$IMG_ULT));
            $interval[$n] = date_diff($fecha_ult, $fecha_actual);
            if ($interval->format('%I') > 15){ $semaforo[$n] = 'R'; $semaforo_color='#FF0000';}
        }
    } else {
        //Opción 2: El instrumento NO es una camara
        $file = $dir_home.'Station/'.$instrumento[$n].'/rawInput/'.$anyo.$mes.$dia.'.ail';
        if (file_exists($file)) {
            $datos              = file($file);
            $fecha_ult_dato[$n] = date_create (substr($ult_dato[$n],0,19));
            $interval[$n]       = date_diff($fecha_ult_dato[$n], $fecha_actual);          
            $semaforo[$n]       = 'V'; $semaforo_color[$n]='#000';
            if ($interval[$n]->format('%I') > 20){ $semaforo[$n] = 'N'; $semaforo_color[$n]='#FF6600';}
            if ($interval[$n]->format('%H') >= 1){ $semaforo[$n] = 'R'; $semaforo_color[$n]='#FF0000';}
            if ($interval[$n]->format('%d') >= 1){ $semaforo[$n] = 'R'; $semaforo_color[$n]='#FF0000';}
        } else {
            $semaforo[$n] = 'R';
            $interval[$n] = '-999';
        }   
    }    
}
?>
