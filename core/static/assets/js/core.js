/**
 *
 */
let hexToRgba = function (hex, opacity) {
    let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    let rgb = result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;

    return 'rgba(' + rgb.r + ', ' + rgb.g + ', ' + rgb.b + ', ' + opacity + ')';
};

/**
 *
 */
$(document).ready(function () {
    /** Constant div card */
    const DIV_CARD = 'div.card';

    /** Initialize tooltips */
    $('[data-toggle="tooltip"]').tooltip();

    /** Initialize popovers */
    $('[data-toggle="popover"]').popover({
        html: true
    });

    /** Function for remove card */
    $('[data-toggle="card-remove"]').on('click', function (e) {
        let $card = $(this).closest(DIV_CARD);

        $card.remove();

        e.preventDefault();
        return false;
    });

    /** Function for collapse card */
    $('[data-toggle="card-collapse"]').on('click', function (e) {
        let $card = $(this).closest(DIV_CARD);

        $card.toggleClass('card-collapsed');

        e.preventDefault();
        return false;
    });

    /** Function for fullscreen card */
    $('[data-toggle="card-fullscreen"]').on('click', function (e) {
        let $card = $(this).closest(DIV_CARD);

        $card.toggleClass('card-fullscreen').removeClass('card-collapsed');

        e.preventDefault();
        return false;
    });

    /**  */
    if ($('[data-sparkline]').length) {
        let generateSparkline = function ($elem, data, params) {
            $elem.sparkline(data, {
                type: $elem.attr('data-sparkline-type'),
                height: '100%',
                barColor: params.color,
                lineColor: params.color,
                fillColor: 'transparent',
                spotColor: params.color,
                spotRadius: 0,
                lineWidth: 2,
                highlightColor: hexToRgba(params.color, .6),
                highlightLineColor: '#666',
                defaultPixelsPerValue: 5
            });
        };

        require(['sparkline'], function () {
            $('[data-sparkline]').each(function () {
                let $chart = $(this);

                generateSparkline($chart, JSON.parse($chart.attr('data-sparkline')), {
                    color: $chart.attr('data-sparkline-color')
                });
            });
        });
    }

    /**  */
    if ($('.chart-circle').length) {
        require(['circle-progress'], function () {
            $('.chart-circle').each(function () {
                let $this = $(this);

                $this.circleProgress({
                    fill: {
                        color: tabler.colors[$this.attr('data-color')] || tabler.colors.blue
                    },
                    size: $this.height(),
                    startAngle: -Math.PI / 4 * 2,
                    emptyFill: '#F4F4F4',
                    lineCap: 'round'
                });
            });
        });
    }
});


google.charts.load("current", {packages: ['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ["Element", "Density", {role: "style"}],
        ["Erkaklar", 2222, "#b87333"],
        ["Ayollar", 1900, "silver"],
        ["Yoshlar", 3000, "gold"],
        ["Kam Ta'minlanganlar", 1200, "color: #e5e4e2"],
        ["Noguronlar", 500, "#26bf40"],
        ["Ishsizlar", 1000, "#4dc488"],

    ]);

    var view = new google.visualization.DataView(data);
    view.setColumns([0, 1,
        {
            calc: "stringify",
            sourceColumn: 1,
            type: "string",
            role: "annotation"
        },
        2]);

    var options = {
        title: "Density of Precious Metals, in g/cm^3",
        width: 550,
        height: 330,
        bar: {groupWidth: "80%"},
        legend: {position: "none"},
    };
    var chart = new google.visualization.ColumnChart(document.getElementById("qwerty"));
    chart.draw(view, options);
}


google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBasic1);

function drawBasic1() {

    var data = google.visualization.arrayToDataTable([
        ['paxta', '2021 plan',],
        ['paxta', 8175000],
        ['Kartoshka', 3792000],
        ['Tarvuz', 2695000],
        ['Pamidor', 2099000],
        ['Piyoz', 5526000]
    ]);

    var options = {
        title: 'Yillik hosil miqdori',
        chartArea: {width: '50%'},
        hAxis: {
            title: 'Umumisy hosil: 1 500 000$',
            minValue: 0
        },
        vAxis: {
            title: 'City'
        }
    };

    var chart = new google.visualization.BarChart(document.getElementById('qwerty1'));

    chart.draw(data, options);
}