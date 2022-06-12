<!DOCTYPE html>
<html lang="es">

<!-- CARGA DE FICHEROS DE INFORMACION -->
<?php
//PENDIENTE: Que hacer en caso de que no haya tres medidas de speedtest
// Carga los datos de la estacion
$version = 'V2.0 | May-2022'; // Nueva versión
//$version = 'V1.5 | Feb-2021'; // Adapto a dos instituciones y elección de SAI / SPE
//$version = 'V1.45 | May-2020'; // Corrijo un fallo en la version de captura y anyado la version del envioDatos.py
//$version = 'V1.44 | May-2020'; // Incluyo versiones de script en el pie de pagina
//$version = 'V1.43 | May-2020'; // Incluyo acceso al log de SpeedTest
//$version = 'V1.42 | May-2020'; // Incluyo accesos directos a los ficheros de logs 
//$version = 'V1.41 | May-2020'; // Incluyo en la cabecera el espacio en disco
//$version = 'V1.4  | Abr-2020'; // Inclusion de info del equipo en el pie
//$version = 'V1.3  | Abr-2020'; // Presentacion imagenes Web + inclusión DTH22 + refresco automatico

include 'contenido/funciones.php';

// SAI si SAI no
$SAI = 'S';
?>



<!-- HEAD --------  -------------------------------------------------------------------------- -->
    <head>
        <title><?php echo $station; ?></title>
        <meta charset="UTF-8">
        <meta name="Keywords"    content="socib, Balearic, Mallorca, mooring, buoy, data management, Oceanography, station">
        
        <!--load styles -->
        <link rel="stylesheet" href="estilo/estilo.css">
        <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">
        <link rel="shortcut icon" href="imagenes/logo_SOCIB.ico" />
        <!--END: load styles -->

        <!--scripts -->
        <script src="//widget.time.is/es.js"></script>
        <script>time_is_widget.init({UTC_za00:{template:"&nbsp;DATE<br>TIME UTC", date_format:"year-monthnum-daynum"}});</script>
        <!-- END: scripts -->    
    </head>
<!-- EMD: HEAD ------------------------------------------------------------------------------- -->

<!-- BODY ------  ---------------------------------------------------------------------------- -->
    <body>
<!-- CABECERA -------------------------------------------------------------------------------- -->
        <?php include 'contenido/cabecera.php'; ?>
        <?php include 'contenido/cabeceraRPi.php'; ?>
<!-- END: CABECERA --------------------------------------------------------------------------- -->

        <div id="contenedor_1">
<!-- MENU IZDA ------  ----------------------------------------------------------------------- -->
            <?php include 'contenido/menu.php'; ?>
<!-- END:MENU IZDA ------  ------------------------------------------------------------------- -->

<!-- CONTENIDO ------  ----------------------------------------------------------------------- -->
            <?php if ($insSel == 999) { 
                include 'contenido/contenidoLOG.php';
            } elseif ($insSel == 888) { 
                include 'contenido/contenidoSAI.php';
            } else {
                include 'contenido/contenidoDAT.php';
            } ?>    
<!-- END: CONTENIDO ------  ------------------------------------------------------------------- -->      
        </div>
        
<!-- INI: Pie -->
        <?php include 'contenido/pie.php'; ?>
<!-- FIN: Pie -->
    </body>
</html>              
