paypal.Buttons({
    createOrder:function(data, actions){
        return actions.order.create({
            purchase_units:[{
                amount:{
                    value: '30.00'
                }
            }]
        });
    },
    onApprove: function(data, actions){
        return actions.order.capture().then(function(details) {
            alert('Transacción realizada con éxito por' + details.payer.name.given_name);
        });
    }
}).render('#paypal-button-container')
