// Library Additional JavaScript


function crud_form_loaded(formName, action) {
    // alert('Hello. I have loaded: ' + formName + ' loaded and we\'re doing ' + action);

    if (formName == "BookForm") {
        BookForm_loaded();
    }

}

function BookForm_loaded() {
    $("#id_mothers_number").on('input', update_study_id_text_field);
    $("#id_mothers_number").on('input', update_skip_patterns_for_mothers_number);

    // Example of how to populate a computed field
    // Obviously this is for display only, as it also needs to be computed on the server
    // And the server version is the only valid one
    function update_study_id_text_field() {
        $("#id_ptbi_infant_study_id").val($("#id_mothers_number").val())

    }

    // Example on how to update skip patterns for mothers_number
    // I recommend putting each pattern in a well-named, single function
    // This one hides Sequence Number if mother's number contains a 'd'
    function update_skip_patterns_for_mothers_number() {

        if ($("#id_ptbi_infant_study_id").val().includes("d")) {
            $("#div_id_sequence_number").val(""); // always clear first before hiding!
            $("#div_id_sequence_number").hide();
        }
        else
            $("#div_id_sequence_number").show();
    }

}


function attach_validator(form, htmltarget, formtarget, posttarget) {
// An example of a validator here
// http://bootstrapvalidator.votintsev.ru/settings/

    $(form)
        .bootstrapValidator({
            message: 'This value is not valid',
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            feedbackIcons: false,
            fields: {
                publication_date: {
                    validators: {
                        notEmpty: {
                            message: 'The email address is required and can\'t be empty'
                        },
                    }
                },
                title: {
                    validators: {
                        notEmpty: {
                            message: 'The title address is required and can\'t be empty'
                        },
                    }
                },

            }
        })
        .on('success.form.bv', function (e) {
            // Prevent form submission
            e.preventDefault();
            postform(event, htmltarget, formtarget, posttarget)

        });

    var datePickers = $('.datepicker');
    for (var i = 0; i < datePickers.length; i++) {
        //alert($(datePickers[0].attr('id')));
        $('#' + datePickers[0].id).on('dp.change', function (e) {
            $(form).bootstrapValidator('revalidateField', datePickers[0].name);
        });
    }
}








// Sidebar
function setAnotherURL(url) {

    CURRENT_URL = url;

    // TODO: This is some kind of easy fix, maybe we can improve this
    var setContentHeight = function () {
        // reset height
        $RIGHT_COL.css('min-height', $(window).height());

        var bodyHeight = $BODY.outerHeight(),
            footerHeight = $BODY.hasClass('footer_fixed') ? 0 : $FOOTER.height(),
            leftColHeight = $LEFT_COL.eq(1).height() + $SIDEBAR_FOOTER.height(),
            contentHeight = bodyHeight < leftColHeight ? leftColHeight : bodyHeight;

        // normalize content
        contentHeight -= $NAV_MENU.height() + footerHeight;

        $RIGHT_COL.css('min-height', contentHeight);
    };

    $SIDEBAR_MENU.find('a').on('click', function(ev) {
        var $li = $(this).parent();

        if ($li.is('.active')) {
            $li.removeClass('active active-sm');
            $('ul:first', $li).slideUp(function() {
                setContentHeight();
            });
        } else {
            // prevent closing menu if we are on child menu
            if (!$li.parent().is('.child_menu')) {
                $SIDEBAR_MENU.find('li').removeClass('active active-sm');
                $SIDEBAR_MENU.find('li ul').slideUp();
            }

            $li.addClass('active');

            $('ul:first', $li).slideDown(function() {
                setContentHeight();
            });
        }
    });

    // toggle small or large menu
    $MENU_TOGGLE.on('click', function() {
        if ($BODY.hasClass('nav-md')) {
            $SIDEBAR_MENU.find('li.active ul').hide();
            $SIDEBAR_MENU.find('li.active').addClass('active-sm').removeClass('active');
        } else {
            $SIDEBAR_MENU.find('li.active-sm ul').show();
            $SIDEBAR_MENU.find('li.active-sm').addClass('active').removeClass('active-sm');
        }

        $BODY.toggleClass('nav-md nav-sm');

        setContentHeight();
    });

    // check active menu
    $SIDEBAR_MENU.find('a[href="' + CURRENT_URL + '"]').parent('li').addClass('current-page');

    $SIDEBAR_MENU.find('a').filter(function () {
        return this.href == CURRENT_URL;
    }).parent('li').addClass('current-page').parents('ul').slideDown(function() {
        setContentHeight();
    }).parent().addClass('active');

    // recompute content when resizing
    $(window).smartresize(function(){
        setContentHeight();
    });

    setContentHeight();

}

$(document).ready(function() {
    //alert('go');
    //setAnotherURL('/library/books/')
});
