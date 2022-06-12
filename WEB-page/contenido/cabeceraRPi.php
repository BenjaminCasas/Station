<!-- DATOS RPI -->
<span id="datos-rpi">
    <i class="fa fa-clock-o" aria-hidden="true"></i> Uptime:<b><?php echo ' '.$uptime;?></b>
    &nbsp;&nbsp;&nbsp;
    <i class="fa fa-hdd-o"></i>
    <?php echo ' <b>'.$dsk_sz.'</b>, '; echo 'Free: ';
    if ($dsk_pr < 30){ echo '<font color=red><b>'.$dsk_pr.'%</b></font>';
    } else { echo '<b>'.$dsk_pr.'%</b>';} 
    ?>
    &nbsp;&nbsp;&nbsp;
    <i class="fa fa-bar-chart-o"></i>
    Load average:
    <?php if ($load > 2){ echo '<font color=red><b>'.$load.'%</b></font>';
    } else {echo '<b>'.$load.'%</b>';} ?>
     &nbsp;&nbsp;&nbsp;
    <i class="fa fa-thermometer" aria-hidden="true"></i>
    CPU Temp.:
     <?php if ($CPU_Temp > 70){ echo '<font color=red><b>'.$CPU_Temp.'ºC</b></font>';
     } else {echo '<b>'.$CPU_Temp.'ºC</b>';} ?>
    &nbsp;&nbsp;&nbsp;
    <i class="fa fa-sitemap"></i> Ip:<b><?php echo ' '.$pub_ip; ?></b>
</span>
<!-- END: DATOS RPI -->