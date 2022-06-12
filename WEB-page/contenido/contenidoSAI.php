<div id="contenedor_1_dcha">
    <div id="contenido">
        <h2>Estado del SAI</h2>
        <div id="contenedor_SAI">
            <center><object type="text/html" data="<?php echo $url; ?>/cgi-bin/apcupsd/multimon.cgi" width="100%" height="700px"></object></center>
            <?php $log = $dir_home.'S/scripts/logs/SAI-Station.log';
            if (file_exists($log)) {?>
                <div class="fichero-datos">[<a href="DATOS/scripts/logs/SAI-Station.log">LOG Completo</a>]</div>
            <?php } ?>
        </div>
        <br>
    </div>
</div>