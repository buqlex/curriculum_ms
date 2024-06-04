$(document).ready(function(){
    
    (function($) {
        "use strict";

    
    jQuery.validator.addMethod('answercheck', function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value)
    }, "Введите корректные вопросы -_-");

    // validate contactForm form
    $(function() {
        $('#contactForm').validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                },
                subject: {
                    required: true,
                    minlength: 4
                },
                number: {
                    required: true,
                    minlength: 5
                },
                email: {
                    required: true,
                    email: true
                },
                message: {
                    required: true,
                    minlength: 20
                }
            },
            messages: {
                name: {
                    required: "Да ладно, у тебя есть имя, не так ли?",
                    minlength: "Ваше имя должно состоять как минимум из 2 символов"
                },
                subject: {
                    required: "Да ладно, у тебя есть тема, не так ли?",
                    minlength: "Ваша тема должна состоять как минимум из 4 символов"
                },
                number: {
                    required: "Да ладно, у Вас есть номер, не так ли?",
                    minlength: "Ваш номер должен состоять как минимум из 5 символов"
                },
                email: {
                    required: "Нет электронной почты, нет сообщения"
                },
                message: {
                    required: "Хм... да, вам нужно что-то написать, чтобы отправить эту форму.",
                    minlength: "thats all? really?"
                }
            },
        })
    })
        
 })(jQuery)
})