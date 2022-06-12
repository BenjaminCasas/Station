<div id="contenedor_1_dcha">
    <div id="contenido">
        <h2>
            <img class="semaforo" src="imagenes/semaforo<?php echo $semaforo[$insSel];?>.png">
            <?php echo $instrumento[$insSel];?>
        </h2>
        <div class="instrumento">
            <?php if ($interval[$insSel] == -999){?>
                <div class="ult">No puedo calcular cuando fue el último dato registrado</div>
                <div id="contenedor_SAI"></div>
            <?php } else { ?>
                <div class="ult">Último dato registrado hace <?php echo'<font color="',$semaforo_color[$insSel],'">', $interval[$insSel]->format('%d días, %H horas, %i minutos, %s segundos'),'</font>'?></div>
                <div class="caja-datos">
                    <?php for ($m = 1; $m < 16; $m++) {
                        echo $datos[count($datos)-$m],'<br>';
                    }?>
                </div>
                <?php if (file_exists('../scripts/figuras/'.$instrumento_id[$insSel].'.png')) { ?>
                    <hr>
                    <div>
                        <img class="figura" src="DATOS/scripts/figuras/<?php echo $instrumento_id[$insSel];?>.png">
                    </div>
                <?php } ?>
                <hr>
                <div class="instrumento-info"> 
                    Instrumento ID: <b><?php echo $instrumento_id[$insSel];?></b> | 
                    Tipo de instrumento: <b><?php echo $instrumento_typ[$insSel];?></b> | 
                    <?php if (strpos($instrumento_id[$insSel],'DTH') == TRUE || strpos($instrumento_id[$insSel],'DS18') == TRUE){
                        echo 'Intervalo de muestreo: <b>',$parametro_1[$insSel],'s</b>';
                    } else {
                        echo 'Puerto: <b>',$parametro_1[$insSel],'</b>';
                    } ?>
                </div>
                <div class="fichero-datos">
                    [<a href="<?php echo 'DATOS/'.$instrumento[$insSel].'/rawInput/'.$anyo.$mes.$dia.'.ail';?>">FICHERO DE DATOS</a>]
                </div>
            <?php } ?>
        </div>
    </div>
</div>    