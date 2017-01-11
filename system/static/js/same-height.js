var selector = '.foro-topic .col-sm-3 .card, .foro-types .col-sm-3 .card, .foro .col-sm-4 .card',
                selectores = selector.split(',');
            $(window).load(function () {
                try {
                    var h = [];
                    var getHeight = function () {
                        h.push($(this).height());
                    };
                    selectores.forEach(function (element) {
                        h = [];
                        $(element.trim()).each(getHeight);
                        var alto = Math.max.apply(null, h);
                        $(element.trim()).height(alto);
                    });
                }
                catch (err) {

                }
            });