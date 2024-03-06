$('input').on('keyup', function () {
    if (this.value) {
        this.setAttribute('value', this.value);
    } else {
        this.removeAttribute('value');
    }
});