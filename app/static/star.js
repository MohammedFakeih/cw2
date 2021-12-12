$(document).ready(function() {

  $('i').on('click', function() {
    console.log('hey');
  });


  $('i.fas').on({

    mouseenter: function() {
      var starId = Number($('this').attr('id'));
      console.log($('this').text());
      for (let x = 1; x <= 10; x++) {
        if (x <= starId) {
          $('this').parent().children('#' + x.toString()).addClass('canrate')
        }
        else {
          $('this').parent().children('#' + x.toString()).addClass('unrated')
        }
      }
    },

    mouseleave: function() {
      console.log('hey');
      var starId = Number($('this').attr('id'));
      for (let x = 1; x <= 10; x++) {
        if (x <= starId) {
          $('this').parent().children('#' + x.toString()).removeClass('canrate')
        }
        else if ($('this').parent().children('#' + x.toString()).hasClass('rated')) {
          $('this').parent().children('#' + x.toString()).removeClass('unrated')
        }
      }
    }});
  });
