$(document).ready(function(){

  /*Messaging*/
  setTimeout(function(){
    $('.notice-message').fadeOut();
    $('.alert-message').fadeOut();
    $('.success-message').fadeOut();
    }, 3000);

  /*Mountain Search*/
    if($('.mountain-info').length > 0){
        var options = {
            valueNames: ['name','elevation','difficulty']
        };

        var mountainlist = new List('mtn-list-container',options);
        //End Search

        /*Highlight filter and sort options when clicked*/
        $('.filter-btn').on('click',function(){
            if($(this).hasClass('filter')){
                $('.filter').removeClass('active');
                $(this).addClass('active');
            }
            else if($(this).hasClass('sort')){
                $('.sort').removeClass('active');
                $(this).addClass('active');
            }
        })

        /*Filter options*/

        if(mountainlist.length) mountainlist.sort('name', { asc: true });
              $('#easiest-button').click(function() {
                    mountainlist.filter(function(item) {
                        if (item.values().difficulty == "Easiest") {
                            return true;
                        } else {
                            return false;
                        }
                    });
                    return false;
                });

               $('#moderate-button').click(function() {
                    mountainlist.filter(function(item) {
                        if (item.values().difficulty == "Moderate") {
                            return true;
                        } else {
                            return false;
                        }
                    });
                    return false;
                });

                $('#difficult-button').click(function() {
                    mountainlist.filter(function(item) {
                        if (item.values().difficulty == "Difficult") {
                            return true;
                        } else {
                            return false;
                        }
                    });
                    return false;
                });


                $('#most-difficult-button').click(function() {
                    mountainlist.filter(function(item) {
                        if (item.values().difficulty == "Most Difficult") {
                            return true;
                        } else {
                            return false;
                        }
                    });
                    return false;
                });


                $('#filter-none').click(function() {
                    mountainlist.filter();
                    return false;
                });
    }
     /*End filters*/

/* Weather Info */
    var coords = new Object();
    $('#weather').on('click', function(){
        var mtnName = getMountainName();
        getWeather(mtnName,"tomorrow");

    });
    /*Weather tabs*/
    $('#weather-content dd').on('click',function(){
        var mtnName = getMountainName();
        var currentTab = $(this)[0].id;

        switch(currentTab){
            case 'today':
                $('#today').addClass('active');
                $('#tomorrow,#week').removeClass('active');

                $('#today-content').show();
                $('#tomorrow-content,#week-content').hide();

                getWeather(mtnName,"today");

            break;
            case 'tomorrow':
                $('#tomorrow').addClass('active');
                $('#today,#week').removeClass('active');

                $('#tomorrow-content').show();
                $('#today-content,#week-content').hide();

                getWeather(mtnName,"tomorrow");

            break;
            case 'week':
                $('#week').addClass('active');
                $('#tomorrow,#today').removeClass('active');

                $('#week-content').show();
                $('#tomorrow-content,#today-content').hide();

                 getWeather(mtnName,"week");

            break;
            default:
                alert('Whoops! There was an error');
            break;
        }
    })

/*end weather info*/

    $('#cancelbtn').on('click',function(){
        window.location = "list";
    });

    /*Date and time pickers*/
    var datepicker = $('.datepicker');
    var timepicker = $('.timepicker');

    if(datepicker) datepicker.pickadate();
    if(timepicker) timepicker.pickatime();

});


/*
* Get current weather data from openweathermap and populate the appropriate fields
* Author: Ed
*/
function getWeather(mtnName, day){
    var url = "/mountains/get_weather";
    $.ajax({
        url: url,
        type: "get",
        dataType: 'json',
        cache: true,
        data:{mountain:mtnName,day:day},
        beforeSend: function(){
            $('#' + day + '-content').hide();
            $('.credit').hide();
            $('.loading').show();
        },
        complete: function(){
            $('#' + day + '-content').show();
            $('.credit').show();
            $('.loading').hide();
        },
        success: function( weather ) {

            if(day == 'week'){
                getWeekForecast(weather[0], weather[1]);
            } else {
                $('#' + day + '-img').attr('src', weather.image);
                $('#' + day + '-desc').text(weather.desc);
                $('#' + day + '-speed').text("Speed: " + weather.wind_speed);
                $('#' + day + '-dir').text("Direction: " + weather.wind_dir + "\xB0");
                $('#' + day + '-temp').html(weather.temp);
                $('#' + day + '-clouds').text(weather.clouds + '%');
                $('#' + day + '-humidity').text(weather.humidity + '%');
            }

        },
        error: function(){
            console.log('error')
        }
    });
}


/*
* Same as getWeather, but for the whole week
* Author: Ed
*/
function getWeekForecast(weather, unit){
    var weatherStats = ['img','desc','speed','dir','temp','clouds','humidity'];
    $.each(weather,function(i,v){

            var unixtime = weather[i]['dt'];
            var date = new Date(unixtime * 1000); //js does unix time in milliseconds
            var day = UnixDayToCalDay(date.getDay());

            $('#day-' + i).text(day);

        $.each(weatherStats,function(index,stat){

            var timeframeID = "#week-" + stat + "-" + i;
            var unit_multiply = unit == 'F' ? 1 : 3.6
            var speed_unit = unit == 'F' ? ' mph' : ' km/h'

            switch(stat){
                case 'img':
                    var icon = weather[i]['weather'][0]['icon']
                    var desc = weather[i]['weather'][0]['description'];

                    $(timeframeID).attr('src', 'http://openweathermap.org/img/w/' + icon + '.png')
                    $(timeframeID).attr('title', desc);
                break
                case 'desc':
                    $(timeframeID).text(weather[i]['weather'][0]['description']);
                break
                case 'speed':
                    var speed = (weather[i]['speed'] * unit_multiply).toFixed(2) + speed_unit;
                    $(timeframeID).text(speed);
                break
                case 'dir':
                    var direction = "Direction: " + weather[i]['deg'] + "\xB0";
                    $(timeframeID).text(direction);
                break
                case 'temp':
                    var temp = Math.round(weather[i]['temp']['day'])
                    $(timeframeID).text(temp);
                break
                case 'clouds':
                    $(timeframeID).text(weather[i]['clouds'] + '%');
                break
                case 'humidity':
                    $(timeframeID).text(weather[i]['humidity'] + '%');
                break
            }
        })
    })
}

/*
* Checks the current URL and gets the mountain name
* Author: Ed
*/
function getMountainName(){
    var url = document.URL;
    var query = url.match("mountains/(.*)(?=/)|(name=.*)");
    var name = decodeURIComponent(query[0]);

    //This works for now, but will need to be rewritten
    name = name.replace(/\+/g, " ")
    name = name.replace("name=","")
    name = name.replace(new RegExp('#(.*)'), "");
    name = name.replace("mountains/", "")

    return name;
}


/*
* Takes the day provided by JS getDay and converts it to the appropriate word
* Author: Ed
*/
function UnixDayToCalDay(Uday){
    switch(Uday){
        case 0:
            var day = 'Sunday';
        break
        case 1:
            var day = 'Monday';
        break
        case 2:
            var day = 'Tuesday';
        break
        case 3:
            var day = 'Wednesday';
        break
        case 4:
            var day = 'Thursday';
        break
        case 5:
            var day = 'Friday';
        break
        case 6:
            var day = 'Saturday';
        break
    }

    return day;
}

$(window).scroll(function(){
    if ($(window).scrollTop() >= 228) {
        $('#search-container').addClass('fixed');
        $('#mountain-list').addClass('margin-top');
    }
    else {
        $('#search-container').removeClass('fixed');
        $('#mountain-list').removeClass('margin-top');
    }
});
