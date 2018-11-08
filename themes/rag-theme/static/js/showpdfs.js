(function(document) {
    document.addEventListener('DOMContentLoaded', function(e) {
        let publications = this.querySelectorAll('.publication[data-haspdf=false]');
        let pdfToggle = this.querySelector('#has-pdf');

        pdfToggle.addEventListener('click', function(e) {
           if(this.checked) {
                hideNoPdfs(true);
           } else {
                hideNoPdfs(false);
           }
        });

        function hideNoPdfs(hide) {
            publications.forEach(element => {
                if (hide) {
                    element.classList.add('hidden');
                } else {
                    element.classList.remove('hidden');
                }
            });
        }
        
    });
})(document);