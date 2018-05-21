$.postJson = function (url, data) {
    var csrf = $("[name=csrfmiddlewaretoken]").val();
    var deferred = new $.Deferred();
    $.ajax({
        headers: { "X-CSRFToken": csrf },
        url: url,
        dataType: 'json',
        type: 'post',
        contentType: 'application/json',
        data: JSON.stringify(data),
        processData: false,
    })
        .done(function(res) {deferred.resolve(res)})
        .fail(function(res) {deferred.reject(res)});
    return deferred;
};

var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        form: {
            server: '192.168.0.10:8332',
            username: 'test',
            password: 'test'
        },
        addresses: [],
        balance: 'N/A',
        //Enables or disables buttons
        buttons: {
            balance: true,
            newAddress: true,
        }
    },
    mounted: function () {
        this.getAddresses();
        this.checkBalance();
    },
    methods: {
        checkBalance: function() {
            var self = this;
            self.buttons.balance = false;
            $.postJson('/balance', this.form)
                .done(function (res) {
                    console.log(res.data);
                    self.balance = res.data;
                })
                .fail(function (res) {
                    console.error(res)
                })
                .always(function () {
                    self.buttons.balance = true;
                });
        },
        getNewAddress: function () {
            var self = this;
            self.buttons.newAddress = false;
            $.postJson('/newaddress', this.form)
                .done(function (res) {
                    console.log(res.data);
                    self.addresses.push(res.data);
                })
                .fail(function (res) {
                    console.error(res)
                })
                .always(function () {
                    self.buttons.newAddress = true;
                });
        },
        getAddresses: function () {
            var self = this;
            $.postJson('/addresses', this.form)
                .done(function (res) {
                    console.log(res.data);
                    self.addresses = res.data;
                })
                .fail(function (res) {
                    console.error(res)
                });
        }
    }
});