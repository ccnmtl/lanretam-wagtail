jQuery(document).ready(function(){
    jQuery('.map-checker input[type="checkbox"]').click(function(){
        var mapValue = jQuery(this).attr("data-target");
        var mapLayer = "#map-" + mapValue;
        var mapLegend = "#legend-" + mapValue;
        jQuery(mapLayer).toggle();
        jQuery(mapLegend).toggle();
    });
});
