$('#myTab a').click(function (e) {
  e.preventDefault()
  $(this).tab('show')
})

$(document).ready(function () {
      $('.registry-page').find('.btn-edit-submit').click(function (event) {
          if($('#id_name').val() == '' || $('#id_last_name').val() == ''
              || $('#id_gender').val() == '' || $('#id_born_date').val() == ''
              || $('#id_nationality').val() == '' || $('#id_institution').val() == ''
              || $('#id_identification').val() == '' )  {
                var active_li = $('#myTab').find('.active');
                var active_tab = $('#myTabContent').find('.active');
                active_li.removeClass('active');
                active_tab.removeClass('active');
                active_tab.removeClass('in');
                $('#myTab').find('.about').addClass('active');
                $('#myTabContent').find('#simple_profile').addClass('active');
                $('#myTabContent').find('#simple_profile').addClass('in');
          }
          else if ($('#id_alimentary_restriction').val() == '' || $('#id_health_consideration').val() == '') {
              var active_li = $('#myTab').find('.active');
              var active_tab = $('#myTabContent').find('.active');
              active_li.removeClass('active');
              active_tab.removeClass('active');
              active_tab.removeClass('in');
              $('#myTab').find('.medical').addClass('active');
              $('#myTabContent').find('#medical_profile').addClass('active');
              $('#myTabContent').find('#medical_profile').addClass('in');
          }
          else if ($('#id_letter').val() == '' || $('#id_entry_country').val() == ''
              || $('#id_out_country').val() == '' || $('#entry_port').val() == ''
              || $('#id_out_port').val() == '' || $('#id_entry_country_date').val() == ''
              || $('#id_out_country_date').val() == '' ) {

                var active_li = $('#myTab').find('.active');
                var active_tab = $('#myTabContent').find('.active');
                active_li.removeClass('active');
                active_tab.removeClass('active');
                active_tab.removeClass('in');
                $('#myTab').find('.in_out').addClass('active');
                $('#myTabContent').find('#in_out_profile').addClass('active');
                $('#myTabContent').find('#in_out_profile').addClass('in');
          }
      })
    }
);