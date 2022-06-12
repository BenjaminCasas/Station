<div id="contenedor_1_izda">
    <div id="update">
        Updated: <strong><?php echo date('Y-m-d H:i:s');?></strong>
    </div>
    <ul id="menu">
        <?php for ($n = 0; $n < $n_instrum; $n++) { 
            echo '<li>';    
            if ($insSel == $n) { 
                echo '<strong>',$instrumento[$n],'</strong> ';
                echo '<img class="semaforo" src="imagenes/semaforo',$semaforo[$n],'.png">';
            } else {
                echo'<a id="hv_menu" href="index.php?insSel=',$n,'">',$instrumento[$n],'</a> ';
                echo '<img class="semaforo" src="imagenes/semaforo',$semaforo[$n],'.png">';
            }
            echo '</li>';
        }?>
    </ul>
    <hr class="vlink_separator">  
    <ul id="menu"> 
        <?php if ($insSel == 999) { ?>
            <li><strong>Registros de eventos</strong></li>
        <?php } else { ?>
            <li><a id="hv_menu" href="index.php?insSel=999">Registro de eventos</a></li>
        <?php } ?>
        <?php if ($SAI == 'S'){ 
            if ($insSel == 888 ) { ?>
                <li><strong>Estado del SAI</strong></li>
            <?php } else { ?>
                <li><a id="hv_menu" href="index.php?insSel=888">Estado del SAI</a></li>
            <?php } ?>
        <?php } ?>
    </ul>
    <hr class="vlink_separator">
    <div id="speedtest">Speedtest</div>
    <?php if ($U_Test == 'No hay datos disponibles'){?>
        No hay datos de Speedtest
    <?php } else {?>
        <div id="speed_date">
            <?php echo $U_Test_Date; ?>
        </div>
        <img class="speedtest" src="<?php echo $U_Test; ?>"> 
    <?php } ?>
    <br>
    <?php if (file_exists('DATOS/WAN/rawInput/'.$anyo.$mes.'_Station.ail')) { ?>
        <div id="speed_file">
            [<a href="<?php echo 'DATOS/WAN/rawInput/'.$anyo.$mes.'_Station.ail'; ?>">FICHERO DE DATOS</a>]
        </div>
    <?php } ?>
</div>