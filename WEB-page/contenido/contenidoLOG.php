<div id="contenedor_1_dcha">
    <div id="contenido">
        <h2>Registro de eventos</h2>
        <div class="ult">(Muestra los últimos diez eventos registrados)</div>
        <div class="instrumento">
            <div class="caja-datos">
                <p>
                    <?php $log = 'DATOS/scripts/logs/LOG-Station.log';
                    if (file_exists($log)) {
                        $log = file($log);
                        for ($n = 1; $n < 11; $n++) {
                            echo $log[count($log)-$n],'<br>' ;
                        }
                    } else {
                        echo "El fichero $log no existe";
                    } ?>
                </p>
            </div>
            <div class="instrument-info">
                <br><div class="fichero-datos">[<a href="DATOS/scripts/logs/LOG-Station.log">LOG Completo</a>]</div>
            </div>
        </div>
        <h2>Registro de errores</h2>
        <div class="ult">(Muestra los últimos cinco eventos registrados)</div>
        <div class="instrumento">
            <div class="caja-datos">
                <p>
                    <?php $log = 'DATOS/scripts/logs/ERROR-Station.log';
                    if (file_exists($log)) {
                        $log = file($log);
                        for ($n = 1; $n < 11; $n++) {
                            echo $log[count($log)-$n],'<br>' ;
                        }
                    } else {
                        echo "El fichero $log no existe";
                    } ?>
                </p>
            </div>
            <div class="instrument-info">
                <br>
                <div class="fichero-datos">[<a href="DATOS/scripts/logs/ERROR-Station.log">LOG Completo</a>]</div>
            </div>
        </div>
    </div>
</div>