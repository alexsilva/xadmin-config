jQuery(function ($) {
    // simple storage layer
    var Storage = function () {
        this.namespace = '';
    }
    Storage.prototype.ns = function (name) {
        this.namespace = name + ".";
        return this;
    }
    Storage.prototype.get = function (key, opts) {
        return $.getCookie(this.namespace + key) || opts;
    }
    Storage.prototype.set = function (key, value) {
        $.setCookie(this.namespace + key, value);
    }
    $.storage = new Storage();
});